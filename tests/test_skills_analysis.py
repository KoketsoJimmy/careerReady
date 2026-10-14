from modules.skills_analysis import analyse_skills

def test_skill_gaps_and_strengths():
    result = analyse_skills("Software Development", {
        "Python": "Confident", "SQL": "Beginner", "Git": "Intermediate"
    })
    assert "Python" in result["strengths"]
    assert "Git" in result["strengths"]
    assert "SQL" in result["gaps"]
