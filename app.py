import streamlit as st
import pandas as pd
from datetime import date

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

st.set_page_config(
    page_title="FacultyFlow",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# SESSION STORAGE
# -----------------------------

if "projects" not in st.session_state:
    st.session_state.projects = []

if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "forms" not in st.session_state:
    st.session_state.forms = []

if "courses" not in st.session_state:
    st.session_state.courses = []


# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

.main {
    background-color: #f7f8fc;
}

.title {
    font-size: 38px;
    font-weight: 700;
}

.subtitle {
    font-size: 18px;
    color: #666;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("🎓 FacultyFlow")

st.sidebar.caption(
    "AI-Powered Faculty Work Management System"
)

menu = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📚 Course Planner",
        "📁 Project Tracker",
        "📝 Assignment Generator",
        "📄 Digital Forms",
        "📊 NBA Documentation",
        "⏰ Tasks & Reminders"
    ]
)


# =========================================================
# DASHBOARD
# =========================================================

if menu == "🏠 Dashboard":

    st.markdown(
        '<div class="title">Good Morning, Faculty! 👋</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Welcome to FacultyFlow</div>',
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📚 Courses",
            len(st.session_state.courses)
        )

    with col2:
        st.metric(
            "📁 Projects",
            len(st.session_state.projects)
        )

    with col3:
        st.metric(
            "⏰ Pending Tasks",
            len(st.session_state.tasks)
        )

    with col4:
        st.metric(
            "📄 Forms",
            len(st.session_state.forms)
        )

    st.divider()

    st.subheader("⚡ Quick Actions")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.info(
            "📚 **Course Planner**\n\n"
            "Create and modify dynamic course plans."
        )

    with c2:
        st.info(
            "📁 **Project Tracker**\n\n"
            "Track project batches and student progress."
        )

    with c3:
        st.info(
            "📄 **Digital Forms**\n\n"
            "Replace repetitive paper-based forms."
        )

    st.divider()

    st.subheader("📌 Faculty Problem Areas")

    problems = pd.DataFrame({
        "Problem": [
            "Course plan updates",
            "Project follow-ups",
            "NBA documentation",
            "Paper-based forms",
            "Administrative workload"
        ],
        "Status": [
            "Needs Attention",
            "In Progress",
            "Pending",
            "Digital Solution Available",
            "Needs Automation"
        ]
    })

    st.dataframe(
        problems,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# COURSE PLANNER
# =========================================================

elif menu == "📚 Course Planner":

    st.title("📚 Smart Course Planner")

    st.write(
        "Create a course plan that can be modified according "
        "to student learning pace."
    )

    course_name = st.text_input(
        "Course Name"
    )

    total_hours = st.number_input(
        "Total Teaching Hours",
        min_value=1,
        max_value=200,
        value=40
    )

    units = st.number_input(
        "Number of Units",
        min_value=1,
        max_value=10,
        value=5
    )

    student_level = st.selectbox(
        "Student Learning Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    if st.button("✨ Generate Course Plan"):

        if course_name == "":
            st.warning("Please enter the course name.")

        else:

            hours_per_unit = round(
                total_hours / units,
                2
            )

            plan = []

            for i in range(1, units + 1):

                plan.append({
                    "Unit": f"Unit {i}",
                    "Planned Hours": hours_per_unit,
                    "Learning Level": student_level,
                    "Activity":
                        "Lecture + Discussion + Assignment"
                })

            df = pd.DataFrame(plan)

            st.success(
                "Course plan generated successfully!"
            )

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

            st.session_state.courses.append(
                course_name
            )


# =========================================================
# PROJECT TRACKER
# =========================================================

elif menu == "📁 Project Tracker":

    st.title("📁 Project Batch Tracker")

    st.write(
        "Track project batches, progress and pending work."
    )

    with st.form("project_form"):

        batch = st.text_input(
            "Project Batch"
        )

        guide = st.text_input(
            "Faculty Guide"
        )

        topic = st.text_input(
            "Project Topic"
        )

        progress = st.slider(
            "Project Progress (%)",
            0,
            100,
            50
        )

        submitted = st.selectbox(
            "Latest Review Status",
            [
                "Submitted",
                "Pending"
            ]
        )

        submit = st.form_submit_button(
            "➕ Add Project"
        )

        if submit:

            st.session_state.projects.append({
                "Batch": batch,
                "Guide": guide,
                "Topic": topic,
                "Progress": progress,
                "Review": submitted
            })

            st.success(
                "Project batch added!"
            )

    st.divider()

    if st.session_state.projects:

        df = pd.DataFrame(
            st.session_state.projects
        )

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        pending = [
            p for p in st.session_state.projects
            if p["Review"] == "Pending"
        ]

        if pending:

            st.warning(
                f"⚠️ {len(pending)} project batch(es) "
                "require follow-up."
            )


# =========================================================
# ASSIGNMENT GENERATOR
# =========================================================

elif menu == "📝 Assignment Generator":

    st.title("📝 AI Assignment Generator")

    st.write(
        "Generate an assignment based on the topic, "
        "difficulty and learning outcome."
    )

    topic = st.text_input(
        "Topic"
    )

    difficulty = st.selectbox(
        "Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

    outcome = st.text_input(
        "Learning Outcome"
    )

    if st.button("🤖 Generate Assignment"):

        if not topic:
            st.warning(
                "Please enter a topic."
            )

        else:

            st.success(
                "Assignment generated!"
            )

            st.markdown(
                f"""
### Assignment

**Topic:** {topic}

**Difficulty:** {difficulty}

**Learning Outcome:** {outcome}

---

### Questions

**Q1.** Explain the concept of {topic}.

**Q2.** Describe the important features
of {topic} with suitable examples.

**Q3.** Apply the concept of {topic}
to a real-world problem.

**Q4.** Compare different approaches
related to {topic}.

**Q5.** Write a short case study based
on {topic}.
"""
            )


# =========================================================
# DIGITAL FORMS
# =========================================================

elif menu == "📄 Digital Forms":

    st.title("📄 Digital Forms")

    st.write(
        "Replace repetitive paper-based forms "
        "with digital submission."
    )

    form_type = st.selectbox(
        "Select Form",
        [
            "Leave Form",
            "Project Review Form",
            "Course Plan Form",
            "Student Feedback Form",
            "Department Form"
        ]
    )

    name = st.text_input(
        "Faculty Name"
    )

    reason = st.text_area(
        "Details / Reason"
    )

    if st.button("📤 Submit Form"):

        st.session_state.forms.append({
            "Form": form_type,
            "Faculty": name,
            "Date": str(date.today()),
            "Status": "Submitted"
        })

        st.success(
            "Form submitted successfully!"
        )

    if st.session_state.forms:

        st.subheader(
            "Submitted Forms"
        )

        df = pd.DataFrame(
            st.session_state.forms
        )

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )


# =========================================================
# NBA DOCUMENTATION
# =========================================================

elif menu == "📊 NBA Documentation":

    st.title("📊 NBA Documentation Center")

    st.write(
        "Track important academic documentation "
        "from one place."
    )

    documents = {
        "Course Plan": False,
        "CO-PO Mapping": False,
        "Assignments": False,
        "Student Feedback": False,
        "Attendance": False,
        "Result Analysis": False
    }

    completed = 0

    for document in documents:

        checked = st.checkbox(
            document
        )

        if checked:
            completed += 1

    progress = int(
        (completed / len(documents)) * 100
    )

    st.progress(
        progress / 100
    )

    st.write(
        f"Documentation Progress: **{progress}%**"
    )

    if st.button("📄 Generate Report"):

        st.success(
            "NBA documentation report draft generated!"
        )

        st.write(
            f"Current documentation completion: "
            f"{progress}%"
        )


# =========================================================
# TASKS
# =========================================================

elif menu == "⏰ Tasks & Reminders":

    st.title("⏰ Tasks & Reminders")

    task = st.text_input(
        "Task"
    )

    deadline = st.date_input(
        "Deadline"
    )

    if st.button("➕ Add Task"):

        st.session_state.tasks.append({
            "Task": task,
            "Deadline": str(deadline),
            "Status": "Pending"
        })

        st.success(
            "Task added!"
        )

    if st.session_state.tasks:

        df = pd.DataFrame(
            st.session_state.tasks
        )

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.warning(
            "🔔 Reminder: Review your pending tasks."
        )
