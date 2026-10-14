import re

SECTION_TERMS = {
    "Contact information": ["email", "phone", "linkedin", "address"],
    "Professional summary": ["professional summary", "profile", "objective", "about me"],
    "Skills": ["skills", "technical skills", "core competencies"],
    "Work experience": ["experience", "employment", "work history"],
    "Education": ["education", "qualification", "diploma", "degree"],
    "Projects": ["projects", "portfolio", "github"],
}
KEYWORDS = [
    "python", "java", "sql", "javascript", "html", "css", "git", "github",
    "communication", "teamwork", "problem solving", "troubleshooting",
    "customer service", "data analysis", "testing", "documentation",
    "cloud", "networking", "database", "project management", "excel"
]

def review_cv(cv_text):
    lower = cv_text.lower()
    present = [section for section, terms in SECTION_TERMS.items() if any(term in lower for term in terms)]
    suggestions = []
    missing = [s for s in SECTION_TERMS if s not in present]
    if missing:
        suggestions.append("Consider adding or clearly labelling these sections if relevant: " + ", ".join(missing) + ".")
    if len(cv_text.split()) < 100:
        suggestions.append("Your CV text is quite short. Check whether it fully explains your skills, education, projects, and experience.")
    if not re.search(r"\b(developed|created|built|managed|supported|improved|analysed|analyzed|coordinated|tested|resolved|implemented)\b", lower):
        suggestions.append("Use action verbs to explain what you did, rather than listing duties only.")
    if not re.search(r"\b(\d+|%|percent|hours|users|projects|customers)\b", lower):
        suggestions.append("Where truthful, add specific scale or outcomes (for example, number of users, projects, or tasks completed).")
    if not any(x in lower for x in ["github", "portfolio", "project"]):
        suggestions.append("If you have practical work, consider including a project or portfolio section with evidence.")
    score = min(100, round((len(present) / len(SECTION_TERMS)) * 70 + min(len(cv_text.split()) / 300, 1) * 15 + (15 if "action verb" not in " ".join(suggestions).lower() else 0)))
    examples = [
        ("Responsible for a student portal.", "Developed a student portal feature to organise student records and support attendance tracking. (Use only if this accurately reflects your contribution.)"),
        ("Worked with a team on tasks.", "Collaborated with team members to coordinate tasks, communicate progress, and support timely delivery. (Adapt to your real experience.)")
    ]
    report = "CV REVIEW\n\n" + f"Basic structure score: {score}/100\n\nSections identified:\n" + "\n".join(f"- {x}" for x in present) + "\n\nSuggestions:\n" + "\n".join(f"- {x}" for x in suggestions)
    return {"score": score, "present_sections": present, "suggestions": suggestions, "examples": examples, "report": report}

def compare_cv_to_job(cv_text, job_text):
    cv = cv_text.lower()
    job = job_text.lower()
    terms = [k for k in KEYWORDS if k in job]
    matched = [k for k in terms if k in cv]
    missing = [k for k in terms if k not in cv]
    return {"matched": matched, "missing": missing}
