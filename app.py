# ==========================================================
# FUTURIO v3.0 – Epic Creative Edition
# Senior Creative Developer Build
# ==========================================================

import streamlit as st
import numpy as np
import random
import plotly.graph_objects as go
import time

# ==========================================================
# CONFIG
# ==========================================================

st.set_page_config(
    page_title="Futurio",
    page_icon="🚀",
    layout="wide"
)

# ==========================================================
# GLOBAL STYLES – EPIC UI SYSTEM
# ==========================================================

def setup_ui():

    st.markdown("""
    <style>

    /* ================= GOOGLE FONT ================= */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Orbitron', sans-serif;
    }

    /* ================= BACKGROUND ================= */
    .stApp {
        background: radial-gradient(circle at 30% 20%, #0f172a, #020617);
        color: #F8FAFC;
        overflow-x: hidden;
    }

    /* Shooting stars animation */
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

    /* ================= CENTER CONTAINER ================= */
    .main-container {
        max-width: 950px;
        margin: auto;
    }

    /* ================= LOGO ANIMATION ================= */
    .logo-circle {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        border: 2px solid #00f2ff;
        position: relative;
        margin: auto;
        box-shadow: 0 0 25px #00f2ff;
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

    /* ================= SLOGAN ================= */
    .slogan {
        font-size: 34px;
        text-align: center;
        font-weight: 700;
        background: linear-gradient(90deg,#00f2ff,#7000ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 20px rgba(0,242,255,0.6);
        margin-top: 20px;
    }

    .hero-text {
        text-align: center;
        font-size: 16px;
        margin-top: 10px;
        color: #F8FAFC;
    }

    /* ================= GLASS CARD ================= */
    .glass {
        background: rgba(255,255,255,0.06);
        border-radius: 18px;
        padding: 26px;
        border: 1px solid rgba(255,255,255,0.15);
        box-shadow: 0 0 25px rgba(0,242,255,0.2);
        margin-bottom: 24px;
        color: #FFFFFF;
        text-shadow: 0px 2px 4px rgba(0,0,0,0.5);
    }

    /* ================= SLIDER ================= */
    .stSlider label {
        color: #00f2ff !important;
        font-weight: bold;
    }

    div[data-baseweb="slider"] span {
        background: linear-gradient(90deg,#7000ff,#00f2ff) !important;
    }

    div[data-baseweb="slider"] div[role="slider"] {
        background: #00f2ff !important;
        border: 2px solid white !important;
    }

    /* ================= BUTTON ================= */
    div.stButton > button {
        border-radius: 16px !important;
        background: linear-gradient(90deg,#7000ff,#00f2ff);
        color: white;
        font-weight: 600;
        padding: 12px 24px;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        transform: scale(1.05);
        opacity: 0.9;
    }

    /* ================= SCENARIO COLORS ================= */
    .card-blue { background: rgba(0,120,255,0.2); }
    .card-purple { background: rgba(112,0,255,0.25); }
    .card-orange { background: rgba(255,165,0,0.25); }

    /* ================= RADAR LOADER ================= */
    .radar-loader {
        border: 3px solid rgba(255,255,255,0.1);
        border-top: 3px solid #00f2ff;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        animation: spin 1s linear infinite;
        margin: auto;
    }

    @keyframes spin {
        0% { transform: rotate(0deg);}
        100% { transform: rotate(360deg);}
    }

    </style>
    """, unsafe_allow_html=True)

    # Shooting star instances
    for i in range(3):
        st.markdown(f'<div class="shooting-star" style="top:{random.randint(0,300)}px; right:{random.randint(0,500)}px;"></div>', unsafe_allow_html=True)

# ==========================================================
# CONTENT ENGINE v3
# ==========================================================

def generate_content(skill, score):

    if score >= 4:
        return f"""
        <div class="glass">
        <b>{skill} đang ở trạng thái đỉnh cao.</b><br><br>
        Năng lực này có thể trở thành trục chiến lược trong hồ sơ nghề nghiệp của bạn.
        Nếu tiếp tục đầu tư, bạn có thể mở rộng ảnh hưởng và đạt cấp độ chuyên gia.<br><br>
        👉 Lời khuyên vàng: Xây dựng dự án thực tế xoay quanh {skill}.
        </div>
        """
    elif score >= 2:
        return f"""
        <div class="glass">
        <b>{skill} đang ở mức ổn định.</b><br><br>
        Đây là nền tảng tốt để phát triển sâu hơn trong tương lai.
        Việc nâng cấp kỹ năng này sẽ giúp bạn tăng biên độ lựa chọn ngành nghề.<br><br>
        👉 Lời khuyên vàng: Đầu tư 30 phút mỗi ngày để rèn luyện {skill}.
        </div>
        """
    else:
        return f"""
        <div class="glass">
        <b>{skill} là vùng tiềm năng chưa khai phá.</b><br><br>
        Việc cải thiện năng lực này sẽ giúp bạn mở rộng đáng kể cơ hội.
        Đây có thể là chìa khóa để chuyển hướng chiến lược sự nghiệp.<br><br>
        👉 Lời khuyên vàng: Tham gia khóa học nền tảng về {skill}.
        </div>
        """

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
# MAIN APP
# ==========================================================

def main():

    setup_ui()

    if "page" not in st.session_state:
        st.session_state.page = "home"

    # ================= HOME =================
    if st.session_state.page == "home":

        st.markdown('<div class="main-container">', unsafe_allow_html=True)

        st.markdown('<div class="logo-circle"></div>', unsafe_allow_html=True)
        st.markdown('<div class="slogan">Futurio - See Your Future. Shape Your Path.</div>', unsafe_allow_html=True)
        st.markdown('<div class="hero-text">Khám phá tinh cầu năng lực của bạn thông qua thuật toán AI mô phỏng.</div>', unsafe_allow_html=True)

        with st.expander("📖 Hướng dẫn khai phá"):
            st.write("1️⃣ Chấm điểm năng lực bằng các Slider.")
            st.write("2️⃣ Nhấn phân tích để AI quét dữ liệu.")
            st.write("3️⃣ Nhận chiến lược và Tuyên ngôn tương lai.")

        if st.button("🚀 Bắt đầu hành trình"):
            st.session_state.page = "assessment"
            st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

    # ================= ASSESSMENT =================
    elif st.session_state.page == "assessment":

        st.markdown('<div class="main-container">', unsafe_allow_html=True)

        skills = {}
        skills["🧠 Logic"] = st.slider("Logic",0,5,3)
        skills["🎨 Sáng tạo"] = st.slider("Sáng tạo",0,5,3)
        skills["📊 Phân tích"] = st.slider("Phân tích",0,5,3)
        skills["📢 Giao tiếp"] = st.slider("Giao tiếp",0,5,3)
        skills["📁 Quản lý"] = st.slider("Quản lý",0,5,3)

        if st.button("AI Quét Năng Lực"):

            st.markdown('<div class="radar-loader"></div>', unsafe_allow_html=True)
            time.sleep(2)

            render_radar({k: v for k, v in skills.items()})

            col1, col2, col3 = st.columns(3)

            col1.markdown(f'<div class="glass card-blue">Hiện tại</div>', unsafe_allow_html=True)
            col2.markdown(f'<div class="glass card-purple">Power Up</div>', unsafe_allow_html=True)
            col3.markdown(f'<div class="glass card-orange">Pivot</div>', unsafe_allow_html=True)

            for k,v in skills.items():
                st.markdown(generate_content(k,v), unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
