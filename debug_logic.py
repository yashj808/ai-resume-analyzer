from resume_checker import analyze_resume

resume_text = "Python developer with 5 years experience in machine learning and SQL"
job_desc = "Python, SQL, Machine Learning, Docker, AWS"

result = analyze_resume(resume_text, job_desc)

print(f"Resume Skills: {result['all_resume_skills']}")
print(f"Matched Skills: {result['skills']}")
print(f"Missing Skills: {result['missing']}")
print(f"Resume Score: {result['resume_score']}%")
print(f"Match Score: {result['match_score']}%")
print(f"Suggestions: {result['suggestions']}")
