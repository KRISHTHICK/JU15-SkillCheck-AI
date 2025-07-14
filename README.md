# JU15-SkillCheck-AI
GEN AI

📘 README.md
markdown
Copy
Edit
# 🧠 SkillCheck AI – Resume vs Job Fit Analyzer

SkillCheck AI compares your resume to a job description, scores how well you match, and suggests improvements.

---

## ✅ Features

- 📤 Upload Resume (PDF, DOCX, TXT)
- 📋 Paste Job Description
- ✅ Shows matched & missing skills
- 📊 Fit score out of 100
- 🤖 AI-powered resume suggestions using LLaMA3 (Ollama)

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/yourusername/skillcheck-ai.git
cd skillcheck-ai
pip install -r requirements.txt
ollama pull llama3
streamlit run app.py
🧪 Sample Output
Fit Score: 72/100

Matched Skills: ['python', 'data', 'ml', 'pandas']

Missing Skills: ['docker', 'api', 'airflow']

Suggestions:

Emphasize Docker & APIs

Mention workflow orchestration (e.g., Airflow)

🔮 Future Add-ons
PDF report download

Multi-resume batch scoring

Auto skill extractor from resumes

JD parsing from job URLs

yaml
Copy
Edit

---

Would you like to:
- ➕ Add resume feedback as downloadable PDF?
- 📤 Auto-generate improved resume sections?
- 💡 Connect to LinkedIn for JD scraping?

Let me know — happy to enhance it further!

🧠 SkillCheck AI – Smart Resume Analyzer & Job Fit Scorer
🎯 What It Does
SkillCheck AI analyzes a candidate's resume (PDF, DOCX, TXT) against a specific job description and gives:

✅ Matched skills

❌ Missing skills

📊 Job fit score (out of 100)

🧠 Suggestions to improve the resume

💬 AI explanation (why it matched or didn't)

🔍 Use Case
Perfect for:

Job seekers improving their resumes

Recruiters screening candidates quickly

Career advisors or job platforms enhancing their tools

✅ Features
Feature	Description
📁 Upload Resume	PDF, DOCX, or TXT
📝 Paste Job Description	or choose from sample roles
📊 Fit Score	Based on skill & keyword overlap
✅ Matched Skills	Skills found in both resume & job
❌ Missing Skills	Critical skills in JD but not in resume
🤖 AI Suggestions	Simple resume improvement tips

🧠 Tech Stack
Layer	Tool
UI	Streamlit
AI Agent	Ollama (LLaMA3)
Parsing	PyMuPDF, docx2txt
Scoring	Python keyword match + AI feedback

