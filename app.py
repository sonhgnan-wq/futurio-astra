# ==========================================================
# FUTURIO ASTRA v2.0 – COMMERCIAL EDITION
# Senior Fullstack & Career Data Intelligence Build
# ==========================================================

import streamlit as st
import numpy as np
import random
import plotly.graph_objects as go

# ==========================================================
# CONFIG
# ==========================================================

st.set_page_config(
    page_title="Futurio Astra",
    page_icon="🚀",
    layout="wide"
)

# ==========================================================
# PERFORMANCE CACHE
# ==========================================================

@st.cache_resource
def load_weights():
    return {
        "Logic": 1.4,
        "Sáng tạo": 1.2,
        "Giao tiếp": 1.1,
        "Phân tích": 1.5,
        "Quản lý": 1.3
    }

# ==========================================================
# UI SETUP (DEEP CUSTOM CSS)
# ==========================================================

def setup_ui():

    st.markdown("""
    <style>

    .stApp {
        background: radial-gradient(circle at 30% 20%, #0f172a, #020617);
        color: #e2e8f0;
    }

    /* Centered container */
    .main-container {
        max-width: 900px;
        margin: auto;
    }

    /* Glass Card */
    .glass {
        background: rgba(255,255,255,0.05);
        border-radius: 16px;
        padding: 28px;
        border: 1px solid rgba(255,255,255,0.15);
        box-shadow: 0 0 25px rgba(0,242,255,0.15);
        margin-bottom: 24px;
    }

    /* Buttons */
    div.stButton > button {
        border-radius: 16px !important;
        background: linear-gradient(90deg,#7000ff,#00f2ff);
        color: white;
        border: none;
        font-weight: 600;
        padding: 12px 22px;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        transform: scale(1.05);
        opacity: 0.9;
    }

    /* Slider Custom */
    div[data-baseweb="slider"] span {
        background: linear-gradient(90deg,#7000ff,#00f2ff) !important;
    }

    div[data-baseweb="slider"] div[role="slider"] {
        background: #00f2ff !important;
        border: 2px solid white !important;
    }

    /* Progress Stepper */
    .stepper {
        display: flex;
        justify-content: space-between;
        margin-bottom: 30px;
    }

    .step {
        flex: 1;
        text-align: center;
        padding: 8px;
        border-radius: 20px;
        background: rgba(255,255,255,0.05);
        margin: 0 4px;
        font-size: 14px;
    }

    .active-step {
        background: linear-gradient(90deg,#7000ff,#00f2ff);
        color: white;
        font-weight: 600;
    }

    </style>
    """, unsafe_allow_html=True)

# ==========================================================
# CONTENT ENGINE – AVOID REPETITION
# ==========================================================

def generate_content(skill, score):

    library = {
        "high": [
            f"Năng lực {skill} đang ở cấp độ vượt trội.",
            f"Bạn sở hữu nền tảng {skill} đáng chú ý.",
            f"{skill} là lợi thế cạnh tranh chiến lược của bạn.",
            f"Tư duy {skill} của bạn thể hiện độ chín cao.",
            f"Khả năng {skill} có thể tạo đột phá dài hạn."
        ],
        "mid": [
            f"{skill} đang ở mức ổn định.",
            f"Bạn có tiềm năng phát triển thêm về {skill}.",
            f"Năng lực {skill} tương đối cân bằng.",
            f"{skill} là nền tảng có thể nâng cấp.",
            f"Bạn đang sở hữu mức {skill} khá."
        ],
        "low": [
            f"{skill} cần được ưu tiên cải thiện.",
            f"Nâng cấp {skill} sẽ mở rộng cơ hội.",
            f"{skill} hiện chưa phát huy tối đa.",
            f"Đầu tư vào {skill} sẽ tăng biên độ phát triển.",
            f"Bạn nên xây dựng lại chiến lược cho {skill}."
        ]
    }

    if score >= 4:
        return random.choice(library["high"])
    elif score >= 2:
        return random.choice(library["mid"])
    else:
        return random.choice(library["low"])

