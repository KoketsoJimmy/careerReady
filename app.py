import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from modules.assessment import calculate_readiness
from modules.cv_assistant import review_cv, compare_cv_to_job
from modules.interview_coach import QUESTIONS, evaluate_answer
from modules.skills_analysis import ROLE_SKILLS, analyse_skills
from modules.action_plan import build_action_plan
from modules.storage import load_json, save_json, export_json_bytes

st.set_page_config(page_title="CareerReady AI", page_icon="🎯", layout="wide")

st.markdown("""
<style>
:root{--ink:#20242d;--muted:#68717d;--paper:#f7f6f2;--card:#ffffff;--line:#e8e6df;--mint:#dff4e9;--green:#28785d;--lilac:#eeebff;--purple:#6555b7;--peach:#fff0e6;--coral:#c96f48}
html,body,[class*="css"]{font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}
.stApp{background:var(--paper);color:var(--ink)}
.block-container{padding-top:2.2rem;padding-bottom:3rem;max-width:1240px}
[data-testid="stHeader"]{background:transparent}
[data-testid="stSidebar"]{background:#efeee8;border-right:1px solid var(--line)}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p{color:var(--muted)}
[data-testid="stSidebar"] [role="radiogroup"]{gap:7px}
[data-testid="stSidebar"] [role="radiogroup"] label{padding:9px 12px;border-radius:12px;transition:background .2s}
[data-testid="stSidebar"] [role="radiogroup"] label:hover{background:#fff}
h1,h2,h3,h4{font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif!important;color:var(--ink)!important;letter-spacing:-.045em!important}
h1{font-size:2.25rem!important;font-weight:800!important;margin-bottom:.35rem!important}
h2{font-size:1.45rem!important;font-weight:800!important}
h3{font-size:1.08rem!important;font-weight:700!important;letter-spacing:-.025em!important}
p{color:#555f6c;line-height:1.7}
.hero{position:relative;overflow:hidden;padding:2.2rem 2.3rem;border-radius:25px;background:#252b32;color:white;margin-bottom:1.7rem;box-shadow:0 18px 45px #22283112}
.hero:after{content:"";position:absolute;width:260px;height:260px;border-radius:50%;right:-55px;top:-105px;border:1px solid #ffffff2e;box-shadow:0 0 0 24px #ffffff08,0 0 0 52px #ffffff07,0 0 0 82px #ffffff06;pointer-events:none}
.hero .eyebrow{display:inline-flex;align-items:center;gap:8px;color:#a9e7ca;text-transform:uppercase;font-size:.72rem;letter-spacing:.16em;font-weight:800;margin-bottom:1rem}
.hero h1{font-size:clamp(2.15rem,4vw,3.2rem)!important;line-height:1.08!important;color:white!important;max-width:720px;margin:.1rem 0 .75rem!important}
.hero h1 span{color:#a9e7ca}
.hero p{color:#d6dbe0;max-width:680px;font-size:1.04rem;margin-bottom:1.15rem}
.hero .hero-note{display:inline-block;border:1px solid #ffffff30;border-radius:999px;padding:7px 12px;color:#f0f2f4;font-size:.8rem}
.section-label{font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;font-weight:800;color:var(--green);margin:1.2rem 0 .35rem}
.metric-card{background:var(--card);border:1px solid var(--line);padding:1.1rem 1.2rem;border-radius:18px;min-height:112px;box-shadow:0 5px 20px #252b3207}
div[data-testid="stMetric"]{background:white;border:1px solid var(--line);padding:1rem 1.1rem;border-radius:17px;box-shadow:0 5px 20px #252b3207;min-height:105px}
div[data-testid="stMetricLabel"]{color:var(--muted);font-size:.78rem;font-weight:700}
div[data-testid="stMetricValue"]{color:var(--ink);font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;font-weight:800;letter-spacing:-.05em}
.stButton>button,.stDownloadButton>button,button[kind="primary"],[data-testid="stFormSubmitButton"] button{border-radius:12px;border:1px solid #28785d;background:#28785d;color:white;font-weight:700;padding:.58rem 1rem;transition:all .18s;box-shadow:none}
.stButton>button:hover,.stDownloadButton>button:hover,[data-testid="stFormSubmitButton"] button:hover{background:#1f654e;border-color:#1f654e;transform:translateY(-1px);box-shadow:0 8px 20px #28785d20}
.stButton>button[kind="secondary"]{background:white;color:var(--ink);border-color:var(--line)}
input,textarea,[data-baseweb="select"]>div{border-radius:11px!important}
[data-testid="stTextInput"] input,[data-testid="stTextArea"] textarea{background:#fff;border-color:#e3e1da}
[data-testid="stProgressBar"]>div{background:#e8e6df;border-radius:99px}
[data-testid="stProgressBar"]>div>div{background:#52a981;border-radius:99px}
[data-testid="stAlert"]{border-radius:14px;border:1px solid var(--line)}
hr{border-color:var(--line)!important}
.feature-card{height:100%;background:white;border:1px solid var(--line);border-radius:18px;padding:1.2rem 1.25rem;min-height:154px;transition:transform .2s,box-shadow .2s}
.feature-card:hover{transform:translateY(-3px);box-shadow:0 14px 28px #20242d0b}
.feature-icon{display:inline-grid;place-items:center;width:38px;height:38px;border-radius:12px;background:var(--mint);color:var(--green);font-size:1.05rem;margin-bottom:.75rem}
.feature-card h3{margin:.1rem 0 .35rem!important}
.feature-card p{font-size:.88rem;margin:0;color:var(--muted)}
.tip-box{padding:1rem 1.15rem;background:#eeebff;border:1px solid #dfd9ff;border-radius:15px;color:#4c438e}
.small-note{color:var(--muted);font-size:.85rem}
[data-testid="stExpander"]{border:1px solid var(--line);border-radius:14px;background:white}
@media(max-width:700px){.block-container{padding-top:1.2rem}.hero{padding:1.5rem;border-radius:19px}.hero:after{right:-150px}.hero h1{font-size:2rem!important}}
</style>
""", unsafe_allow_html=True)

