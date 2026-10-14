# CareerReady AI

CareerReady AI is a beginner-friendly career preparation dashboard built with Python and Streamlit. It helps learners assess their preparation, review CV content, practise interviews, identify skill gaps, and build a career action plan.

## Features

- Career readiness self-assessment with explainable scoring
- Rule-based CV structure review and job-description keyword comparison
- Interview practice questions with transparent feedback
- Role-specific skills gap analysis
- Personal action plan with local progress tracking
- Career learning resources
- Responsible AI and privacy guidance
- Local JSON storage; no paid API key required

## Technology

- Python
- Streamlit
- Pandas
- Matplotlib
- Pytest

## Requirements

Install Python 3.10 or newer. Verify the installation:

```powershell
python --version
```

## Run on Windows

Open PowerShell or the VS Code terminal in the `careerready-ai` folder.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

If PowerShell blocks virtual-environment activation, you can use Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

Streamlit will print a local URL, usually `http://localhost:8501`. Open it in your browser.

## Run tests

```powershell
python -m pytest
```

## Project structure

```text
careerready-ai/
├── app.py
├── requirements.txt
├── README.md
├── DOCUMENTATION.md
├── .gitignore
├── modules/
│   ├── assessment.py
│   ├── cv_assistant.py
│   ├── interview_coach.py
│   ├── skills_analysis.py
│   ├── action_plan.py
│   └── storage.py
├── data/
│   ├── profile.json
│   ├── action_plan.json
│   ├── progress.json
│   └── career_resources.json
└── tests/
    ├── test_assessment.py
    ├── test_skills_analysis.py
    └── test_storage.py
```

## Privacy

The prototype saves profile and progress information to local JSON files under `data/`. Do not enter sensitive personal data. Anyone who can access the files on your computer may be able to read them. Use the app's delete option to clear the saved profile and progress.

## Limitations

- CV review and interview feedback use rules, not a large language model.
- The readiness score is a self-assessment, not a validated employment predictor.
- Skills libraries are examples and should be compared with current job descriptions.
- External resource availability, pricing, and course details can change.
- This is a local educational prototype, not a production service for multiple users.

## Publish to GitHub

1. Create a new empty repository on GitHub.
2. Ensure `.gitignore` is present.
3. In the project folder, run:

```powershell
git init
git add .
git commit -m "Build CareerReady AI prototype"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/careerready-ai.git
git push -u origin main
```

Replace the remote URL with your own repository URL. Do not commit personal data or secrets.

## Possible future improvements

- Optional LLM integration for richer feedback
- User authentication for hosted multi-user deployment
- Role-specific question bank expansion
- Export reports to PDF
- Add a small, evaluated ML component using a documented dataset
- Deploy to a Streamlit-compatible hosting service