# ==========================================================
# CALCULATION ENGINE
# ==========================================================

def calculate_scenarios(skills):

    weights = load_weights()

    # Current
    current = np.mean(list(skills.values()))

    # Power Up (boost top 2)
    sorted_skills = sorted(skills.items(), key=lambda x: x[1], reverse=True)
    boosted = dict(sorted_skills[:2])
    power = sum(boosted[k]*weights[k] for k in boosted)

    # Pivot (increase weakest)
    weakest = min(skills, key=skills.get)
    pivot_skills = skills.copy()
    pivot_skills[weakest] += 1
    pivot = np.mean(list(pivot_skills.values()))

    return current, power, pivot

# ==========================================================
# RADAR CHART
# ==========================================================

def render_radar(skills):

    categories = list(skills.keys())
    values = list(skills.values())
    values += values[:1]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories + categories[:1],
        fill='toself',
        name='Hồ sơ năng lực',
        line_color='#00f2ff'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,5],
                gridcolor="rgba(200,200,200,0.2)"
            )
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# STEPPER
# ==========================================================

def render_stepper(step):

    steps = ["Đánh giá", "Kết quả", "Chiến lược", "Tuyên ngôn"]

    html = '<div class="stepper">'
    for i, name in enumerate(steps, start=1):
        if i == step:
            html += f'<div class="step active-step">{i}. {name}</div>'
        else:
            html += f'<div class="step">{i}. {name}</div>'
    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

# ==========================================================
# MAIN
# ==========================================================

def main():

    setup_ui()

    if "step" not in st.session_state:
        st.session_state.step = 1

    with st.container():
        st.markdown('<div class="main-container">', unsafe_allow_html=True)

        render_stepper(st.session_state.step)

        # STEP 1
        if st.session_state.step == 1:

            with st.form("form"):
                skills = {}
                skills["Logic"] = st.slider("Logic",0,5,3,key="logic")
                skills["Sáng tạo"] = st.slider("Sáng tạo",0,5,3,key="creative")
                skills["Phân tích"] = st.slider("Phân tích",0,5,3,key="analysis")
                skills["Giao tiếp"] = st.slider("Giao tiếp",0,5,3,key="communication")
                skills["Quản lý"] = st.slider("Quản lý",0,5,3,key="management")

                submit = st.form_submit_button("Phân tích Astra")

            if submit:
                st.session_state.skills = skills
                st.session_state.step = 2
                st.rerun()

        # STEP 2
        elif st.session_state.step == 2:

            skills = st.session_state.skills
            current, power, pivot = calculate_scenarios(skills)

            render_radar(skills)

            col1, col2, col3 = st.columns(3)

            col1.markdown(f'<div class="glass"><b>Hiện tại</b><br>{round(current,2)}</div>', unsafe_allow_html=True)
            col2.markdown(f'<div class="glass"><b>Power Up</b><br>{round(power,2)}</div>', unsafe_allow_html=True)
            col3.markdown(f'<div class="glass"><b>Pivot</b><br>{round(pivot,2)}</div>', unsafe_allow_html=True)

            if st.button("Tiếp tục"):
                st.session_state.step = 3
                st.rerun()

        # STEP 3
        elif st.session_state.step == 3:

            skills = st.session_state.skills

            for k,v in skills.items():
                st.markdown(f'<div class="glass">{generate_content(k,v)}</div>', unsafe_allow_html=True)

            if st.button("Tạo Tuyên ngôn"):
                st.session_state.step = 4
                st.rerun()

        # STEP 4
        elif st.session_state.step == 4:

            skills = st.session_state.skills
            dominant = max(skills, key=skills.get)

            manifesto = f"""
            Bạn được thiết kế để dẫn dắt bằng {dominant}.
            Khi khai thác triệt để năng lực này, bạn có thể tạo ra lợi thế chiến lược.
            Tương lai thuộc về những người hiểu rõ hồ sơ năng lực của mình.
            """

            st.markdown(f'<div class="glass">{manifesto}</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
