import streamlit as st
import pandas as pd
import datetime

# Page Configuration
st.set_page_config(
    page_title="Abdullah's Analysis & Solution Engine",
    page_icon="⚡",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: bold;
        color: #1E88E5;
    }
    .sub-title {
        text-align: center;
        font-size: 1.1rem;
        color: #666;
        margin-bottom: 25px;
    }
    .solution-card {
        background-color: #0E1117;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #00C853;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='main-title'>⚡ Abdullah's Analysis & Solution Engine</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Universal System Analysis based on C-E-P-N Logic & Actionable Solution Engine</div>", unsafe_allow_html=True)

# Initialize History State
if 'history' not in st.session_state:
    st.session_state.history = []

# Sidebar Domain Selection
st.sidebar.header("🎯 Select Analysis Domain")
domain = st.sidebar.selectbox(
    "Choose System Category:",
    [
        "Fast Bowling & Sports Bio-Fatigue",
        "Financial Market Risk (SMC/VSA)",
        "Civilizational & Geopolitical Dynamics",
        "Custom Universal Scenario"
    ]
)

# Presets Section
st.sidebar.markdown("---")
st.sidebar.header("📌 Quick Historical / Benchmark Presets")

preset_selected = False
preset_c, preset_e, preset_p, preset_n = 0.5, 0.5, 0.5, 0.5
preset_name = ""

if domain == "Fast Bowling & Sports Bio-Fatigue":
    if st.sidebar.button("Load: High Bowling Workload Stress"):
        preset_c, preset_e, preset_p, preset_n = 0.65, 0.40, 0.90, 0.85
        preset_name = "High Bowling Workload Stress"
        preset_selected = True

elif domain == "Financial Market Risk (SMC/VSA)":
    if st.sidebar.button("Load: Market Liquidity Crunch"):
        preset_c, preset_e, preset_p, preset_n = 0.40, 0.35, 0.85, 0.80
        preset_name = "Market Liquidity Crunch"
        preset_selected = True

elif domain == "Civilizational & Geopolitical Dynamics":
    if st.sidebar.button("Load: Late Roman Empire Overreach"):
        preset_c, preset_e, preset_p, preset_n = 0.30, 0.25, 0.80, 0.90
        preset_name = "Late Roman Empire Overreach"
        preset_selected = True

# Main Input Layout
st.header(f"📊 Inputs: {domain}")

col1, col2 = st.columns(2)

with col1:
    scenario_title = st.text_input("Scenario / Subject Name:", value=preset_name if preset_selected else "Default Assessment")
    
    c_val = st.slider(
        "Constitutive Capacity (C) - Base Strength / Core Foundation",
        0.0, 1.0, preset_c if preset_selected else 0.70, 0.05
    )
    e_val = st.slider(
        "Existential Foresight / Resources (E) - Adaptability & Backup",
        0.0, 1.0, preset_e if preset_selected else 0.60, 0.05
    )

with col2:
    p_val = st.slider(
        "Power Output / Workload Stress (P) - Output Load",
        0.0, 1.0, preset_p if preset_selected else 0.50, 0.05
    )
    n_val = st.slider(
        "Natural Limits / Systemic Friction (N) - Environmental Limits",
        0.1, 1.0, preset_n if preset_selected else 0.40, 0.05
    )

# Logic Calculation: Persistence Index P_idx = (C + E + P) / (2 * N)
score = (c_val + e_val + p_val) / (2 * n_val)
score_normalized = min(max(score, 0.0), 2.0)

# Status Determination
if score_normalized >= 1.2:
    status = "STABLE / OPTIMAL"
    color = "green"
elif score_normalized >= 0.8:
    status = "WARNING / STRESS ZONE"
    color = "orange"
else:
    status = "CRITICAL / COLLAPSE RISK"
    color = "red"

# Results Section
st.markdown("---")
st.header("📈 System Evaluation & Solution Zone")

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
    st.subheader("💡 Actionable Solution Zone")
    
    if domain == "Fast Bowling & Sports Bio-Fatigue":
        if color == "red":
            st.write("❌ **Problem:** Extreme mechanical fatigue / injury risk due to high load and low recovery.")
            st.write("🛠️ **Solution:** Reduce workload immediately. Increase recovery intervals, focus on shoulder/core strengthening, and adjust bowling stride efficiency.")
        elif color == "orange":
            st.write("⚠️ **Problem:** Moderate bio-mechanical friction detected.")
            st.write("🛠️ **Solution:** Maintain rotation drills, monitor bowling spell length, and optimize sleep/nutrition protocols.")
        else:
            st.write("✅ **Status:** Peak physical conditioning and sustainable workload ratio.")

    elif domain == "Financial Market Risk (SMC/VSA)":
        if color == "red":
            st.write("❌ **Problem:** High market volatility / FVG setup failure risk.")
            st.write("🛠️ **Solution:** Avoid aggressive entry. Wait for liquidity sweep confirm, tighten Stop Loss, and reduce risk-to-reward position sizing.")
        elif color == "orange":
            st.write("⚠️ **Problem:** Market showing signs of order block exhaustion.")
            st.write("🛠️ **Solution:** Wait for high-volume confirmation before entering trades. Protect capital.")
        else:
            st.write("✅ **Status:** Strong market structure alignment and manageable risk parameters.")

    elif domain == "Civilizational & Geopolitical Dynamics":
        if color == "red":
            st.write("❌ **Problem:** Systemic overreach exceeding natural and existential limits.")
            st.write("🛠️ **Solution:** De-escalate resource consumption, reinforce institutional core (C), and focus on internal resource preservation.")
        elif color == "orange":
            st.write("⚠️ **Problem:** Rising systemic friction.")
            st.write("🛠️ **Solution:** Optimize resource distribution and improve strategic foresight (E).")
        else:
            st.write("✅ **Status:** High systemic stability and strong adaptive endurance.")

    else:
        if color == "red":
            st.write("❌ **Problem:** System is overloaded beyond operational limit N.")
            st.write("🛠️ **Solution:** Reduce stress P immediately and increase base capacity C.")
        else:
            st.write("✅ **Status:** Balanced operational parameters.")

# Save to History
if st.button("💾 Save Analysis to History"):
    entry = {
        "Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Domain": domain,
        "Scenario": scenario_title,
        "Score": f"{score_normalized:.2f}",
        "Status": status
    }
    st.session_state.history.append(entry)
    st.success("Analysis saved to history log below!")

# History Log Table
if st.session_state.history:
    st.markdown("---")
    st.header("📜 Saved Analysis History")
    df_history = pd.DataFrame(st.session_state.history)
    st.dataframe(df_history, use_container_width=True)
    
    if st.button("🗑️ Clear History"):
        st.session_state.history = []
        st.rerun()
