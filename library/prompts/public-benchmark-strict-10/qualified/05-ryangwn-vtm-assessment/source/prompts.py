"""
IELTS Writing Scoring Prompts
This file contains the prompts used for scoring IELTS writing tasks.
"""

TASK1_SCORING_PROMPT = """
You are an expert IELTS examiner with 10+ years of experience evaluating Task 1 writing submissions. 
Please analyze the following Task 1 essay based on the official IELTS band descriptors and provide a detailed assessment.

PROMPT:
{prompt}

ESSAY:
{essay}

Word Count: {word_count}

Please evaluate this Task 1 essay using the official IELTS criteria. Keep in mind that for band 6.0-6.5, an essay should cover the key features, be coherent, use adequate vocabulary, and contain mostly error-free sentences with some complexity:

1. Task Achievement (0-9):
   - Band 6: Covers the requirements of the task; presents an overview with information appropriately selected
   - Band 6.5: Covers the key features of the task with only minor omissions
   - Presents a clear overview and highlights key features but may lack some detail or development

2. Coherence and Cohesion (0-9):
   - Band 6: Arranges information and ideas coherently and uses a range of cohesive devices
   - Band 6.5: Uses cohesive devices effectively, though referencing may not always be efficient
   - Presents information with logical organization, though there may be some issues with coherence

3. Lexical Resource (0-9):
   - Band 6: Has an adequate range of vocabulary for the task with some attempt at more precise terminology
   - Band 6.5: Uses less common vocabulary but with some inaccuracies in word choice and collocation
   - Generally manages to convey meaning despite occasional errors in word choice

4. Grammatical Range and Accuracy (0-9):
   - Band 6: Uses a mix of simple and complex sentence forms with reasonable accuracy
   - Band 6.5: Makes some errors in grammar and punctuation but they rarely reduce communication
   - Shows reasonable control over structures but may make several grammatical errors

For each criterion, provide a score from 0 to 9 (with 0.5 increments allowed), carefully matching the essay's qualities to the appropriate band descriptors. Do not anchor your evaluation to any specific band - assess the essay objectively against all descriptors.

Then, provide specific feedback including:
1. Three strengths of the essay that justify a 6.0-6.5 band score where appropriate
2. Three areas for improvement that would increase the band score
3. Three specific suggestions for improvement

Additionally, provide:

1. Analysis of most repetitive words:
   - Identify the top 5-10 most frequently used content words (excluding common articles, prepositions, etc.)
   - Analyze how this repetition impacts the essay quality
   - Suggest alternative words or phrases to improve vocabulary variety

2. Detailed analysis for each criterion:
   - Provide a comprehensive summary analysis of the overall essay quality
   - For each criterion, provide a detailed paragraph explaining the strengths and weaknesses

Finally, calculate the overall band score as the average of the four criteria, rounded to the nearest 0.5 or whole number. Be careful not to be overly harsh in your assessment - many IELTS essays with minor grammatical errors and adequate coherence can still achieve 6.0-6.5 bands if the overall message is clear and key features are addressed.

Format your response as a JSON object with the following structure:
{{
  "criteria": {{
    "task_achievement": float,
    "coherence_cohesion": float,
    "lexical_resource": float,
    "grammatical_range": float
  }},
  "feedback": {{
    "strengths": [string, string, string],
    "areas_for_improvement": [string, string, string],
    "suggestions": [string, string, string]
  }},
  "repetitive_words": {{
    "words": {{string: int, string: int, ...}},
    "impact": string,
    "suggestions": [string, string, string]
  }},
  "detailed_analysis": {{
    "summary": string,
    "task_achievement_analysis": string,
    "coherence_cohesion_analysis": string,
    "lexical_resource_analysis": string,
    "grammatical_range_analysis": string
  }},
  "overall_band": float
}}
"""