PROFILE_FILE = "data/profile.json"
PLAN_FILE = "data/action_plan.json"
PROGRESS_FILE = "data/progress.json"

if "profile" not in st.session_state:
    st.session_state.profile = load_json(PROFILE_FILE, {})
if "task_progress" not in st.session_state:
    st.session_state.task_progress = load_json(PROGRESS_FILE, {})
if "last_assessment" not in st.session_state:
    st.session_state.last_assessment = None

st.sidebar.markdown("<div style='font-family:Inter,system-ui,sans-serif;font-size:1.35rem;font-weight:800;letter-spacing:-.05em;color:#20242d;padding:.5rem 0 .1rem'>careerready<span style='color:#28785d'>.</span></div><div style='font-size:.78rem;color:#68717d;margin-bottom:1rem'>Your next chapter starts here.</div>", unsafe_allow_html=True)
pages = [
    "Career Dashboard", "Readiness Assessment", "CV Assistant",
    "Interview Practice", "Skills Gap Analysis", "Career Action Plan",
    "Resources & Responsible AI"
]
if "requested_page" in st.session_state:
    st.session_state["nav_page"] = st.session_state.pop("requested_page")
page = st.sidebar.radio("YOUR WORKSPACE", pages, key="nav_page")
st.sidebar.divider()
st.sidebar.caption("Prototype mode: data is stored locally on this computer.")

def persist_profile():
    save_json(PROFILE_FILE, st.session_state.profile)

def current_role():
    return st.session_state.profile.get("target_role", "Software Development")

