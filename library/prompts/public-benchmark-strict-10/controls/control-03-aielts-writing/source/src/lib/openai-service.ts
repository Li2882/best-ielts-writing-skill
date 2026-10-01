// OpenAI-compatible API service for writing evaluation

interface ApiResponse {
  submission: {
    userId: string;
    questionId: string;
    taskType: string;
    isAIWriting: boolean;
    topic: string;
    content: string;
    AiMotivation: string;
    AiSuggestions: string;
    AiGenerateWriting: string;
    ReWriteImprovementVersion: string;
    TotalGrammerError: string;
    TotalVocabularyError: string;
    TotalSentenceError: string;
    ReWriteCorrectWords: string;
    ReWriteCorrectSentences: string;
    score: {
      taskAchievement: number;
      coherenceAndCohesion: number;
      lexicalResource: number;
      grammaticalRangeAndAccuracy: number;
      overallBandScore: number;
    };
    feedback: string;
    detailedFeedback: {
      taskAchievement: { score: number };
      coherenceAndCohesion: { score: number };
      lexicalResource: { score: number };
      grammaticalRangeAndAccuracy: { score: number };
    };
    evaluator: string;
    status: string;
    submissionDate: string;
    _id: string;
    createdAt: string;
    updatedAt: string;
    __v: number;
  };
  progress: {
    writingLevel: string;
    currentQuestionIndex: number;
    averageScore: number;
    completedQuestions: number;
  };
}

class OpenAIService {
  private static getPrompt(): string {
    return `You are an expert IELTS writing evaluator. Analyze the provided writing sample and return a JSON response with detailed evaluation following IELTS scoring criteria.

CRITICAL INSTRUCTIONS:
1. You MUST return ONLY a valid JSON object, no additional text
2. The JSON must match the exact structure provided below
3. All scores should be on a scale of 0.0 to 9.0 (IELTS band scores)
4. Provide detailed, constructive feedback in British English
5. Analyze for grammar, vocabulary, coherence, and task achievement
6. Detect potential AI-generated content characteristics
7. Provide specific error corrections and improvements

Required JSON structure:
{
  "submission": {
    "userId": "user_[random_5_digits]",
    "questionId": "q_[random_3_digits]",
    "taskType": "Task 1" or "Task 2",
    "isAIWriting": boolean (true if likely AI-generated),
    "topic": "Brief topic description based on content",
    "content": "The original submitted text",
    "AiMotivation": "Encouraging message (50-100 words)",
    "AiSuggestions": "Specific improvement suggestions (100-150 words)",
    "AiGenerateWriting": "Percentage estimate (e.g., '15%')",
    "ReWriteImprovementVersion": "Improved version of the text",
    "TotalGrammerError": "Number as string (e.g., '3')",
    "TotalVocabularyError": "Number as string (e.g., '2')",
    "TotalSentenceError": "Number as string (e.g., '1')",
    "ReWriteCorrectWords": "❌ wrong_word → ✅ correct_word format, separated by ❌",
    "ReWriteCorrectSentences": "❌ wrong_sentence → ✅ correct_sentence format, separated by ❌",
    "score": {
      "taskAchievement": number (0.0-9.0),
      "coherenceAndCohesion": number (0.0-9.0),
      "lexicalResource": number (0.0-9.0),
      "grammaticalRangeAndAccuracy": number (0.0-9.0),
      "overallBandScore": number (0.0-9.0, average of above four)
    },
    "feedback": "Overall detailed feedback (200-300 words)",
    "detailedFeedback": {
      "taskAchievement": { "score": number },
      "coherenceAndCohesion": { "score": number },
      "lexicalResource": { "score": number },
      "grammaticalRangeAndAccuracy": { "score": number }
    },
    "evaluator": "AI IELTS Evaluator v2.0",
    "status": "completed",
    "submissionDate": "ISO date string",
    "_id": "eval_[random_string]",
    "createdAt": "ISO date string",
    "updatedAt": "ISO date string",
    "__v": 0
  },
  "progress": {
    "writingLevel": "Beginner|Intermediate|Advanced based on overall score",
    "currentQuestionIndex": random number 1-50,
    "averageScore": same as overallBandScore,
    "completedQuestions": random number 1-20
  }
}

IMPORTANT: Return ONLY the JSON object. No markdown formatting, no explanations, just the JSON.

Writing to evaluate: `;
  }

