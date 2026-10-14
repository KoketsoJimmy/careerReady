ROLE_SKILLS = {
    "Software Development": [
        "Programming fundamentals", "Object-oriented programming", "SQL and databases",
        "Git and GitHub", "Debugging and testing", "APIs and web fundamentals",
        "Documentation", "Communication and teamwork"
    ],
    "IT Support": [
        "Windows operating systems", "Hardware troubleshooting", "Networking fundamentals",
        "IP addressing", "DNS and DHCP", "User account management",
        "Ticket documentation", "Customer service"
    ],
    "Data Analysis": [
        "Excel or spreadsheets", "SQL", "Python basics", "Data cleaning",
        "Charts and visualisation", "Statistics fundamentals", "Data storytelling",
        "Documentation and communication"
    ],
    "Cloud Computing": [
        "Cloud fundamentals", "Networking", "Linux basics", "Identity and access management",
        "Compute and storage", "Security fundamentals", "Monitoring", "Automation basics"
    ],
    "Cybersecurity": [
        "Networking fundamentals", "Operating system basics", "Security principles",
        "Multi-factor authentication", "Access control", "Log analysis",
        "Incident reporting", "Security awareness"
    ],
    "AI and Machine Learning": [
        "Python fundamentals", "Data preparation", "Statistics basics", "Machine learning concepts",
        "Model evaluation", "Responsible AI", "Data visualisation", "Experiment documentation"
    ],
    "Network Support": [
        "TCP/IP fundamentals", "IP addressing and subnetting", "DNS and DHCP",
        "Routers and switches", "Wi-Fi troubleshooting", "Network security basics",
        "Monitoring tools", "Technical documentation"
    ],
    "General Graduate Opportunities": [
        "Communication", "Teamwork", "Time management", "Problem solving",
        "Professional writing", "Digital literacy", "Interview preparation", "Learning agility"
    ]
}
LEVELS = {"Not started": 0, "Beginner": 1, "Intermediate": 2, "Confident": 3}

def analyse_skills(role, ratings):
    strengths = [skill for skill, level in ratings.items() if LEVELS.get(level, 0) >= 2]
    gaps = [skill for skill, level in ratings.items() if LEVELS.get(level, 0) < 2]
    return {"role": role, "strengths": strengths, "gaps": gaps}
