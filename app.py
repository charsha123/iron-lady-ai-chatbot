
import streamlit as st

# ---------------------------------
# PAGE CONFIG
# ---------------------------------
st.set_page_config(
    page_title="🤖 Iron Lady AI Program Guide",
    layout="wide"
)

# ---------------------------------
# CUSTOM CSS (BLACK + RED THEME)
# ---------------------------------
st.markdown("""
<style>
.stApp {
    background-color: #0B0B0B;
    color: white;
}

h1 {
    font-weight: 900;
}

.stCaption {
    color: #B0B0B0;
}

textarea {
    background-color: #111111 !important;
    color: white !important;
    border: 1px solid #B11226 !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------
# HEADER
# ---------------------------------
st.markdown("""
<h1 style="text-align:center;">
    <span style="color:#B11226;">🤖 IRON LADY</span>
    <span style="color:white;"> AI Program Guide</span>
</h1>
""", unsafe_allow_html=True)

st.caption("Empowering women with leadership, confidence, and career clarity")

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------
# SESSION STATE
# ---------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "stage" not in st.session_state:
    st.session_state.stage = "welcome"

# ---------------------------------
# DISPLAY CHAT HISTORY
# ---------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------------------------------
# WELCOME MESSAGE
# ---------------------------------
if st.session_state.stage == "welcome":
    welcome_text = (
        "Hi 👋 Welcome to Iron Lady!\n\n"
        "I’m your AI Program Guide. I help women explore leadership, skill-building, "
        "and career growth programs.\n\n"
        "**May I know your background?**\n"
        "(Student / Working Professional / Career Break / Exploring)"
    )
    st.session_state.messages.append(
        {"role": "assistant", "content": welcome_text}
    )
    st.session_state.stage = "background"
    st.rerun()

# ---------------------------------
# USER INPUT
# ---------------------------------
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    reply = ""

    # ---------------------------------
    # BACKGROUND LOGIC
    # ---------------------------------
    if st.session_state.stage == "background":
        if "student" in user_input.lower():
            reply = (
                "Great! 🎓 As a student, Iron Lady offers programs that help you "
                "build confidence, leadership mindset, and career clarity.\n\n"
                "**What is your main goal right now?**\n"
                "(Learn skills / Career readiness / Leadership growth)"
            )
            st.session_state.stage = "goal"

        elif "working" in user_input.lower():
            reply = (
                "Nice! 💼 As a working professional, Iron Lady helps you "
                "break career plateaus and grow into leadership roles.\n\n"
                "**What are you looking for right now?**\n"
                "(Promotion / Leadership skills / Career transition)"
            )
            st.session_state.stage = "goal"

        elif "career" in user_input.lower():
            reply = (
                "That’s absolutely okay 💛\n"
                "Iron Lady supports women returning to work with confidence and clarity.\n\n"
                "**What would you like help with?**\n"
                "(Confidence / Skill rebuilding / Career direction)"
            )
            st.session_state.stage = "goal"

        else:
            reply = (
                "No problem 😊\n"
                "Many people explore before deciding.\n\n"
                "**Would you like to know about our programs or how enrollment works?**"
            )
            st.session_state.stage = "programs"

    # ---------------------------------
    # GOAL LOGIC
    # ---------------------------------
    elif st.session_state.stage == "goal":
        reply = (
            "Perfect! Based on your interest, I recommend:\n\n"
            "✅ **Skill Development Program** – practical, beginner-friendly learning\n"
            "✅ **Career Readiness Program** – confidence, communication, and clarity\n\n"
            "These programs are designed to help women grow personally and professionally.\n\n"
            "**Would you like to know about enrollment or program duration?**"
        )
        st.session_state.stage = "enrollment"

    # ---------------------------------
    # ENROLLMENT LOGIC
    # ---------------------------------
    elif st.session_state.stage == "enrollment":
        reply = (
            "Enrollment is simple 😊\n\n"
            "1️⃣ Choose a suitable program\n"
            "2️⃣ Fill out the enrollment form\n"
            "3️⃣ Our team reviews your profile\n"
            "4️⃣ You receive onboarding details\n\n"
            "**Would you like to explore another program or need help with anything else?**"
        )
        st.session_state.stage = "end"

    else:
        reply = (
            "I’m here to help 😊\n"
            "You can ask me about Iron Lady programs, leadership growth, or enrollment anytime."
        )

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
    st.rerun()
