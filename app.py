# app.py – SkillCheck AI: Resume Analyzer & Job Fit Scorer

import streamlit as st
import fitz  # PyMuPDF
import docx2txt
import ollama
import re

# --- Extract text from resume file ---
def extract_resume_text(file):
    if file.name.endswith(".pdf"):
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            return "\n".join(page.get_text() for page in doc)
    elif file.name.endswith(".docx"):
        return docx2txt.process(file)
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    return ""

# --- Simple skill extractor (from JD) ---
def extract_skills_from_jd(jd_text):
    lines = jd_text.lower().split("\n")
    keywords = set()
    for line in lines:
        words = re.findall(r"\b[a-zA-Z]{3,}\b", line)
        keywords.update(word.strip() for word in words if word not in {"and", "with", "for", "the", "you", "are", "our"})
    return sorted(list(keywords))

# --- Match skills ---
def score_resume_against_jd(resume_text, jd_skills):
    resume_text_lower = resume_text.lower()
    matched = [skill for skill in jd_skills if skill in resume_text_lower]
    missing = [skill for skill in jd_skills if skill not in resume_text_lower]
    score = int((len(matched) / len(jd_skills)) * 100) if jd_skills else 0
    return matched, missing, score

# --- AI Suggestions ---
def get_ai_feedback(resume_text, jd_text, matched, missing):
    prompt = f"""
You are a resume improvement assistant.

Given the following:
Resume Text: {resume_text[:1500]}
Job Description: {jd_text[:1500]}
Matched Skills: {matched}
Missing Skills: {missing}

Suggest 3 to 5 tips to improve the resume for this job.
"""
    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# --- Streamlit UI ---
st.set_page_config(page_title="SkillCheck AI", layout="centered")
st.title("🧠 SkillCheck AI – Resume vs Job Fit Analyzer")

col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader("📄 Upload Resume (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])

with col2:
    jd_text = st.text_area("📝 Paste Job Description", height=300, placeholder="Paste job description here...")

if resume_file and jd_text:
    with st.spinner("Analyzing your resume against the job description..."):
        resume_text = extract_resume_text(resume_file)
        jd_skills = extract_skills_from_jd(jd_text)
        matched, missing, score = score_resume_against_jd(resume_text, jd_skills)
        ai_feedback = get_ai_feedback(resume_text, jd_text, matched, missing)

    st.markdown(f"### 📊 Fit Score: `{score}/100`")

    st.markdown("---")
    st.markdown("#### ✅ Matched Skills")
    st.write(matched)

    st.markdown("#### ❌ Missing Skills")
    st.write(missing)

    st.markdown("---")
    st.markdown("### 🤖 AI Suggestions to Improve Resume")
    st.markdown(ai_feedback)
else:
    st.info("Upload a resume and paste a job description to begin analysis.")