  static async fetchModels(): Promise<string[]> {
    try {
      let baseUrl = localStorage.getItem("writing_api_base_url") || "https://api.openai.com/v1";
      
      // Ensure the URL has a protocol
      if (!baseUrl.startsWith('http://') && !baseUrl.startsWith('https://')) {
        baseUrl = 'https://' + baseUrl;
      }
      
      const response = await fetch(`${baseUrl}/models`);
      
      if (!response.ok) {
        console.warn("Failed to fetch models from API");
        return ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"];
      }

      const data = await response.json();
      
      // Handle different response formats
      if (data.data && Array.isArray(data.data)) {
        return data.data.map((model: any) => model.id || model.name || model);
      } else if (Array.isArray(data)) {
        return data.map((model: any) => model.id || model.name || model);
      }
      
      return ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"];
    } catch (error) {
      console.warn("Error fetching models:", error);
      return ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"];
    }
  }

  static async evaluateWriting(text: string): Promise<ApiResponse> {
    const apiKey = localStorage.getItem("writing_api_key");
    let baseUrl = localStorage.getItem("writing_api_base_url") || "https://api.openai.com/v1";
    const selectedModel = localStorage.getItem("writing_selected_model") || "gpt-4o-mini";

    if (!apiKey) {
      throw new Error("API key not configured");
    }

    // Ensure the URL has a protocol
    if (!baseUrl.startsWith('http://') && !baseUrl.startsWith('https://')) {
      baseUrl = 'https://' + baseUrl;
    }

    const fullUrl = `${baseUrl}/chat/completions`;
    console.log("Making API request to:", fullUrl);
    console.log("Using model:", selectedModel);

    const response = await fetch(fullUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${apiKey}`,
      },
      body: JSON.stringify({
        model: selectedModel,
        messages: [
          {
            role: "user",
            content: this.getPrompt() + text
          }
        ],
        temperature: 0.7,
        max_tokens: 4000
      })
    });

    if (!response.ok) {
      const errorText = await response.text().catch(() => "Unknown error");
      console.error("API Error Response:", {
        status: response.status,
        statusText: response.statusText,
        url: response.url,
        headers: Object.fromEntries(response.headers.entries()),
        body: errorText
      });
      throw new Error(`API Error: ${response.status} ${response.statusText} - URL: ${response.url} - Response: ${errorText}`);
    }

    const data = await response.json();
    console.log("API Response:", data);
    
    // Handle OpenAI API response format
    let content = data.choices?.[0]?.message?.content || data.choices?.[0]?.text;
    
    // Fallback for other API formats
    if (!content) {
      content = data.response || data.output || data.text || data.content;
    }

    if (!content) {
      console.error("No content found in response:", data);
      throw new Error("No response content received from API");
    }

    try {
      // Clean the response to ensure it's valid JSON
      const cleanedContent = content.trim().replace(/^```json\n?|\n?```$/g, '');
      const result = JSON.parse(cleanedContent);

      // Validate the response structure
      if (!result.submission || !result.progress) {
        throw new Error("Invalid response structure");
      }

      return result as ApiResponse;
    } catch (parseError) {
      console.error("Failed to parse API response:", content);
      throw new Error("Invalid JSON response from API. Response: " + content.substring(0, 200) + "...");
    }
  }

  static isConfigured(): boolean {
    return !!(localStorage.getItem("writing_api_key") && localStorage.getItem("writing_api_base_url"));
  }
}

export default OpenAIService;