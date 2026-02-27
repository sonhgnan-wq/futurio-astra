# ==========================================================
# FUTURIO v3.5 – THE FINAL EVOLUTION
# Senior Creative Developer & UI/UX Expert Edition
# ==========================================================

import streamlit as st
import plotly.graph_objects as go
import random
import time

st.set_page_config(page_title="Futurio v3.5", page_icon="🚀", layout="wide")

# ==========================================================
# STATE MANAGEMENT
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
# GLOBAL UI
# ==========================================================

def setup_ui():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Orbitron', sans-serif;
        color: #FFFFFF;
    }

    .stApp {
        background: radial-gradient(circle at 20% 20%, #0f172a, #020617);
    }

    /* ===== NAVBAR ===== */
    .navbar {
        background: rgba(255,255,255,0.05);
        padding: 10px 20px;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        margin-bottom: 20px;
    }

    /* ===== LOGO TRIANGLE ===== */
    .logo-triangle {
        width: 0;
        height: 0;
        border-left: 25px solid transparent;
        border-right: 25px solid transparent;
        border-bottom: 45px solid #00f2ff;
        margin-right: 15px;
        filter: drop-shadow(0 0 10px #00f2ff);
    }

    .title-glow {
        text-shadow: 0 0 10px rgba(0,242,255,0.5);
    }

    /* ===== GLASS CARD ===== */
    .glass {
        background: rgba(255,255,255,0.06);
        padding: 20px;
        border-radius: 18px;
        border: 1px solid rgba(255,255,255,0.15);
        margin-bottom: 20px;
        transition: 0.3s;
    }

    .glass:hover {
        transform: translateY(-5px);
        box-shadow: 0 0 25px rgba(0,242,255,0.5);
    }

    /* ===== SCORE BORDER STATES ===== */
    .low-score { border: 1px solid rgba(255,0,0,0.5); }
    .high-score { border: 1px solid rgba(0,255,100,0.8); }

    /* ===== SLIDER ===== */
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

    /* ===== BUTTON ===== */
    div.stButton > button {
        border-radius: 12px !important;
        background: linear-gradient(90deg,#7000ff,#00f2ff);
        box-shadow: 0 0 20px #00f2ff;
        font-weight: 600;
    }

    </style>
    """, unsafe_allow_html=True)

# ==========================================================
# NAVIGATION BAR
# ==========================================================

def navbar():
    col1, col2, col3, col4 = st.columns([1,2,2,1])

    with col1:
        st.markdown('<div class="logo-triangle"></div>', unsafe_allow_html=True)

    with col2:
        if st.button("🏠 Trang chủ"):
            st.session_state.page = "home"
            st.session_state.analysis_done = False
            st.rerun()

    with col3:
        with st.popover("🌟 Tại sao chọn Futurio?"):
            st.markdown("**Tính năng:** Phân tích đa chiều, mô phỏng 3 kịch bản, tuyên ngôn cá nhân.")
            st.markdown("**Lợi ích:** Định hướng chính xác, khám phá tiềm năng ẩn, tối ưu lộ trình học tập.")

    with col4:
        with st.popover("📖 Hướng dẫn nhanh"):
            st.markdown("1️⃣ Chấm điểm năng lực.")
            st.markdown("2️⃣ Nhấn AI Quét.")
            st.markdown("3️⃣ Xem kết quả & tuyên ngôn.")

# ==========================================================
# CONTENT ENGINE
# ==========================================================

analysis_bank = {
    1: ["đang ở mức nền tảng, cần đầu tư nghiêm túc.",
        "cần được xây dựng lại từ gốc.",
        "chưa khai thác đúng tiềm năng.",
        "đòi hỏi sự rèn luyện có chiến lược."],

    2: ["đang phát triển nhưng chưa ổn định.",
        "có dấu hiệu tiến bộ rõ rệt.",
        "cần môi trường thực hành nhiều hơn.",
        "nên tham gia dự án thực tế để tăng tốc."],

    3: ["đang ở ngưỡng ổn định, sẵn sàng bứt phá.",
        "vận hành khá tốt, cần hoàn thiện thêm.",
        "có thể trở thành lợi thế nếu nâng cấp.",
        "đang giữ vai trò nền tảng trong hồ sơ năng lực."],

    4: ["đang nổi bật và tạo ưu thế cạnh tranh.",
        "là điểm sáng trong hồ sơ của bạn.",
        "mang lại khả năng dẫn dắt.",
        "có thể mở ra cơ hội lớn nếu khai thác sâu."],

    5: ["ở cấp độ xuất sắc, tiệm cận chuyên gia.",
        "là năng lực mũi nhọn chiến lược.",
        "giúp bạn tạo ảnh hưởng mạnh mẽ.",
        "có thể trở thành thương hiệu cá nhân."]
}

def get_deep_analysis(skill, score):
    text = random.choice(analysis_bank[score])
    return f"Năng lực {skill} {text}"

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
        fillcolor='rgba(0,242,255,0.35)',
        line_color='#00f2ff'
    ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0,5])),
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# MAIN
# ==========================================================

def main():
    initialize_state()
    setup_ui()
    navbar()

    if st.session_state.page == "home":

        st.markdown("<h1 class='title-glow'>Futurio - See Your Future. Shape Your Path.</h1>", unsafe_allow_html=True)

        st.markdown("### Trước khi dùng Futurio vs Sau khi dùng Futurio")
        st.table({
            "Trước": ["Mơ hồ", "Không rõ thế mạnh", "Chọn ngành theo cảm tính"],
            "Sau": ["Tự tin 100%", "Hiểu rõ năng lực", "Chiến lược rõ ràng"]
        })

        if st.button("🚀 Bắt đầu phân tích"):
            st.session_state.page = "assessment"
            st.rerun()

    elif st.session_state.page == "assessment":

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<div class='glass'>", unsafe_allow_html=True)
            skills = {
                "Logic": st.slider("Logic",1,5,3),
                "Sáng tạo": st.slider("Sáng tạo",1,5,3),
                "Phân tích": st.slider("Phân tích",1,5,3),
                "Giao tiếp": st.slider("Giao tiếp",1,5,3),
                "Quản lý": st.slider("Quản lý",1,5,3)
            }
            st.markdown("</div>", unsafe_allow_html=True)

            if st.button("AI Quét Năng Lực"):
                loader = st.empty()
                loader.markdown("<div class='glass'>🔄 Đang mô phỏng AI...</div>", unsafe_allow_html=True)
                time.sleep(2)
                loader.empty()

                st.session_state.analysis_done = True
                st.session_state.skills = skills

                highest = max(skills, key=skills.get)
                lowest = min(skills, key=skills.get)
                st.session_state.manifesto = f"""
                Sứ mệnh của bạn là dùng {highest} làm mũi nhọn,
                đồng thời cải thiện {lowest} để tạo sự cân bằng chiến lược.
                Khi hai yếu tố này hòa hợp, bạn sẽ đạt bước nhảy vọt.
                """

        if st.session_state.analysis_done:

            colA, colB = st.columns([1,1])

            with colA:
                render_radar(st.session_state.skills)

            with colB:
                for k,v in st.session_state.skills.items():
                    border_class = "high-score" if v >=4 else "low-score" if v<=2 else ""
                    st.markdown(f"<div class='glass {border_class}'>{get_deep_analysis(k,v)}</div>", unsafe_allow_html=True)

            st.markdown("<h2 class='title-glow'>📜 Tuyên ngôn Sứ mệnh</h2>", unsafe_allow_html=True)
            st.markdown(f"<div class='glass'>{st.session_state.manifesto}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
