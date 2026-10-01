# 资料格式与核验要求

路径均相对于雅思项目根目录，文件使用 UTF-8。未知字段写 `null` 或 `unknown`，不能推断补齐评分或考生身份。

## 索引

`library/index.json` 保存目标及 `standards`、`prompts`、`samples`、`evaluations`。样本数量从已核实记录计算，不把目标当作实际进度。

标准和提示词记录包含 `id`、`path`、`source_url`、`author_or_publisher`、`version`、`accessed_at`、`status`、适用任务 `tasks`。标准记录官方出处及发布日期。提示词另记录 `kind`、源提示词编号和修改说明。

只有文件存在且来源和内容完成核验才标记 verified；未采用的候选材料保留并记录原因。

## 作文

每条样本索引至少包含：

- `id`、`task`（task1/task2）、`task_type`、`path`；
- `source_url`、`source_locator`、`accessed_at`；
- `score_source`、`rater_evidence`；
- `candidate_region`、`region_evidence`，不能确认时写 unknown；
- `status`、`split`、`duplicate_group`、`prompt_group` 及可获知的 `author_group`。

索引不放入 holdout 的分数或评语。reference 可保存人工总分、真实分项分数和评语；holdout 标签另存，预测锁定后才能读取。

只用该篇单独评分作标签；考生 Writing 成绩单总分不能作为某一篇分数。缺少真实分项时不得从总分反推。教师评分不升级为官方考官评分。

中国地区身份须有来源证据；中文网站、姓名或语言错误不能证明地域。优先符合地域偏好的样本，缺失时如实说明。

保留原稿错误，核对 OCR 和转写。Task 1 保留可辨认图表或完整可核对数据。缺少可靠评分的材料不算校准样本。

来源核实与标签可靠度分别记录。新增记录使用 `label_scope`、`label_review_status`、`source_context_region` 及证据。整本合集的笼统分档不计入单篇精确标签；逐篇区间分可以计数，但不能用于点值 MAE。

发现评分证据矛盾时，保留原始分数和原件，在 `quality_issues` 定位问题，先改为 candidate。来源、原稿版本或评分者存在矛盾时，整篇不得用于锚点。矛盾仅属于某个分项、且其他分项的封面与独立批改页明确一致时，可逐项核验无争议分项：`criterion_quarantine` 必须保留全部争议说明、被排除的标签及每个可用分项两份证据的路径与哈希；争议分项和总分从可用 `traits`、`overall`、`band_low`、`band_high` 中移除，原始值另存 `raw_published_scores`。此时 verified 仅表示仍留在可用字段的分项已核实；不得补推、恢复或计入被隔离标签。缺少上述证据仍整篇排除。教师的半分分项照录，不擅自改写。

## 拆分和评估

重复转载和同篇改写归为同组，不能分散到参考集和留出集。尽可能按题目与作者分组留出，在调整评分规则前确定拆分。

留出集答案不进入评分输入。先保存作文编号、预测、运行标识、资料版本和日期，再读标签计算误差。已读过答案的运行不是盲测。

当前建设为每个任务四项的6、7、8、9整数档，每格至少10篇去重原稿，共32格；不扩建更低分档。数量不能替代真实人工分项、原稿与题图核验。历史每档25篇、每类175篇是旧总分资料收集目标，不是本版每次校准的硬门。

项目半分以相邻整数档的独立比较证据判断；不再强制搜集半分标签作为先决条件。总分半分、区间分、AI评分和自行平均不能填入精确分项格。多个真实评分使用 `human_ratings` 分别保存评分者、总分、分项、来源与意见；不能平均、反推或事后选择最接近模型的标签。有最终联合结果时保留其优先级，不能为补半分挑旧评分。

新增线索和接纳/拒绝原因见 `research/anchor-refresh-20260930/REPORT.md`；未经原稿、评分及题图核验的线索不能因网页可读而标记verified。索引中的总分coverage不等于分项锚点覆盖。`python -X utf8 scripts/integer_anchor_inventory.py`可只读检查提示词锁和32格库存；旧v1.3审计保留为历史脚本；结果不是逐篇原稿核验或评分测试。

教师原创稿计入配额时，须保存 `sample_kind=teacher_model`、`author_type=teacher`、`independent_human_rating=true`，并核对逐篇分数、评语、评分者出处和批改前原稿。作者与评分者角色不得混写。
