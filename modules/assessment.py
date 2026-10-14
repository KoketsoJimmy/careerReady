def calculate_readiness(answers):
    """Calculate a transparent self-assessment score from Not yet/Partly/Yes answers."""
    points = {"Not yet": 0, "Partly": 1, "Yes": 2}
    total = len(answers)
    earned = sum(points.get(value, 0) for value in answers.values())
    score = round((earned / (total * 2)) * 100) if total else 0
    strengths = [q for q, v in answers.items() if v == "Yes"]
    improvements = [q for q, v in answers.items() if v != "Yes"]
    actions = []
    if any("CV" in q or "profile" in q.lower() for q in improvements):
        actions.append("Review your CV and professional profile, then tailor them to one target role.")
    if any("interview" in q.lower() or "STAR" in q for q in improvements):
        actions.append("Practise two interview questions and structure behavioural answers with STAR.")
    if any("technical" in q.lower() or "project" in q.lower() or "tools" in q.lower() for q in improvements):
        actions.append("Choose one role-relevant skill and demonstrate it in a small documented project.")
    if not actions:
        actions = ["Review a current job description and identify one specific area to strengthen.", "Practise explaining a project or achievement out loud.", "Set a weekly learning and application target."]
    if score >= 80:
        summary = "Your answers suggest a solid preparation foundation. Focus on evidence, practice, and tailoring applications."
    elif score >= 50:
        summary = "You have a foundation to build on. Focus on the improvement areas below and take them one at a time."
    else:
        summary = "Start with a few manageable steps. Improving your CV, practising answers, and building evidence can help you progress."
    return {"score": score, "strengths": strengths[:5], "improvements": improvements[:6], "actions": actions[:3], "summary": summary}
