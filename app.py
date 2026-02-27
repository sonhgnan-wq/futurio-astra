import streamlit as st
import random
import time
import plotly.graph_objects as go

# =============================
# CONFIG
# =============================
st.set_page_config(
    page_title="Futurio - See Your Future",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =============================
# STATE
# =============================
def initialize_state():
    if "page" not in st.session_state:
        st.session_state.page = "home"
    if "analysis_done" not in st.session_state:
        st.session_state.analysis_done = False
    if "scores" not in st.session_state:
        st.session_state.scores = {}

initialize_state()

# =============================
# UI SETUP
# =============================
def setup_ui():
    st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Playfair+Display:ital@1&display=swap" rel="stylesheet">

<style>

/* GLOBAL */
html, body, [class*="css"] {
    font-family: sans-serif;
    background: radial-gradient(circle at center, #0f172a 0%, #020617 100%);
    color: #FFFFFF !important;
}

h1, h2, h3 {
    font-family: 'Orbitron', sans-serif;
    color: #FFFFFF !important;
    text-shadow: 0 0 10px rgba(0,242,255,0.5);
}

/* NAVBAR */
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    padding: 15px 40px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: transparent;
    z-index: 999;
}

.logo-circle {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    border: 2px solid #00f2ff;
    box-shadow: 0 0 20px #00f2ff;
    position: relative;
}

.logo-circle::after {
    content: "";
    position: absolute;
    top: 8px;
    left: 8px;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    border: 2px solid #9333ea;
    box-shadow: 0 0 10px #9333ea;
}

/* GLASS CARD */
.glass {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 20px;
    backdrop-filter: blur(10px);
    transition: 0.3s ease;
}

.glass:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 20px rgba(0,242,255,0.4);
}

/* MANIFESTO */
.manifesto {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    border: 2px solid gold;
    padding: 25px;
    border-radius: 15px;
    background: rgba(255,215,0,0.05);
    box-shadow: 0 0 15px gold;
}

/* SHOOTING STAR */
.shooting-star {
    position: fixed;
    width: 2px;
    height: 80px;
    background: linear-gradient(-45deg, white, rgba(255,255,255,0));
    animation: shoot 5s linear infinite;
    opacity: 0.6;
}

@keyframes shoot {
    0% { transform: translateX(0) translateY(0); opacity:1;}
    100% { transform: translateX(-1000px) translateY(600px); opacity:0;}
}

</style>
""", unsafe_allow_html=True)

    # Shooting stars
    for _ in range(5):
        left = random.randint(0, 100)
        delay = random.uniform(0, 5)
        st.markdown(
            f'<div class="shooting-star" style="top:0%; left:{left}%; animation-delay:{delay}s;"></div>',
            unsafe_allow_html=True
        )

setup_ui()

# =============================
# ANALYSIS BANK
# =============================
analysis_bank = {
    1: [
        "Năng lực này đang ở mức khởi đầu, bạn cần đầu tư nghiêm túc.",
        "Đây là vùng tiềm năng chưa được khai phá.",
        "Bạn nên tập trung cải thiện kỹ năng này sớm.",
        "Kỹ năng này đang hạn chế sự phát triển tổng thể."
    ],
    2: [
        "Bạn đã có nền tảng cơ bản nhưng chưa ổn định.",
        "Kỹ năng này cần thêm thực hành thực tế.",
        "Có tiềm năng phát triển nếu được rèn luyện đúng cách.",
        "Đây là giai đoạn củng cố và mở rộng."
    ],
    3: [
        "Mức ổn định, sẵn sàng cho bứt phá.",
        "Bạn đang vận hành khá tốt kỹ năng này.",
        "Đây là nền tảng vững cho bước tiến tiếp theo.",
        "Chỉ cần thêm trải nghiệm để hoàn thiện."
    ],
    4: [
        "Bạn thể hiện năng lực vượt trội ở đây.",
        "Đây là lợi thế cạnh tranh rõ rệt của bạn.",
        "Bạn có thể tận dụng kỹ năng này làm đòn bẩy.",
        "Mức cao, gần đạt chuyên sâu."
    ],
    5: [
        "Đây là siêu năng lực nổi bật của bạn.",
        "Kỹ năng này định hình bản sắc cá nhân.",
        "Bạn đạt mức xuất sắc hiếm thấy.",
        "Đây là trụ cột phát triển sự nghiệp."
    ]
}

def get_deep_analysis(skill, score):
    return random.choice(analysis_bank[score])

# =============================
# HOME
# =============================
if st.session_state.page == "home":

    st.markdown("<div style='height:100px'></div>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align:center;'>Futurio</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>See Your Future. Shape Your Path.</h3>", unsafe_allow_html=True)

    st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        if st.button("🚀 Bắt đầu", use_container_width=True):
            st.session_state.page = "assessment"

# =============================
# ASSESSMENT
# =============================
elif st.session_state.page == "assessment":

    st.markdown("## Đánh giá năng lực")

    skills = ["Tư duy chiến lược", "Sáng tạo", "Kỷ luật", "Giao tiếp", "Thích nghi"]

    scores = {}

    for skill in skills:
        st.markdown("<div class='glass'>", unsafe_allow_html=True)
        scores[skill] = st.slider(skill, 1, 5, 3)
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("AI Quét Năng Lực"):
        placeholder = st.empty()
        with placeholder:
            st.markdown("<h2 style='text-align:center;'>🔄 Đang phân tích...</h2>", unsafe_allow_html=True)
        time.sleep(2)
        placeholder.empty()

        st.session_state.scores = scores
        st.session_state.analysis_done = True

    if st.session_state.analysis_done:

        tab1, tab2, tab3 = st.tabs(["📊 Biểu đồ", "🔮 Phân tích", "📜 Tuyên ngôn"])

        with tab1:
            fig = go.Figure()
            fig.add_trace(go.Scatterpolar(
                r=list(st.session_state.scores.values()),
                theta=list(st.session_state.scores.keys()),
                fill='toself',
                fillcolor='rgba(0,242,255,0.3)',
                line=dict(color='#00f2ff')
            ))
            fig.update_layout(
                polar=dict(bgcolor="rgba(0,0,0,0)"),
                paper_bgcolor="rgba(0,0,0,0)",
                font=dict(color="white")
            )
            st.plotly_chart(fig, use_container_width=True)

        with tab2:
            for skill, score in st.session_state.scores.items():
                st.markdown("<div class='glass'>", unsafe_allow_html=True)
                st.markdown(f"### {skill}")
                st.write(get_deep_analysis(skill, score))
                st.markdown("</div>", unsafe_allow_html=True)

        with tab3:
            highest = max(st.session_state.scores, key=st.session_state.scores.get)
            lowest = min(st.session_state.scores, key=st.session_state.scores.get)

            st.markdown("<div class='manifesto'>", unsafe_allow_html=True)
            st.write(f"Sứ mệnh của bạn là lấy {highest} làm đòn bẩy để khắc phục {lowest}, từ đó tạo nên một phiên bản cân bằng và bứt phá.")
            st.markdown("</div>", unsafe_allow_html=True)

    if st.button("🏠 Trang chủ"):
        st.session_state.page = "home"
        st.session_state.analysis_done = False
