# ==========================================================
# FUTURIO v3.1 – Stable UX & Premium Edition
# Senior Streamlit Developer Build
# ==========================================================

import streamlit as st
import numpy as np
import random
import plotly.graph_objects as go
import time

# ==========================================================
# CONFIG
# ==========================================================

st.set_page_config(page_title="Futurio", page_icon="🚀", layout="wide")

# ==========================================================
# STATE INITIALIZER (Fix lỗi trống rỗng)
# ==========================================================

def initialize_state():
    defaults = {
        "page": "home",
        "analysis_done": False,
        "skills": {},
        "manifesto": ""
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

# ==========================================================
# GLOBAL CSS
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
    }

    /* Slide-up animation */
    .slide-up {
        animation: slideUp 1.2s ease forwards;
        opacity: 0;
        transform: translateY(40px);
    }

    @keyframes slideUp {
        to { opacity: 1; transform: translateY(0);}
    }

    /* Glass Card */
    .glass {
        background: rgba(255,255,255,0.06);
        border-radius: 18px;
        padding: 28px;
        border: 1px solid rgba(255,255,255,0.15);
        box-shadow: 0 0 30px rgba(0,242,255,0.25);
        margin-bottom: 24px;
        color: #FFFFFF !important;
        font-weight: 500;
        text-shadow: 0 0 10px rgba(255,255,255,0.3);
    }

    /* Gold Manifesto */
    .manifesto {
        font-family: 'Playfair Display', serif;
        border: 2px solid gold;
        box-shadow: 0 0 30px rgba(255,215,0,0.6);
    }

    /* Slider label */
    .stSlider label {
        font-size: 18px !important;
        color: #00f2ff !important;
        font-weight: 700;
    }

    /* Button glow */
    div.stButton > button {
        border-radius: 16px !important;
        background: linear-gradient(90deg,#7000ff,#00f2ff);
        color: white;
        font-weight: 600;
        padding: 12px 24px;
        box-shadow: 0 0 25px #00f2ff;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 45px #00f2ff;
    }

    </style>
    """, unsafe_allow_html=True)

# ==========================================================
# CONTENT ENGINE v3 (Phong phú hơn)
# ==========================================================

def generate_content(skill, score):

    base_analysis = f"<b>{skill}</b> đang ở mức {score}/5."

    if score >= 4:
        detail = """
        Đây là năng lực nổi bật có thể trở thành trục chiến lược.
        Nếu được đầu tư bài bản, bạn có thể xây dựng lợi thế cạnh tranh dài hạn.
        Trong môi trường phù hợp, kỹ năng này giúp bạn dẫn dắt và tạo ảnh hưởng.
        """
    elif score >= 2:
        detail = """
        Đây là nền tảng tốt nhưng vẫn còn không gian nâng cấp.
        Khi được cải thiện thêm 1-2 cấp độ, cơ hội ngành nghề sẽ mở rộng đáng kể.
        Việc luyện tập đều đặn sẽ tạo ra bước tiến rõ rệt trong 6–12 tháng.
        """
    else:
        detail = """
        Đây là vùng tiềm năng cần được khai phá.
        Việc cải thiện kỹ năng này có thể thay đổi hoàn toàn chiến lược nghề nghiệp.
        Bạn nên bắt đầu từ các khóa học nền tảng và dự án nhỏ thực tế.
        """

    return f"""
    <div class="glass">
    {base_analysis}<br><br>
    {detail}
    </div>
    """

# ==========================================================
# RADAR
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
        polar=dict(radialaxis=dict(visible=True, range=[0,5])),
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

        st.markdown('<h1 class="slide-up" style="text-align:center;">Futurio - See Your Future. Shape Your Path.</h1>', unsafe_allow_html=True)
        st.markdown('<p style="text-align:center;">Khám phá tinh cầu năng lực của bạn thông qua thuật toán AI mô phỏng.</p>', unsafe_allow_html=True)

        if st.button("🚀 Bắt đầu"):
            st.session_state.page = "assessment"
            st.rerun()

    # ================= ASSESSMENT =================
    elif st.session_state.page == "assessment":

        col_back, col_space = st.columns([1,6])
        with col_back:
            if st.button("⬅ Quay lại"):
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
            loader.markdown('<div class="glass" style="text-align:center;">🔄 AI đang quét dữ liệu...</div>', unsafe_allow_html=True)
            time.sleep(2)
            loader.empty()

            st.session_state.analysis_done = True
            st.session_state.skills = skills

            dominant = max(skills, key=skills.get)
            st.session_state.manifesto = f"""
            Bạn được thiết kế để dẫn dắt bằng {dominant}.
            Khi khai thác triệt để năng lực này, bạn có thể tạo lợi thế chiến lược bền vững.
            Tương lai thuộc về những người hiểu rõ chính mình.
            """

        # Hiển thị kết quả nếu đã phân tích
        if st.session_state.analysis_done:

            tab1, tab2, tab3 = st.tabs(["📊 Biểu đồ", "🔮 Phân tích chi tiết", "📜 Tuyên ngôn"])

            with tab1:
                render_radar(st.session_state.skills)

            with tab2:
                for k,v in st.session_state.skills.items():
                    st.markdown(generate_content(k,v), unsafe_allow_html=True)

            with tab3:
                st.markdown(f'<div class="glass manifesto">{st.session_state.manifesto}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
