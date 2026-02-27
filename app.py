# =========================================================
# FUTURIO ASTRA v3.2 – UI RESTORED EDITION
# Senior UI/UX + Streamlit Expert
# =========================================================

import streamlit as st
import plotly.graph_objects as go
import random
import time

st.set_page_config(
    page_title="Futurio Astra",
    page_icon="✨",
    layout="centered"
)

# =========================================================
# STATE MANAGEMENT
# =========================================================

def initialize_state():
    defaults = {
        "page": "home",
        "analysis_done": False,
        "skills": {},
        "manifesto": ""
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

# =========================================================
# UI & CSS (v3.2 STYLE RESTORED)
# =========================================================

def setup_ui():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800&family=Playfair+Display:ital@1&display=swap');

    body {
        background: radial-gradient(circle at top, #0f172a, #020617);
        color: #ffffff;
    }

    /* ===== STAR BACKGROUND ===== */
    .shooting-star {
        position: fixed;
        top: -10px;
        width: 2px;
        height: 80px;
        background: linear-gradient(white, rgba(255,255,255,0));
        animation: shoot 3s linear infinite;
        opacity: 0.4;
    }

    @keyframes shoot {
        from { transform: translateY(0) translateX(0); }
        to { transform: translateY(120vh) translateX(300px); }
    }

    /* ===== NAVBAR ===== */
    .navbar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background: transparent;
        padding: 12px 30px;
        z-index: 1000;
        display: flex;
        justify-content: space-between;
    }

    .nav-btn {
        font-size: 14px;
        color: #ffffff;
        background: rgba(255,255,255,0.05);
        border-radius: 12px;
        padding: 6px 14px;
        border: 1px solid rgba(255,255,255,0.15);
    }

    /* ===== LOGO ===== */
    .logo-circle {
        width: 42px;
        height: 42px;
        border-radius: 50%;
        border: 2px solid #00f2ff;
        box-shadow: 0 0 15px #00f2ff;
    }

    /* ===== GLASS CARD ===== */
    .glass {
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 18px;
        padding: 20px;
        margin-bottom: 18px;
        transition: 0.3s ease;
        text-shadow: 0 0 10px rgba(255,255,255,0.3);
    }

    .glass:hover {
        transform: translateY(-5px);
        box-shadow: 0 0 25px rgba(0,242,255,0.4);
    }

    /* ===== TEXT ===== */
    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif;
        text-shadow: 0 0 12px rgba(0,242,255,0.6);
    }

    .manifesto {
        font-family: 'Playfair Display', serif;
        font-size: 18px;
        border: 1px solid gold;
        box-shadow: 0 0 20px rgba(255,215,0,0.6);
    }

    /* ===== SLIDER ===== */
    .stSlider label {
        font-size: 18px !important;
        color: #00f2ff !important;
        font-weight: 600;
    }

    div[data-baseweb="slider"] span {
        background: linear-gradient(90deg,#7000ff,#00f2ff) !important;
    }

    </style>
    """, unsafe_allow_html=True)

    # Shooting stars
    for i in range(5):
        st.markdown(f"<div class='shooting-star' style='left:{random.randint(0,100)}%; animation-delay:{random.random()*3}s'></div>", unsafe_allow_html=True)

# =========================================================
# NAVBAR
# =========================================================

def navbar():
    st.markdown("""
    <div class="navbar">
        <div class="logo-circle"></div>
        <div>
            <span class="nav-btn">🏠 Trang chủ</span>
            <span class="nav-btn">🌟 Tính năng</span>
            <span class="nav-btn">📖 Hướng dẫn</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# CONTENT ENGINE
# =========================================================

analysis_bank = {
    1: ["đang ở mức nền tảng, cần tái cấu trúc toàn diện."],
    2: ["đang phát triển nhưng thiếu sự ổn định chiến lược."],
    3: ["đang ở vùng ổn định, sẵn sàng cho cú bứt phá lớn."],
    4: ["là lợi thế rõ ràng, có thể tạo khác biệt."],
    5: ["là năng lực mũi nhọn mang tính định danh cá nhân."]
}

def get_analysis(skill, score):
    return f"Năng lực **{skill}** {random.choice(analysis_bank[score])}"

# =========================================================
# RADAR
# =========================================================

def radar_chart(skills):
    labels = list(skills.keys())
    values = list(skills.values()) + [list(skills.values())[0]]

    fig = go.Figure(go.Scatterpolar(
        r=values,
        theta=labels + [labels[0]],
        fill='toself',
        fillcolor='rgba(0,242,255,0.35)',
        line_color='#00f2ff'
    ))

    fig.update_layout(
        polar=dict(radialaxis=dict(range=[0,5])),
        paper_bgcolor="rgba(0,0,0,0)",
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# MAIN
# =========================================================

def main():
    initialize_state()
    setup_ui()
    navbar()

    st.markdown("<br><br>", unsafe_allow_html=True)

    if st.session_state.page == "home":

        st.markdown("<h1 align='center'>Futurio</h1>", unsafe_allow_html=True)
        st.markdown("<h3 align='center'>See Your Future. Shape Your Path.</h3>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("🚀 Bắt đầu hành trình"):
            st.session_state.page = "assessment"
            st.rerun()

    elif st.session_state.page == "assessment":

        st.markdown("## 🌌 Đánh giá năng lực")

        skills = {}
        for s in ["Logic", "Sáng tạo", "Phân tích", "Giao tiếp", "Quản lý"]:
            with st.container():
                st.markdown("<div class='glass'>", unsafe_allow_html=True)
                skills[s] = st.slider(s, 1, 5, 3)
                st.markdown("</div>", unsafe_allow_html=True)

        if st.button("🧠 AI Quét Năng Lực"):
            loader = st.empty()
            loader.markdown("<div class='glass'>🔄 AI đang mô phỏng tương lai...</div>", unsafe_allow_html=True)
            time.sleep(2)
            loader.empty()

            st.session_state.skills = skills
            st.session_state.analysis_done = True

            hi = max(skills, key=skills.get)
            lo = min(skills, key=skills.get)
            st.session_state.manifesto = f"""
            Sứ mệnh của bạn là sử dụng **{hi}** làm trụ cột phát triển,
            đồng thời nâng cấp **{lo}** để tạo nên sự cân bằng chiến lược.
            """

        if st.session_state.analysis_done:
            tabs = st.tabs(["📊 Biểu đồ", "🔮 Phân tích", "📜 Tuyên ngôn"])

            with tabs[0]:
                radar_chart(st.session_state.skills)

            with tabs[1]:
                for k,v in st.session_state.skills.items():
                    st.markdown(f"<div class='glass'>{get_analysis(k,v)}</div>", unsafe_allow_html=True)

            with tabs[2]:
                st.markdown(f"<div class='glass manifesto'>{st.session_state.manifesto}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