if page == "Career Dashboard":
    display_name = st.session_state.profile.get("name", "there").strip() or "there"
    st.markdown(f'<div class="hero"><div class="eyebrow">✦ YOUR CAREER, YOUR MOMENTUM</div><h1>Small steps today.<br><span>Big moves tomorrow.</span></h1><p>Welcome back, {display_name}. Turn your ambition into a practical plan — build confidence, sharpen your story, and get ready for what comes next.</p><span class="hero-note">A little progress is still progress ✨</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Your starting point</div>', unsafe_allow_html=True)
    st.subheader("Shape your career profile")
    with st.form("profile_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Your name (optional)", value=st.session_state.profile.get("name", ""))
            education = st.text_input("Education / qualification", value=st.session_state.profile.get("education", ""))
        with col2:
            roles = list(ROLE_SKILLS.keys())
            target = st.selectbox("Target career path", roles, index=roles.index(current_role()) if current_role() in roles else 0)
            goal = st.text_input("Career goal (optional)", value=st.session_state.profile.get("goal", ""))
        submitted = st.form_submit_button("Save profile", type="primary")
        if submitted:
            st.session_state.profile.update({"name": name.strip(), "education": education.strip(), "target_role": target, "goal": goal.strip()})
            persist_profile()
            st.success("Profile saved locally.")
    st.divider()
    assessment = st.session_state.last_assessment
    skills_data = st.session_state.profile.get("skills", {})
    plan = load_json(PLAN_FILE, [])
    completed = sum(bool(v) for v in st.session_state.task_progress.values())
    total = len(plan)
    a, b, c, d = st.columns(4)
    a.metric("Readiness score", f"{assessment['score']}/100" if assessment else "—", help="Complete the self-assessment to get your starting score.")
    b.metric("Career direction", current_role())
    c.metric("Skills explored", len(skills_data))
    d.metric("Plan progress", f"{completed}/{total}" if total else "—")
    st.markdown('<div class="section-label">Your next move</div>', unsafe_allow_html=True)
    st.subheader("Keep your momentum going")
    if assessment:
        for item in assessment["actions"]:
            st.write(f"➡️ {item}")
    else:
        st.markdown('<div class="tip-box"><strong>Start where you are.</strong><br>Take the readiness check to discover your strengths and choose one practical next step. No pressure to have everything figured out.</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Your career toolkit</div>', unsafe_allow_html=True)
    st.subheader("Pick one thing to work on")
    f1, f2, f3 = st.columns(3)
    with f1:
        st.markdown('<div class="feature-card"><div class="feature-icon">✦</div><h3>Know your strengths</h3><p>Get a clear starting point and practical recommendations.</p></div>', unsafe_allow_html=True)
        if st.button("Check my readiness →", key="go_assessment", use_container_width=True): st.session_state["requested_page"] = "Readiness Assessment"; st.rerun()
    with f2:
        st.markdown('<div class="feature-card"><div class="feature-icon" style="background:#eeebff;color:#6555b7">✎</div><h3>Tell your story</h3><p>Make your CV clearer and practise interview answers.</p></div>', unsafe_allow_html=True)
        if st.button("Improve my CV →", key="go_cv", use_container_width=True): st.session_state["requested_page"] = "CV Assistant"; st.rerun()
    with f3:
        st.markdown('<div class="feature-card"><div class="feature-icon" style="background:#fff0e6;color:#c96f48">↗</div><h3>Build momentum</h3><p>Turn your goals into manageable actions and learning steps.</p></div>', unsafe_allow_html=True)
        if st.button("Make my action plan →", key="go_plan", use_container_width=True): st.session_state["requested_page"] = "Career Action Plan"; st.rerun()
    st.caption("CareerReady AI is a learning aid. Scores and suggestions are not hiring predictions or a substitute for professional career advice.")

elif page == "Readiness Assessment":
    st.title("Career Readiness Assessment")
    st.write("Answer honestly. Your result is a self-assessment to help you choose practical next steps.")
    categories = {
        "CV and applications": ["I have an up-to-date CV.", "I tailor my CV to each role.", "I can explain my projects or experience clearly."],
        "Interview preparation": ["I have practised common interview questions.", "I can explain my strengths and areas to improve.", "I can use the STAR method for examples."],
        "Technical preparation": ["I understand the fundamentals for my target role.", "I have completed or documented a practical project.", "I can explain the tools and technologies I have used."],
        "Professional readiness": ["My professional profile is reasonably up to date.", "I can describe the role I am targeting.", "I have a plan for continued learning and applications."]
    }
    with st.form("assessment_form"):
        answers = {}
        for category, questions in categories.items():
            st.subheader(category)
            for q in questions:
                answers[q] = st.radio(q, ["Not yet", "Partly", "Yes"], horizontal=True, key=f"assess_{q}")
        done = st.form_submit_button("Calculate my readiness", type="primary")
    if done:
        result = calculate_readiness(answers)
        st.session_state.last_assessment = result
        st.session_state.profile["assessment_answers"] = answers
        st.session_state.profile["last_assessment"] = result
        persist_profile()
        st.success("Assessment complete.")
        st.metric("Career readiness score", f"{result['score']}/100")
        st.progress(result["score"] / 100)
        st.write(result["summary"])
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Strengths")
            for x in result["strengths"]:
                st.write(f"✅ {x}")
        with c2:
            st.subheader("Areas to work on")
            for x in result["improvements"]:
                st.write(f"🛠️ {x}")
        st.subheader("Suggested next actions")
        for x in result["actions"]:
            st.write(f"• {x}")
        st.caption("This score is calculated from your answers using a transparent rubric. It is not a validated hiring prediction.")

