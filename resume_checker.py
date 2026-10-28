import re
import traceback

SKILLS_DB = [
    # Programming Languages
    "python", "javascript", "typescript", "java", "c++", "c#", "c", "go", "rust",
    "ruby", "php", "swift", "kotlin", "scala", "r", "dart",
    
    # Web & Frameworks
    "html", "css", "react", "angular", "vue", "node.js", "express", "django",
    "flask", "fastapi", "spring boot", "next.js", "tailwind", "bootstrap",
    
    # Databases & Storage
    "sql", "nosql", "postgresql", "mysql", "mongodb", "redis", "sqlite",
    "oracle", "cassandra", "dynamodb",
    
    # Data Science & Machine Learning
    "machine learning", "deep learning", "artificial intelligence", "nlp",
    "computer vision", "pandas", "numpy", "scikit-learn", "tensorflow",
    "pytorch", "keras", "data analysis",
    
    # Cloud, DevOps & Tools
    "aws", "azure", "gcp", "docker", "kubernetes", "git", "github",
    "gitlab", "ci/cd", "jenkins", "linux", "terraform", "rest api", "graphql"
]

def extract_skills(text, skills_list):
    if not text:
        return []
    text_padded = f" {text.lower()} "
    found = []
    for skill in skills_list:
        pattern = r'(?<![a-zA-Z0-9_#+])' + re.escape(skill.lower()) + r'(?![a-zA-Z0-9_#+])'
        if re.search(pattern, text_padded):
            found.append(skill)
    return sorted(list(set(found)))

def analyze_resume(resume_text, job_desc):
    try:
        return _analyze_logic(resume_text, job_desc)
    except Exception as e:
        error_msg = f"Error in analyze_resume: {str(e)}\n{traceback.format_exc()}"
        with open("api_debug.log", "a") as f:
            f.write(f"\n--- LOGIC ERROR ---\n{error_msg}\n")
        return {
            "resume_score": 0,
            "match_score": 0,
            "skills": [],
            "all_resume_skills": [],
            "missing": [],
            "suggestions": [f"Error during analysis: {str(e)}"],
            "radar_labels": ["Technical Skills", "Tools", "Problem Solving", "Architecture", "Testing"],
            "radar_values": [30, 30, 30, 30, 30]
        }

def _analyze_logic(resume_text, job_desc):
    resume_skills = extract_skills(resume_text, SKILLS_DB)
    job_skills = extract_skills(job_desc, SKILLS_DB)

    matched = [skill for skill in job_skills if skill in resume_skills]
    missing = [skill for skill in job_skills if skill not in resume_skills]

    # Calculate match score
    if job_skills:
        match_score = int((len(matched) / len(job_skills)) * 100)
    else:
        match_score = 100 if resume_skills else 0

    # Calculate overall resume strength score
    if resume_skills:
        skill_breadth_score = min(len(resume_skills) * 10, 60)
        match_component = int(match_score * 0.4)
        resume_score = min(skill_breadth_score + match_component, 100)
    else:
        resume_score = 0

    # Actionable suggestions
    suggestions = []
    for m in missing[:4]:
        suggestions.append(f"Consider adding '{m.title()}' to your skills or project descriptions.")

    if len(resume_skills) < 3:
        suggestions.append("Add more technical skills and tools to demonstrate your breadth of expertise.")

    suggestions.append("Use quantifiable metrics in bullet points (e.g., 'improved performance by 30%').")
    suggestions.append("Keep standard section headers (Experience, Skills, Education) for optimal ATS readability.")

    # Radar chart skills (dynamically derived from analysis)
    combined = matched[:4] + missing[:3]
    if len(combined) < 5:
        fallbacks = ["git", "linux", "sql", "python", "docker"]
        for fb in fallbacks:
            if fb not in combined:
                combined.append(fb)
            if len(combined) >= 5:
                break

    radar_labels = [s.title() for s in combined]
    radar_values = [85 if s in resume_skills else 30 for s in combined]

    return {
        "resume_score": resume_score,
        "match_score": match_score,
        "skills": matched,
        "all_resume_skills": resume_skills,
        "missing": missing,
        "suggestions": suggestions,
        "radar_labels": radar_labels,
        "radar_values": radar_values
    }
