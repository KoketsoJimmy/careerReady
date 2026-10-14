# CareerReady AI — Technical Documentation

## 1. Purpose

CareerReady AI supports career preparation by combining a self-assessment, CV checklist, interview practice, role-specific skills analysis, and action planning in one interface.

## 2. Architecture

The application uses Streamlit for the interface. Business logic is separated into Python modules under `modules/`. JSON files in `data/` provide local persistence and editable resource content.

```text
User
 |
 v
Streamlit interface (app.py)
 |-- Readiness assessment --> modules/assessment.py
 |-- CV review ------------> modules/cv_assistant.py
 |-- Interview practice ---> modules/interview_coach.py
 |-- Skills analysis ------> modules/skills_analysis.py
 |-- Action plan ----------> modules/action_plan.py
 `-- Local persistence ----> modules/storage.py --> data/*.json
```

## 3. Scoring and recommendation logic

### Readiness assessment
Each answer receives 0 points for “Not yet”, 1 for “Partly”, and 2 for “Yes”. The score is the total points divided by the maximum possible points, multiplied by 100. Recommendations are based on areas where the user selected something other than “Yes”.

### CV review
The application searches for common CV section labels and basic evidence such as action verbs, project references, and measurable details. The score is a heuristic checklist score; it is not an assessment of a candidate's true employability.

### Interview practice
Feedback checks answer length and whether the response contains examples, actions, reasoning, results, or learning language. It cannot reliably assess all technical correctness, tone, body language, or context.

### Skills gap analysis
Each self-rated level is mapped to an ordinal value: Not started = 0, Beginner = 1, Intermediate = 2, Confident = 3. Skills rated Beginner or Not started are listed as gaps; Intermediate and Confident are listed as strengths.

### Career action plan
A role-neutral sequence of practical activities is generated and labelled by week. Users should customise it based on their schedule and current opportunities.

## 4. Data and privacy

The application stores profile information, skill ratings, action plans, and task progress in local JSON files. It does not provide authentication or encryption. It is intended for one local user on a trusted computer. Do not use it to store sensitive personal information or deploy it as a multi-user service without additional controls.

## 5. Responsible AI

- Scores are indicators for reflection, not hiring predictions.
- Rule-based feedback can be incomplete and may misinterpret context.
- Skill lists are examples, not universal job requirements.
- Users should verify suggestions and avoid inventing CV claims.
- The system must not be used to make automated hiring decisions.

## 6. Testing

Automated tests cover assessment score calculations, skills classification, and JSON persistence. Run `python -m pytest` from the project root.

## 7. Next steps

For a stronger portfolio submission, add screenshots, document one prompt-iteration or rule-improvement case study, demonstrate a test run, and record a short walkthrough video. If adding machine learning, select a suitable public dataset, establish a baseline, evaluate it with appropriate metrics, and document limitations instead of adding ML only for appearance.