elif page == "CV Assistant":
    st.title("CV Improvement Assistant")
    st.write("Paste CV text and, optionally, a job description. Your text stays in this local application in the basic version.")
    cv_text = st.text_area("Paste your CV content", height=250, placeholder="Professional summary, skills, experience, education, projects...")
    job_text = st.text_area("Paste a target job description (optional)", height=180, placeholder="Role responsibilities and requirements...")
    if st.button("Review my CV", type="primary"):
        if not cv_text.strip():
            st.warning("Please paste some CV content first.")
        else:
            result = review_cv(cv_text)
            st.subheader("CV review")
            st.metric("Basic structure score", f"{result['score']}/100")
            for section in result["present_sections"]:
                st.write(f"✅ Found: {section}")
            for issue in result["suggestions"]:
                st.write(f"🛠️ {issue}")
            st.subheader("Action-oriented bullet examples")
            for before, after in result["examples"]:
                st.markdown(f"**Original idea:** {before}\n\n**Possible rewrite:** {after}")
            if job_text.strip():
                comparison = compare_cv_to_job(cv_text, job_text)
                st.subheader("Job description keyword comparison")
                st.write(f"Matched terms: {', '.join(comparison['matched']) or 'No clear matches found'}")
                st.write(f"Terms to consider if they truthfully match your experience: {', '.join(comparison['missing']) or 'No obvious missing terms from the basic keyword list'}")
                st.caption("Keyword matching is approximate. Do not add skills or experience you do not have.")
            st.download_button("Download review as text", result["report"], file_name="cv_review.txt", mime="text/plain")

elif page == "Interview Practice":
    st.title("Interview Practice Coach")
    roles = list(QUESTIONS.keys())
    role = st.selectbox("Choose an interview area", roles)
    types = ["Behavioural", "Technical", "General"]
    qtype = st.selectbox("Interview type", types)
    questions = QUESTIONS[role].get(qtype, QUESTIONS[role]["General"])
    question = st.selectbox("Choose a question", questions)
    st.info(question)
    answer = st.text_area("Your answer", height=200, placeholder="Write your answer here...")
    if st.button("Review my answer", type="primary"):
        if len(answer.strip()) < 15:
            st.warning("Add a little more detail so the coach can give useful feedback.")
        else:
            feedback = evaluate_answer(question, answer, qtype)
            st.subheader("Feedback")
            st.metric("Answer structure indicator", f"{feedback['score']}/100")
            for item in feedback["strengths"]:
                st.write(f"✅ {item}")
            for item in feedback["improvements"]:
                st.write(f"🛠️ {item}")
            if qtype == "Behavioural":
                st.markdown("**Try the STAR structure:** Situation → Task → Action → Result.")
            st.markdown("**Suggested answer structure:**")
            st.write(feedback["structure"])
            st.caption("This is rule-based practice feedback, not a definitive assessment of your ability or a hiring decision.")

