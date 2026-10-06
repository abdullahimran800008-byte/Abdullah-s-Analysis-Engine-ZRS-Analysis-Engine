import streamlit as st
import pandas as pd
import datetime

# Page Configuration
st.set_page_config(
    page_title="Abdullah's Analysis Engine",
    page_icon="⚡",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    header, footer { visibility: hidden; }
    .main-title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: bold;
        color: #1E88E5;
    }
    .sub-title {
        text-align: center;
        font-size: 1.1rem;
        color: #AAA;
        margin-bottom: 25px;
    }
    .login-box {
        background-color: #161B22;
        padding: 35px;
        border-radius: 12px;
        border: 1px solid #1E88E5;
        text-align: center;
        max-width: 480px;
        margin: 50px auto;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# AUTHENTICATION & SESSION STATE MANAGEMENT
# -----------------------------------------------------------------------------
if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False
if "user_gmail" not in st.session_state:
    st.session_state.user_gmail = ""
if "history" not in st.session_state:
    st.session_state.history = []

def perform_login(email):
    email_clean = email.strip()
    if "@gmail.com" in email_clean.lower() or "@" in email_clean:
        st.session_state.is_logged_in = True
        st.session_state.user_gmail = email_clean
        st.rerun()
    else:
        st.error("Baraye meharbani sahi Gmail address enter karein.")

def perform_logout():
    st.session_state.is_logged_in = False
    st.session_state.user_gmail = ""
    st.rerun()

# -----------------------------------------------------------------------------
# SCREEN 1: GMAIL LOGIN GATE (AGAR USER LOGGED IN NAHI HAI)
# -----------------------------------------------------------------------------
if not st.session_state.is_logged_in:
    st.markdown("""
        <div class='login-box'>
            <h2>⚡ Abdullah's Analysis Engine</h2>
            <p style='color: #888;'>System access karne ke liye apna Gmail enter karein.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        gmail_input = st.text_input("Gmail Address:", placeholder="yourname@gmail.com")
        if st.button("🔑 Access Engine", use_container_width=True):
            perform_login(gmail_input)
            
        st.caption("🔒 Secured Session Portal")

# -----------------------------------------------------------------------------
# SCREEN 2: MAIN ENGINE WORKSPACE (GMAIL LOGIN KE BAAD)
# -----------------------------------------------------------------------------
else:
    # Header & User Info Bar
    head_col1, head_col2 = st.columns([4, 1])
    with head_col1:
        st.markdown("<div class='main-title'>⚡ Abdullah's Analysis & Solution Engine</div>", unsafe_allow_html=True)
        st.markdown("<div class='sub-title'>Universal System Analysis based on C-E-P-N Logic</div>", unsafe_allow_html=True)
    with head_col2:
        st.write(f"👤 `{st.session_state.user_gmail}`")
        if st.button("🚪 Logout"):
            perform_logout()

    # Sidebar Settings
    st.sidebar.header("🎯 Select Domain")
    domain = st.sidebar.selectbox(
        "Choose System Category:",
        [
            "Fast Bowling & Sports Bio-Fatigue",
            "Financial Market Risk (SMC/VSA)",
            "Civilizational & Geopolitical Dynamics",
            "Custom Universal Scenario"
        ]
    )

    st.sidebar.markdown("---")
    st.sidebar.write(f"Active User: **{st.session_state.user_gmail}**")

    # Main Inputs Section
    st.header(f"📊 Inputs: {domain}")

    col1, col2 = st.columns(2)

    with col1:
        scenario_title = st.text_input("Scenario Name:", value="Default Assessment")
        c_val = st.slider("Constitutive Capacity (C) - Base Strength", 0.0, 1.0, 0.70, 0.05)
        e_val = st.slider("Existential Foresight / Resources (E) - Adaptability", 0.0, 1.0, 0.60, 0.05)

    with col2:
        p_val = st.slider("Power Output / Workload Stress (P)", 0.0, 1.0, 0.50, 0.05)
        n_val = st.slider("Natural Limits / Systemic Friction (N)", 0.1, 1.0, 0.40, 0.05)

    # Persistence Formula Calculation: P_idx = (C + E + P) / (2 * N)
    score = (c_val + e_val + p_val) / (2 * n_val)
    score_normalized = min(max(score, 0.0), 2.0)

    if score_normalized >= 1.2:
        status = "STABLE / OPTIMAL"
        color = "green"
    elif score_normalized >= 0.8:
        status = "WARNING / STRESS ZONE"
        color = "orange"
    else:
        status = "CRITICAL / COLLAPSE RISK"
        color = "red"

    # Results & Solution Zone
    st.markdown("---")
    st.header("📈 Evaluation & Solution Zone")

    res_col1, res_col2 = st.columns([1, 2])

    with res_col1:
        st.metric(label="System Persistence Score", value=f"{score_normalized:.2f}")
        if color == "green":
            st.success(f"Status: {status}")
        elif color == "orange":
            st.warning(f"Status: {status}")
        else:
            st.error(f"Status: {status}")

    with res_col2:
        st.subheader("💡 Solution Zone")
        if color == "red":
            st.write("❌ **Critical Status:** High systemic stress. Immediate workload reduction and structural reinforcement required.")
        elif color == "orange":
            st.write("⚠️ **Warning Status:** System under elevated friction. Monitor recovery/reserves.")
        else:
            st.write("✅ **Optimal Status:** Operational parameters are sustainable.")

    # Save Analysis to History
    if st.button("💾 Save Analysis to History"):
        entry = {
            "Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "User": st.session_state.user_gmail,
            "Domain": domain,
            "Scenario": scenario_title,
            "Score": f"{score_normalized:.2f}",
            "Status": status
        }
        st.session_state.history.append(entry)
        st.success("Analysis log save ho gaya hai!")

    # Display History Table
    if st.session_state.history:
        st.markdown("---")
        st.header("📜 Saved Analysis History")
        df_history = pd.DataFrame(st.session_state.history)
        st.dataframe(df_history, use_container_width=True)

import streamlit.components.v1 as 

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5291809284478036"
     crossorigin="anonymous"></script>