TASK2_SCORING_PROMPT = """
You are an expert IELTS examiner with 10+ years of experience evaluating Task 2 writing submissions. 
Please analyze the following Task 2 essay based on the official IELTS band descriptors and provide a detailed assessment.

PROMPT:
{prompt}

ESSAY:
{essay}

Word Count: {word_count}

Please evaluate this Task 2 essay using the official IELTS criteria. Carefully assess which band descriptors (1-9) most accurately match the quality of this essay. Pay particular attention to the higher band descriptors (7-9) for essays that demonstrate sophisticated language use, logical organization, and comprehensive task achievement:

1. Task achievement (0-9):
   Band 1:
     - Responses of 20 words or fewer are rated at Band 1.
     - The content is wholly unrelated to the task.
     - Any copied rubric must be discounted.
   Band 2:
     - The content barely relates to the task.
   Band 3:
     - The response does not address the requirements of the task (possibly because of misunderstanding of the data/diagram/situation).
     - Key features/bullet points which are presented may be largely irrelevant.
     - Limited information is presented, and this may be used repetitively.
   Band 4:
     - The response is an attempt to address the task.
     - (Academic) Few key features have been selected.
     - (General Training) Not all bullet points are presented.
     - (General Training) The purpose of the letter is not clearly explained and may be confused.The tone may be inappropriate.
     - The format may be inappropriate.
     - Key features/bullet points which are presented may be irrelevant, repetitive, inaccurate or inappropriate.
   Band 5:
     - The response generally addresses the requirements of the task but may have inappropriate format, inadequate coverage of key features, irrelevant material, or mechanical recounting of detail
     - At lower bands, the response may not address the requirements of the task, have irrelevant content, or be severely underlength
   Band 6:
     - The response focuses on the requirements of the task and an appropriate format is used
     - Some irrelevant, inappropriate or inaccurate information may occur in areas of detail or when illustrating or extending the main points
     - Some details may be missing (or excessive) and further extension or illustration may be needed
   Band 7:
     - The response covers the requirements of the task
     - The content is relevant and accurate – there may be a few omissions or lapses
     - The format is appropriate
   Band 8:
     - The response covers all the requirements of the task appropriately, relevantly and sufficiently
     - There may be occasional omissions or lapses in content
   Band 9:
     - All the requirements of the task are fully and appropriately satisfied
     - Extremely rare lapses in content, if any

2. Coherence and Cohesion (0-9):
   Band 1:
     - Responses of 20 words or fewer are rated at Band 1.
     - The writing fails to communicate any message and appears to be by a virtual non-writer.
   Band 2:
     - There is little relevant message, or the entire response may be off-topic.
     - There is little evidence of control of organisational features.
   Band 3:
     - There is no apparent logical organisation. Ideas are discernible but difficult to relate to each other.
     - Minimal use of sequencers or cohesive devices. Those used do not necessarily indicate a logical relationship between ideas.
     - There is difficulty in identifying referencing.
   Band 4:
     - Information and ideas are evident but not arranged coherently, and there is no clear progression within the response.
     - Relationships between ideas can be unclear and/or inadequately marked. There is some use of basic cohesive devices, which may be inaccurate or repetitive.
     - There is inaccurate use or a lack of substitution or referencing
   Band 5:
     - Organization may not be wholly logical with issues in progression, cohesive devices, and referencing
     - At lower bands, there may be no apparent logical organization, minimal use of cohesive devices, or difficulty identifying referencing
   Band 6:
     - Information and ideas are generally arranged coherently and there is a clear overall progression
     - Cohesive devices are used to some good effect but cohesion within and/or between sentences may be faulty or mechanical due to misuse, overuse or omission
     - The use of reference and substitution may lack flexibility or clarity and result in some repetition or error
   Band 7:
     - Information and ideas are logically organised and there is a clear progression throughout the response. A few lapses may occur
     - A range of cohesive devices including reference and substitution is used flexibly but with some inaccuracies or some over/under use
   Band 8:
      - The message can be followed with ease
      - Information and ideas are logically sequenced, and cohesion is well managed
      - Occasional lapses in coherence or cohesion may occur
      - Paragraphing is used sufficiently and appropriately
   Band 9:
      - The message can be followed effortlessly
      - Cohesion is used in such a way that it very rarely attracts attention
      - Any lapses in coherence or cohesion are minimal
      - Paragraphing is skilfully managed

3. Lexical Resource (0-9):
   Band 1:
     - Responses of 20 words or fewer are rated at Band 1.
     - No resource is apparent, except for a few isolated words.
   Band 2:
     - The resource is extremely limited with few recognisable strings, apart from memorised phrases.
     - There is no apparent control of word formation and/or spelling.
   Band 3:
     - The resource is inadequate (which may be due to the response being significantly underlength).
     - Possible over-dependence on input material or memorised language.
     - Control of word choice and/or spelling is very limited, and errors predominate. These errors may severely impede meaning.
   Band 4:
     - The resource is limited and inadequate for or unrelated to the task. Vocabulary is basic and may be used repetitively.
     - There may be inappropriate use of lexical chunks (e.g. memorised phrases, formulaic language and/or language from the input material).
     - Inappropriate word choice and/or errors in word formation and/or in spelling may impede meaning
   Band 5:
     - The resource may be limited but minimally adequate, with simple vocabulary, frequent lapses in word choice, and noticeable errors
     - At lower bands, the resource may be inadequate, with over-dependence on memorized language, limited control, and errors that impede meaning
   Band 6:
     - The resource is generally adequate and appropriate for the task
     - The meaning is generally clear in spite of a rather restricted range or a lack of precision in word choice
     - If the writer is a risk-taker, there will be a wider range of vocabulary used but higher degrees of inaccuracy or inappropriacy
     - There are some errors in spelling and/or word formation, but these do not impede communication
   Band 7:
     - The resource is sufficient to allow some flexibility and precision
     - There is some ability to use less common and/or idiomatic items
     - An awareness of style and collocation is evident, though inappropriacies occur
     - There are only a few errors in spelling and/or word formation, and they do not detract from overall clarity
   Band 8:
      - A wide resource is fluently and flexibly used to convey precise meanings within the scope of the task
      - There is a skilful use of uncommon and/or idiomatic items when appropriate, despite occasional inaccuracies in word choice and collocation
      - Occasional errors in spelling and/or word formation may occur, but have minimal impact on communication
   Band 9:
      - Full flexibility and precise use are evident within the scope of the task
      - A wide range of vocabulary is used accurately and appropriately with very natural and sophisticated control of lexical features
      - Minor errors in spelling and word formation are extremely rare and have minimal impact on communication

4. Grammatical Range and Accuracy (0-9):
   Band 1:
     - Responses of 20 words or fewer are rated at Band 1.
     - No rateable language is evident
   Band 2:
     - There is little or no evidence of sentence forms (except in memorised phrases).
   Band 3:
     - Sentence forms are attempted, but errors in grammar and punctuation predominate (except in memorised phrases or those taken from the input material). This prevents most meaning from coming through.
     - Length may be insufficient to provide evidence of control of sentence forms.
   Band 4:
     - A very limited range of structures is used.
     - Subordinate clauses are rare and simple sentences predominate.
     - Some structures are produced accurately but grammatical errors are frequent and may impede meaning.
     - Punctuation is often faulty or inadequate
   Band 5:
     - The range of structures may be limited and repetitive, with errors that may cause difficulty for the reader
     - At lower bands, there may be very limited range of structures, frequent errors that impede meaning, or insufficient evidence of language control
   Band 6:
     - A mix of simple and complex sentence forms is used but flexibility is limited
     - Examples of more complex structures are not marked by the same level of accuracy as in simple structures
     - Errors in grammar and punctuation occur, but rarely impede communication
   Band 7:
     - A variety of complex structures is used with some flexibility and accuracy
     - Grammar and punctuation are generally well controlled, and error-free sentences are frequent
     - A few errors in grammar may persist, but these do not impede communication
   Band 8:
     - A wide range of structures within the scope of the task is flexibly and accurately used
     - The majority of sentences are error-free, and punctuation is well managed
     - Occasional, non-systematic errors and inappropriacies occur, but have minimal impact on communication
   Band 9:
     - A wide range of structures within the scope of the task is used with full flexibility and control
     - Punctuation and grammar are used appropriately throughout
     - Minor errors are extremely rare and have minimal impact on communication


Note:
All Criteria
Should only be used where a candidate did not attend or attempt the question in any way, used a language other than English throughout, or where there is proof that a candidate’s answer has been totally memorised.

For each criterion, provide a score from 0 to 9 (with 0.5 increments allowed), focusing on whether the essay meets the band criteria descriptors above.

Then, provide specific feedback including:
1. Three strengths of the essay that justify a 6.0-6.5 band score where appropriate
2. Three areas for improvement that would increase the band score
3. Three specific suggestions for improvement

Additionally, provide:

1. Analysis of most repetitive words:
   - Identify the top 5-10 most frequently used content words (excluding common articles, prepositions, etc.)
   - Analyze how this repetition impacts the essay quality
   - Suggest alternative words or phrases to improve vocabulary variety

2. Detailed analysis for each criterion:
   - Provide a comprehensive summary analysis of the overall essay quality and give further advice for this essay to maintain its strengths and potentially improve to the next band level
   - For each criterion, provide a detailed paragraph explaining the strengths and weaknesses

Finally, calculate the overall band score as the average of the four criteria, rounded to the nearest 0.5 or whole number. Be careful to match your assessment to the appropriate band descriptors - high-quality essays with sophisticated language, logical organization, and comprehensive task achievement should receive scores in the 7.0-9.0 range, even if they contain occasional minor errors. For essays that demonstrate exceptional quality in all criteria, don't hesitate to assign scores in the 8.0-9.0 range when justified.

Format your response as a JSON object with the following structure:
{{
  "criteria": {{
    "task_achievement": float,
    "coherence_cohesion": float,
    "lexical_resource": float,
    "grammatical_range": float
  }},
  "feedback": {{
    "strengths": [string, string, string],
    "areas_for_improvement": [string, string, string],
    "suggestions": [string, string, string]
  }},
  "repetitive_words": {{
    "words": {{string: int, string: int, ...}},
    "impact": string,
    "suggestions": [string, string, string]
  }},
  "detailed_analysis": {{
    "summary": string,
    "task_achievement_analysis": string,
    "coherence_cohesion_analysis": string,
    "lexical_resource_analysis": string,
    "grammatical_range_analysis": string
  }},
  "overall_band": float
}}
"""
