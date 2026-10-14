from modules.assessment import calculate_readiness

def test_all_yes_gives_100():
    result = calculate_readiness({"q1": "Yes", "q2": "Yes"})
    assert result["score"] == 100

def test_all_not_yet_gives_zero():
    result = calculate_readiness({"q1": "Not yet", "q2": "Not yet"})
    assert result["score"] == 0

def test_partly_gives_half():
    result = calculate_readiness({"q1": "Partly"})
    assert result["score"] == 50
