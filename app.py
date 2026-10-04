import numpy as np
import plotly.graph_objects as go
import streamlit as st
from scipy.integrate import solve_ivp

# ==========================================
# 1. PAGE CONFIGURATION & STYLING
# ==========================================
st.set_page_config(
    page_title="Abdullah's Analysis Engine — GUT-SPF",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
""",
    unsafe_allow_html=True,
)

# ==========================================
# 2. HEADER & FRAMEWORK ARCHITECTURE
# ==========================================
st.title("⚡ Grand Unified Framework for Systemic Persistence (GUT-SPF)")
st.caption(
    "**Abdullah's Analysis Engine** | System Stability & Collapse Prediction Platform"
)

st.markdown("""
> **Theoretical Core:** Dynamic evaluation of systemic resilience via constitutive capacity ($C$), existential foresight ($E$), power output ($P$), and natural limits ($N$).
""")

# ==========================================
# 3. SIDEBAR — PARAMETER & DOMAIN SELECTION
# ==========================================
st.sidebar.header("🎯 System Domain Profile")
domain = st.sidebar.selectbox(
    "Select Target Profile",
    [
        "High-Performance Athletics (Fast Bowling)",
        "Civilizational Systems Dynamics",
        "Biological / Metabolic Homeostasis",
        "Macro-Economic Infrastructure",
        "Custom Parameters",
    ],
)

presets = {
    "High-Performance Athletics (Fast Bowling)": {
        "C": 0.85,
        "E": 0.75,
        "P": 0.92,
        "N": 0.95,
        "desc": "Focus: High kinetic workload (140+ km/h), physical limits, and fatigue recovery dynamics.",
    },
    "Civilizational Systems Dynamics": {
        "C": 0.65,
        "E": 0.50,
        "P": 0.80,
        "N": 0.85,
        "desc": "Focus: Resource consumption, consciousness, institutional foresight, and systemic collapse bounds.",
    },
    "Biological / Metabolic Homeostasis": {
        "C": 0.90,
        "E": 0.80,
        "P": 0.40,
        "N": 0.95,
        "desc": "Focus: Organism stability, cellular energy expenditure, and stress threshold boundaries.",
    },
    "Macro-Economic Infrastructure": {
        "C": 0.55,
        "E": 0.60,
        "P": 0.88,
        "N": 0.90,
        "desc": "Focus: Supply chain strain, market velocity, capital reserves, and structural limits.",
    },
    "Custom Parameters": {
        "C": 0.70,
        "E": 0.70,
        "P": 0.50,
        "N": 0.90,
        "desc": "Custom manual input for specialized theoretical modeling.",
    },
}

selected_preset = presets[domain]
st.sidebar.info(selected_preset["desc"])

st.sidebar.markdown("---")
st.sidebar.header("⚙️ GUT-SPF Equation Weights")
beta = st.sidebar.slider("β (Capacity Weight)", 0.0, 1.0, 0.60, 0.05)
gamma = st.sidebar.slider("γ (Foresight Weight)", 0.0, 1.0, 0.40, 0.05)
alpha = st.sidebar.slider("α (Power Scaling)", 0.1, 2.0, 1.00, 0.05)

# ==========================================
# 4. SYSTEM INPUT VARIABLES
# ==========================================
col_in1, col_in2 = st.columns(2)

with col_in1:
    st.subheader("📥 Primary Parameters")
    C = st.slider(
        "Constitutive Capacity (C)",
        0.01,
        1.00,
        selected_preset["C"],
        0.01,
        help="Physical base, structural integrity, raw resources.",
    )
    E = st.slider(
        "Existential Foresight / Adaptation (E)",
        0.01,
        1.00,
        selected_preset["E"],
        0.01,
        help="Biological intelligence, biomechanical feedback, strategic adaptation.",
    )

with col_in2:
    st.subheader("⚡ Operational Dynamics")
    P = st.slider(
        "Power Output / Workload (P)",
        0.01,
        1.00,
        selected_preset["P"],
        0.01,
        help="Kinetic output, execution force, operational demand.",
    )
    N = st.slider(
        "Natural / Environmental Limits (N)",
        0.01,
        1.00,
        selected_preset["N"],
        0.01,
        help="Absolute biological, physical, or structural ceiling.",
    )

# ==========================================
# 5. CORE MATHEMATICAL CALCULATION ENGINE
# ==========================================
st.markdown("---")


def calculate_persistence(C, E, P, N, beta, gamma, alpha):
    if P >= N:
        return 0.0, "CRITICAL_VIOLATION"

    capacity_ratio = (beta * C + gamma * E) / (alpha * P)
    bounded_ratio = min(1.0, capacity_ratio)
    limit_margin = 1.0 - (P / N)

    I = 1.0 - (bounded_ratio * limit_margin)
    return float(np.clip(I, 0.0, 1.0)), "OK"


I_score, status = calculate_persistence(C, E, P, N, beta, gamma, alpha)

# Dashboard Columns
col_res1, col_res2, col_res3 = st.columns([1, 1, 1])

with col_res1:
    st.metric(
        label="Persistence Index (I)",
        value=f"{I_score:.4f}",
        delta=f"{I_score - 0.70:.4f} vs Threshold",
    )

with col_res2:
    if status == "CRITICAL_VIOLATION":
        zone_color = "🔴"
        zone_name = "CRITICAL / BOUNDARY BREACH"
    elif I_score >= 0.70:
        zone_color = "🟢"
        zone_name = "STABLE ZONE"
    elif 0.40 <= I_score < 0.70:
        zone_color = "🟡"
        zone_name = "STRESSED ZONE"
    else:
        zone_color = "🔴"
        zone_name = "CRITICAL / COLLAPSE ZONE"

    st.metric(label="System Status", value=f"{zone_color} {zone_name}")

with col_res3:
    stress_ratio = (P / N) * 100
    st.metric(label="Limit Utilization (P/N)", value=f"{stress_ratio:.1f}%")

# ==========================================
# 6. ACTIONABLE DIAGNOSTIC & REMEDIATION ENGINE
# ==========================================
st.subheader("💡 Automated Remediation Strategy")

if status == "CRITICAL_VIOLATION":
    st.error(
        "**EMERGENCY OVERRIDE:** Power Output ($P$) has breached or reached Natural Limits ($N$). Total structural collapse or career-ending injury trigger is active. Immediately scale back operational load!"
    )
elif I_score >= 0.70:
    st.success(
        "**OPTIMAL SYSTEM BALANCE:** The system possesses adequate constitutive capacity and strategic adaptation to support current power output. Maintain load and monitor parameter drift."
    )
elif 0.40 <= I_score < 0.70:
    st.warning(
        "**STRESS DETECTED:** System is entering the degradation threshold. Apply targeted intervention:"
    )
    rec1 = (
        f"* **Reduce Kinetic Demand ($P$):** Decrease workload by at least {((P - 0.7*N)/P)*100:.1f}% to restore safety margin."
        if P / N > 0.75
        else ""
    )
    rec2 = "* **Augment Capacity ($C$):** Implement recovery protocols, hydration cycles, or baseline structural reinforcement."
    rec3 = "* **Elevate Foresight ($E$):** Optimize execution biomechanics and feedback tracking."
    st.markdown(f"{rec1}\n{rec2}\n{rec3}")
else:
    st.error(
        "**CRITICAL COLLAPSE RISK:** High probability of imminent breakdown."
    )
    st.markdown(
        "**Remediation Blueprint:** Force dynamic load shedding ($P \\rightarrow P/2$) and focus on capacity reconstruction ($C$) and adaptive realignment ($E$)."
    )

# ==========================================
# 7. TIME-SERIES ODE SIMULATION ENGINE
# ==========================================
st.markdown("---")
st.subheader("📈 Time-Series Dynamic Projection (Differential Equations)")


def system_ode(t, y):
    c_val, e_val, p_val, n_val = y
    dc_dt = 0.02 * e_val - 0.05 * p_val
    de_dt = 0.01 * c_val - 0.01 * p_val
    dp_dt = 0.01 * (n_val - p_val)
    dn_val = -0.005 * (p_val / n_val)
    return [dc_dt, de_dt, dp_dt, dn_val]


t_span = (0, 50)
t_eval = np.linspace(0, 50, 200)
y0 = [C, E, P, N]
solution = solve_ivp(system_ode, t_span, y0, t_eval=t_eval)

I_time = []
for idx in range(len(t_eval)):
    c_t, e_t, p_t, n_t = solution.y[:, idx]
    idx_val, _ = calculate_persistence(
        c_t, e_t, p_t, n_t, beta, gamma, alpha
    )
    I_time.append(idx_val)

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=t_eval,
        y=I_time,
        mode="lines",
        name="Persistence Index I(t)",
        line=dict(color="#00E676", width=3),
    )
)
fig.add_trace(
    go.Scatter(
        x=t_eval,
        y=solution.y[0],
        mode="lines",
        name="Capacity C(t)",
        line=dict(color="#29B6F6", dash="dash"),
    )
)
fig.add_trace(
    go.Scatter(
        x=t_eval,
        y=solution.y[2],
        mode="lines",
        name="Power Output P(t)",
        line=dict(color="#FF5252", dash="dot"),
    )
)

fig.add_hline(
    y=0.70,
    line_dash="dash",
    line_color="green",
    annotation_text="Stable Threshold (0.7)",
)
fig.add_hline(
    y=0.40,
    line_dash="dash",
    line_color="red",
    annotation_text="Critical Threshold (0.4)",
)

fig.update_layout(
    title="System Trajectory Simulation over Time (t)",
    xaxis_title="Time Steps (t)",
    yaxis_title="Index / Variable Value",
    template="plotly_dark",
    height=450,
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption(
    "© Abdullah's Analysis Engine — Formalized for Global Open-Source Deployment."
)
