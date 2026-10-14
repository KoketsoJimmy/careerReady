QUESTIONS = {
    "Software Development": {
        "Behavioural": [
            "Tell me about a time you solved a difficult problem.",
            "Describe a project you worked on and what you contributed.",
            "Tell me about a time you had to learn something quickly."
        ],
        "Technical": [
            "Explain the difference between a variable and a function.",
            "What is the purpose of testing and debugging?",
            "What is a database, and when might you use SQL?"
        ],
        "General": ["Tell me about yourself.", "Why are you interested in this role?", "What are your strengths and one area you are improving?"]
    },
    "IT Support": {
        "Behavioural": [
            "Tell me about a time you helped someone solve a problem.",
            "How do you respond when several people need support at once?",
            "Describe how you handle feedback."
        ],
        "Technical": [
            "How would you troubleshoot a computer that cannot connect to Wi-Fi?",
            "What are DNS and DHCP used for?",
            "What steps would you take if a user could not log in?"
        ],
        "General": ["Tell me about yourself.", "Why do you want to work in IT support?", "How would you explain a technical issue to a non-technical user?"]
    },
    "Data Analysis": {
        "Behavioural": [
            "Tell me about a time you used information to make a decision.",
            "Describe how you checked your work for errors.",
            "Tell me about a time you explained something complex."
        ],
        "Technical": [
            "What is the difference between a row and a column in a table?",
            "When would you use a SQL JOIN?",
            "How would you handle missing values in a dataset?"
        ],
        "General": ["Tell me about yourself.", "Why are you interested in data analysis?", "How do you keep learning new tools?"]
    },
    "Cloud Computing": {
        "Behavioural": [
            "Tell me about a time you learned a new technical concept.",
            "Describe a problem you broke into smaller steps.",
            "How do you manage competing priorities?"
        ],
        "Technical": [
            "What is cloud computing?",
            "Explain the difference between compute, storage, and networking.",
            "Why is identity and access management important?"
        ],
        "General": ["Tell me about yourself.", "Why are you interested in cloud computing?", "How would you approach a technology you have never used?"]
    },
    "Cybersecurity": {
        "Behavioural": [
            "Tell me about a time you noticed a risk or mistake.",
            "How would you handle an unfamiliar security issue?",
            "Describe how you would communicate a concern responsibly."
        ],
        "Technical": [
            "What is multi-factor authentication?",
            "What is the principle of least privilege?",
            "How would you respond to a suspicious email?"
        ],
        "General": ["Tell me about yourself.", "Why are you interested in cybersecurity?", "How do you stay aware of security best practices?"]
    }
}

def evaluate_answer(question, answer, qtype):
    text = answer.strip()
    words = text.split()
    lower = text.lower()
    score = min(100, round(min(len(words) / 100, 1) * 35 + min(sum(1 for k in ["because", "for example", "first", "then", "result", "learned", "I"] if k.lower() in lower) * 8, 40) + (25 if len(words) >= 35 else 10)))
    strengths, improvements = [], []
    if len(words) >= 35:
        strengths.append("You provided enough detail for a practice response.")
    else:
        improvements.append("Add more detail: explain the context, what you did, and the outcome.")
    if any(x in lower for x in ["I ", "my ", "we "]):
        strengths.append("You refer to your own actions or experience.")
    else:
        improvements.append("Use a specific example and make your personal contribution clear.")
    if any(x in lower for x in ["result", "learned", "improved", "resolved", "completed", "because"]):
        strengths.append("You include some reasoning, learning, or outcome language.")
    else:
        improvements.append("Explain the result or what you learned from the situation.")
    if qtype == "Behavioural":
        structure = "Situation: briefly set the scene. Task: explain your responsibility. Action: describe what you did. Result: share the outcome and lesson."
    elif qtype == "Technical":
        structure = "Define the concept, explain how it works, give a practical example, and mention any important limitation or troubleshooting step."
    else:
        structure = "Give a direct opening answer, support it with a relevant example, connect it to the role, and finish with what you want to contribute or learn."
    if not improvements:
        improvements.append("Practise delivering the answer aloud and keep it focused on the question.")
    return {"score": score, "strengths": strengths, "improvements": improvements, "structure": structure}
