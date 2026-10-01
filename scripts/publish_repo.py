"""Publish this sanitized tree with the authenticated GitHub CLI."""
from __future__ import annotations

import base64
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GH = Path(r"C:/Users/Pc/AppData/Local/IELTSWritingCoach/publish-tools/gh-2.102.0/extracted/bin/gh.exe")
OWNER = "Li2882"
REPO = "best-ielts-writing-skill"


def api(path: str, method: str = "GET", body: dict | None = None) -> dict:
    command = [str(GH), "api", path]
    if method != "GET":
        command += ["--method", method]
    if body is not None:
        command += ["--input", "-"]
    result = subprocess.run(command, input=json.dumps(body) if body is not None else None,
                            text=True, capture_output=True, check=True)
    return json.loads(result.stdout)


def files() -> list[Path]:
    excluded = {".git", "library", "research", "reviews", "local-materials", ".tools", "__pycache__"}
    return sorted(p for p in ROOT.rglob("*") if p.is_file() and not any(part in excluded for part in p.parts))


def main() -> None:
    # GitHub does not allow Git database blobs in a completely empty repository.
    # Seed the branch through the Contents API, then make one atomic Git commit.
    readme = base64.b64encode((ROOT / "README.md").read_bytes()).decode("ascii")
    api(f"repos/{OWNER}/{REPO}/contents/README.md", "PUT", {
        "message": "Initialize repository", "content": readme,
    })
    head = api(f"repos/{OWNER}/{REPO}/git/ref/heads/main")
    parent = head["object"]["sha"]
    parent_commit = api(f"repos/{OWNER}/{REPO}/git/commits/{parent}")
    paths = files()
    entries = []
    for path in paths:
        relative = path.relative_to(ROOT).as_posix()
        encoded = base64.b64encode(path.read_bytes()).decode("ascii")
        blob = api(f"repos/{OWNER}/{REPO}/git/blobs", "POST",
                   {"content": encoded, "encoding": "base64"})
        entries.append({"path": relative, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    tree = api(f"repos/{OWNER}/{REPO}/git/trees", "POST", {
        "base_tree": parent_commit["tree"]["sha"], "tree": entries,
    })
    commit = api(f"repos/{OWNER}/{REPO}/git/commits", "POST", {
        "message": "Publish IELTS Writing Coach skill and research record",
        "tree": tree["sha"],
        "parents": [parent],
    })
    api(f"repos/{OWNER}/{REPO}/git/refs/heads/main", "PATCH", {"sha": commit["sha"], "force": False})
    api(f"repos/{OWNER}/{REPO}/topics", "PUT", {"names": ["ielts", "ielts-writing", "writing-feedback", "codex-skill", "ai-writing"]})
    print(json.dumps({"repository": f"https://github.com/{OWNER}/{REPO}", "files": len(paths),
                      "commit": commit["sha"], "tree": tree["sha"]}))


if __name__ == "__main__":
    main()