elif page == "Skills Gap Analysis":
    st.title("Skills Gap Analysis")
    role = st.selectbox("Target role", list(ROLE_SKILLS.keys()), index=list(ROLE_SKILLS.keys()).index(current_role()) if current_role() in ROLE_SKILLS else 0)
    st.write("Rate your current confidence in each skill. You can use the results to prioritise learning.")
    options = ["Not started", "Beginner", "Intermediate", "Confident"]
    saved = st.session_state.profile.get("skills", {})
    with st.form("skills_form"):
        ratings = {}
        for skill in ROLE_SKILLS[role]:
            ratings[skill] = st.select_slider(skill, options=options, value=saved.get(skill, "Not started"), key=f"skill_{role}_{skill}")
        submit_skills = st.form_submit_button("Analyse my skills", type="primary")
    if submit_skills:
        result = analyse_skills(role, ratings)
        st.session_state.profile["skills"] = ratings
        st.session_state.profile["target_role"] = role
        persist_profile()
        st.subheader("Your skill profile")
        st.metric("Skills rated", len(ratings))
        st.write(f"**Current strengths:** {', '.join(result['strengths']) or 'Keep practising and rating your skills honestly.'}")
        st.write("**Priority areas:**")
        for item in result["gaps"]:
            st.write(f"• {item}")
        df = pd.DataFrame({"Skill": list(ratings.keys()), "Level": [options.index(v) for v in ratings.values()]})
        st.bar_chart(df.set_index("Skill"))
        st.info("Tip: choose one priority skill at a time and practise it through a small project or exercise.")

elif page == "Career Action Plan":
    st.title("Personal Career Action Plan")
    role = st.selectbox("Target role for this plan", list(ROLE_SKILLS.keys()), index=list(ROLE_SKILLS.keys()).index(current_role()) if current_role() in ROLE_SKILLS else 0)
    weeks = st.selectbox("Plan length", [2, 4, 6], index=1)
    if st.button("Generate action plan", type="primary"):
        assessment = st.session_state.last_assessment or st.session_state.profile.get("last_assessment")
        skills = st.session_state.profile.get("skills", {})
        plan = build_action_plan(role, weeks, assessment, skills)
        save_json(PLAN_FILE, plan)
        st.session_state.task_progress = {str(i): False for i in range(len(plan))}
        save_json(PROGRESS_FILE, st.session_state.task_progress)
        st.success("Your plan has been created and saved locally.")
    plan = load_json(PLAN_FILE, [])
    if plan:
        completed = 0
        for i, task in enumerate(plan):
            key = str(i)
            checked = st.checkbox(f"**Week {task['week']} — {task['title']}**\n\n{task['description']}", value=bool(st.session_state.task_progress.get(key, False)), key=f"plan_{key}")
            st.session_state.task_progress[key] = checked
            completed += int(checked)
        save_json(PROGRESS_FILE, st.session_state.task_progress)
        st.progress(completed / len(plan) if plan else 0)
        st.write(f"**Progress:** {completed} of {len(plan)} tasks completed")
        st.download_button("Export action plan (JSON)", export_json_bytes(plan), file_name="career_action_plan.json", mime="application/json")
    else:
        st.info("Generate a plan to get a structured set of career preparation tasks.")
    st.caption("Plans are suggestions. Adapt them to your schedule, access to resources, and actual job requirements.")

elif page == "Resources & Responsible AI":
    st.title("Resources & Responsible AI")
    st.subheader("Free learning and career resources")
    resources = load_json("data/career_resources.json", [])
    for item in resources:
        st.markdown(f"**[{item['title']}]({item['url']})** — {item['category']}")
        st.write(item["description"])
    st.divider()
    st.subheader("Responsible AI and limitations")
    st.markdown("""
- Career readiness scores are based on self-reported answers and are not validated predictions of hiring success.
- CV and interview feedback uses simple rules and may miss context, nuance, or technical correctness.
- Skills recommendations are general examples. Always compare them with current job descriptions and official documentation.
- The app does not make hiring decisions and should not be used to rank or exclude candidates.
- Do not enter passwords, identity numbers, bank details, or other unnecessary sensitive information.
- In this prototype, data is stored locally in files on the computer running the app. Anyone with access to those files may be able to read them.
- Verify external learning links and course availability before relying on them.
""")
    st.subheader("Delete locally stored profile data")
    if st.button("Delete my local profile and progress", type="secondary"):
        st.session_state.profile = {}
        st.session_state.task_progress = {}
        st.session_state.last_assessment = None
        save_json(PROFILE_FILE, {})
        save_json(PROGRESS_FILE, {})
        save_json(PLAN_FILE, [])
        st.success("Local profile and progress files have been cleared.")

st.sidebar.divider()
st.sidebar.caption("Built with Python + Streamlit • Educational prototype")
