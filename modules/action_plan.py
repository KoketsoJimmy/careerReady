def build_action_plan(role, weeks=4, assessment=None, skills=None):
    tasks = [
        ("Audit your target role", f"Find two current job descriptions for {role}. Note repeated responsibilities and skills."),
        ("Update your CV", "Review your summary, skills, education, projects, and experience. Keep every claim accurate."),
        ("Practise interview answers", "Practise three questions aloud. Use STAR for behavioural examples."),
        ("Build evidence", "Complete or improve a small role-relevant project and document what you contributed."),
        ("Strengthen a priority skill", "Choose one skill gap and complete a practical exercise with notes or screenshots."),
        ("Improve your professional profile", "Review your LinkedIn headline and About section. Add evidence of genuine projects."),
        ("Practise explaining your work", "Prepare a two-minute explanation of a project, including the problem, approach, and lesson."),
        ("Prepare applications", "Tailor your CV to one suitable opportunity and check all details before submitting."),
        ("Review progress", "Reflect on what improved, identify the next gap, and set a realistic weekly learning target.")
    ]
    count = max(4, min(weeks * 2, len(tasks)))
    selected = tasks[:count]
    plan = []
    for i, (title, description) in enumerate(selected):
        week = min(weeks, (i // max(1, (count + weeks - 1) // weeks)) + 1)
        if i == 0 and assessment and assessment.get("score", 100) < 50:
            description += " Start small and prioritise consistency over perfection."
        if i == 4 and skills:
            gaps = [k for k, v in skills.items() if v in ("Not started", "Beginner")]
            if gaps:
                description = f"Focus on one priority from your self-rated gaps, such as {gaps[0]}. " + description
        plan.append({"week": week, "title": title, "description": description})
    return plan
