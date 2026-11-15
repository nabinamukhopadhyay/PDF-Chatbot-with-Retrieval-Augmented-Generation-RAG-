from src.model import load_model
from langchain_classic.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

template = """
You are a highly experienced ATS (Applicant Tracking System) evaluator and senior technical hiring manager.

Your task is to objectively evaluate how well a candidate’s resume matches a given job description.

Follow these rules strictly:
1. Evaluate ONLY based on the provided resume text and job description text.
2. Do NOT assume or invent any skills, experience, or projects.
3. Be unbiased, factual, and concise.
4. Output MUST be valid JSON only.
5. Do NOT add explanations outside JSON.
Compare the following RESUME and JOB DESCRIPTION.

RESUME TEXT:

{resume_text}


JOB DESCRIPTION TEXT:

{job_description_text}


EVALUATION INSTRUCTIONS:

1. Calculate an overall match score from 0 to 100.
2. Evaluate match based on:
   - Skills match
   - Experience relevance
   - Tools & technologies
   - Role responsibilities alignment
   - Domain fit (if applicable)

3. Identify key strengths where the resume strongly matches the JD.
4. Identify clear gaps or missing requirements.
5. Provide constructive feedback to improve the resume for this role.

OUTPUT FORMAT (STRICT JSON):

{{
  "match_score": number,
  "strengths": [
    "string",
    "string"
  ],
  "gaps": [
    "string",
    "string"
  ],
  "feedback": [
    "string",
    "string"
  ],
  "summary": "string"
}}

IMPORTANT:
- Do NOT include markdown
- Do NOT include additional text
- Do NOT include explanations outside JSON
- Ensure the JSON is valid and parsable


"""

def get_response(file_path, jd):
    llm = load_model()
    resume_data = PyPDFLoader(file_path)
    resume_data = resume_data.load()
    prompt = PromptTemplate(
        template=template,
        input_variables=['resume_text', 'job_description_text']
    )

    chain = prompt | llm | JsonOutputParser()

    return chain.invoke({
        'resume_text': resume_data,
        'job_description_text': jd
    })

    


