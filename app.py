# ==========================================================
# FUTURIO v3.2 – Epic Stability Fusion Edition
# Senior Streamlit Developer Build
# ==========================================================

import streamlit as st
import numpy as np
import plotly.graph_objects as go
import random
import time

# ==========================================================
# CONFIG
# ==========================================================

st.set_page_config(page_title="Futurio", page_icon="🚀", layout="wide")

# ==========================================================
# STATE INIT
# ==========================================================

def initialize_state():
    defaults = {
        "page": "home",
        "analysis_done": False,
        "skills": {},
        "manifesto": ""
    }
    for k,v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

# ==========================================================
# GLOBAL UI (EPIC STYLE)
# ==========================================================

def setup_ui():

    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&family=Playfair+Display:wght@600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Orbitron', sans-serif;
    }

    .stApp {
        background: radial-gradient(circle at 30% 20%, #0f172a, #020617);
        color: #FFFFFF;
        overflow-x: hidden;
    }

    /* SHOOTING STARS */
    .shooting-star {
        position: fixed;
        width: 2px;
        height: 80px;
        background: linear-gradient(-45deg, white, transparent);
        animation: shoot 6s linear infinite;
        opacity: 0.6;
    }

    @keyframes shoot {
        0% { transform: translateX(0) translateY(0) rotate(45deg); opacity: 1;}
        100% { transform: translateX(-800px) translateY(800px) rotate(45deg); opacity: 0;}
    }

    /* LOGO */
    .logo-circle {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        border: 2px solid #00f2ff;
        margin: auto;
        box-shadow: 0 0 30px #00f2ff;
        position: relative;
    }

    .logo-circle::after {
        content: "";
        position: absolute;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        border: 2px solid #7000ff;
        animation: pulse 2s infinite;
    }

    @keyframes pulse {
        0% { transform: scale(1); opacity: 1;}
        100% { transform: scale(1.3); opacity: 0;}
    }

    /* SLOGAN */
    .slogan {
        font-size: 34px;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(90deg,#00f2ff,#7000ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 25px rgba(0,242,255,0.8);
        margin-top: 20px;
    }

    .hero {
        text-align:center;
        margin-top:10px;
        color:#FFFFFF;
    }

    /* GLASS CARD */
    .glass {
        background: rgba(255,255,255,0.06);
        border-radius: 18px;
        padding: 28px;
        border: 1px solid rgba(255,255,255,0.15);
        box-shadow: 0 0 25px rgba(0,242,255,0.2);
        margin-bottom: 24px;
        color: #FFFFFF !important;
        font-weight: 500;
        text-shadow: 0 0 10px rgba(255,255,255,0.3);
        transition: all 0.3s ease;
    }

    .glass:hover {
        transform: translateY(-5px);
        box-shadow: 0 0 40px rgba(0,242,255,0.6);
    }

    /* MANIFESTO */
    .manifesto {
        font-family: 'Playfair Display', serif;
        border: 2px solid gold;
        box-shadow: 0 0 35px rgba(255,215,0,0.7);
    }

    /* SLIDER */
    .stSlider label {
        font-size: 18px !important;
        color: #00f2ff !important;
        font-weight: 700;
    }

    div[data-baseweb="slider"] span {
        background: linear-gradient(90deg,#7000ff,#00f2ff) !important;
    }

    div[data-baseweb="slider"] div[role="slider"] {
        background: #00f2ff !important;
        border: 2px solid white !important;
    }

    /* BUTTON */
    div.stButton > button {
        border-radius: 16px !important;
        background: linear-gradient(90deg,#7000ff,#00f2ff);
        color: white;
        font-weight: 600;
        padding: 12px 24px;
        box-shadow: 0 0 30px #00f2ff;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 50px #00f2ff;
    }

    /* RADAR LOADER */
    .radar-loader {
        border: 3px solid rgba(255,255,255,0.1);
        border-top: 3px solid #00f2ff;
        border-radius: 50%;
        width: 70px;
        height: 70px;
        animation: spin 1s linear infinite;
        margin: auto;
    }

    @keyframes spin {
        0% { transform: rotate(0deg);}
        100% { transform: rotate(360deg);}
    }

    </style>
    """, unsafe_allow_html=True)

    # Generate shooting stars
    for i in range(4):
        st.markdown(
            f'<div class="shooting-star" style="top:{random.randint(0,300)}px; right:{random.randint(0,600)}px;"></div>',
            unsafe_allow_html=True
        )

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
        fillcolor='rgba(0,242,255,0.35)',
        line_color='#00f2ff'
    ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0,5],
                                   gridcolor="rgba(200,200,200,0.3)")),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# MAIN
# ==========================================================

def main():
    initialize_state()
    setup_ui()

    # ================= HOME =================
    if st.session_state.page == "home":

        st.markdown('<div class="logo-circle"></div>', unsafe_allow_html=True)
        st.markdown('<div class="slogan">Futurio - See Your Future. Shape Your Path.</div>', unsafe_allow_html=True)
        st.markdown('<div class="hero">Khám phá tinh cầu năng lực của bạn thông qua thuật toán AI mô phỏng.</div>', unsafe_allow_html=True)

        st.image("https://upload.wikimedia.org/wikipedia/commons/3/3b/Flowchart_example.svg", use_column_width=True)

        with st.expander("📖 Hướng dẫn khai phá"):
            st.write("1️⃣ Chấm điểm năng lực qua Slider.")
            st.write("2️⃣ Nhấn AI Quét để kích hoạt mô phỏng.")
            st.write("3️⃣ Xem biểu đồ, phân tích và tuyên ngôn.")

        if st.button("🚀 Bắt đầu hành trình"):
            st.session_state.page = "assessment"
            st.rerun()

    # ================= ASSESSMENT =================
    elif st.session_state.page == "assessment":

        if st.button("⬅ Quay lại trang chủ"):
            st.session_state.page = "home"
            st.session_state.analysis_done = False
            st.rerun()

        skills = {
            "🧠 Logic": st.slider("Logic",0,5,3),
            "🎨 Sáng tạo": st.slider("Sáng tạo",0,5,3),
            "📊 Phân tích": st.slider("Phân tích",0,5,3),
            "📢 Giao tiếp": st.slider("Giao tiếp",0,5,3),
            "📁 Quản lý": st.slider("Quản lý",0,5,3)
        }

        if st.button("AI Quét Năng Lực"):
            loader = st.empty()
            loader.markdown('<div class="radar-loader"></div>', unsafe_allow_html=True)
            time.sleep(2)
            loader.empty()

            st.session_state.analysis_done = True
            st.session_state.skills = skills
            dominant = max(skills, key=skills.get)
            st.session_state.manifesto = f"""
            Bạn được thiết kế để dẫn dắt bằng {dominant}.
            Khi khai thác tối đa năng lực này, bạn có thể tạo ra lợi thế chiến lược dài hạn.
            Tương lai thuộc về những người hiểu rõ chính mình.
            """

        if st.session_state.analysis_done:

            tab1, tab2, tab3 = st.tabs(["📊 Biểu đồ", "🔮 Phân tích chi tiết", "📜 Tuyên ngôn"])

            with tab1:
                render_radar(st.session_state.skills)

            with tab2:
                for k,v in st.session_state.skills.items():
                    st.markdown(f'<div class="glass"><b>{k}</b> đạt {v}/5. Đây là yếu tố quan trọng ảnh hưởng đến chiến lược phát triển của bạn. Khi nâng cấp kỹ năng này, bạn sẽ mở rộng đáng kể cơ hội trong tương lai.</div>', unsafe_allow_html=True)

            with tab3:
                st.markdown(f'<div class="glass manifesto">{st.session_state.manifesto}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
