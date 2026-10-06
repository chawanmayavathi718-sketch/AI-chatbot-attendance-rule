import streamlit as st

# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="AI Attendance Assistant",
    page_icon="🎓",
    layout="centered"
)

# -----------------------------------
# CUSTOM CSS
# -----------------------------------

st.markdown("""
<style>

.title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# TITLE
# -----------------------------------

st.markdown(
    '<div class="title">🎓 AI Attendance Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Check your attendance according to college rules'
    '</div>',
    unsafe_allow_html=True
)

# -----------------------------------
# COLLEGE ATTENDANCE RULE
# -----------------------------------

REQUIRED_ATTENDANCE = 75

st.info(
    f"📚 Minimum required attendance: **{REQUIRED_ATTENDANCE}%**"
)

# -----------------------------------
# STUDENT NAME
# -----------------------------------

student_name = st.text_input(
    "👤 Enter Student Name",
    placeholder="Example: Sindhura"
)

# -----------------------------------
# ATTENDANCE INPUT
# -----------------------------------

attendance = st.number_input(
    "📊 Enter Your Attendance Percentage",
    min_value=0.0,
    max_value=100.0,
    value=75.0,
    step=0.1
)

# -----------------------------------
# CHECK BUTTON
# -----------------------------------

if st.button(
    "🤖 Check Attendance",
    use_container_width=True
):

    if student_name.strip() == "":
        st.warning("⚠️ Please enter your name.")

    else:

        # -----------------------------------
        # BELOW REQUIRED ATTENDANCE
        # -----------------------------------

        if attendance < REQUIRED_ATTENDANCE:

            shortage = REQUIRED_ATTENDANCE - attendance

            st.error(
                f"⚠️ Warning {student_name}!"
            )

            st.warning(
                f"Your attendance is **{attendance:.1f}%**."
            )

            st.write(
                f"Your attendance is **{shortage:.1f}%** "
                f"below the required {REQUIRED_ATTENDANCE}%."
            )

            st.error(
                "❌ You need to improve your attendance."
            )

        # -----------------------------------
        # REQUIRED ATTENDANCE
        # -----------------------------------

        else:

            st.success(
                f"✅ Good attendance, {student_name}!"
            )

            st.success(
                f"Your attendance is **{attendance:.1f}%**, "
                f"which meets the required "
                f"{REQUIRED_ATTENDANCE}%."
            )

            st.balloons()

# -----------------------------------
# ATTENDANCE RULE
# -----------------------------------

st.markdown("---")

st.markdown("### 📚 Attendance Rule")

st.write(
    f"""
    According to the attendance rule used in this application,
    students should maintain at least **{REQUIRED_ATTENDANCE}%**
    attendance.

    - 🟢 **{REQUIRED_ATTENDANCE}% or above:** Good attendance
    - 🔴 **Below {REQUIRED_ATTENDANCE}%:** Attendance shortage warning
    """
)

# -----------------------------------
# FOOTER
# -----------------------------------

st.markdown("---")

st.caption(
    "🎓 AI Attendance Assistant | "
    "Attendance checking tool"
)