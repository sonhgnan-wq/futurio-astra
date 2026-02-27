# ==========================================================
# FUTURIO v3.9.6 – FINAL DIVERSITY EDITION
# ==========================================================

import streamlit as st
import plotly.graph_objects as go
import random
import time

# ==========================================================
# CONFIG & STATE
# ==========================================================

st.set_page_config(page_title="Futurio", page_icon="🚀", layout="wide")

if "page" not in st.session_state: st.session_state.page = "home"
if "analysis_done" not in st.session_state: st.session_state.analysis_done = False

# ==========================================================
# UI SYSTEM (FINAL COLOR SPECIFICATIONS)
# ==========================================================

def setup_ui():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Playfair+Display:ital,wght@1,600&display=swap');

    .stApp {
        background: radial-gradient(circle at center, #0f172a, #020617);
        color: #FFFFFF !important;
    }

    /* SAO RƠI */
    .shooting-star {
        position: fixed; width: 2px; height: 60px;
        background: linear-gradient(to bottom, #00f2ff, transparent);
        animation: shoot 5s linear infinite; opacity: 0.2; z-index: 0;
    }
    @keyframes shoot {
        0% { transform: translateY(-100px) translateX(0); opacity: 1; }
        100% { transform: translateY(100vh) translateX(200px); opacity: 0; }
    }

    /* CHỮ FUTURIO */
    .main-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 85px !important;
        font-weight: 900;
        color: #FFFFFF !important;
        text-shadow: 0 0 30px #00f2ff;
        text-align: center;
        margin-top: 10px;
    }

    /* POPOVER (LỢI ÍCH & HƯỚNG DẪN) - CHỮ XANH DƯƠNG, NỀN TRẮNG, NỘI DUNG ĐEN */
    div[data-testid="stPopover"] > button {
        background: linear-gradient(90deg, #7000ff, #00f2ff) !important;
        color: #00f2ff !important;
        border: none !important;
        border-radius: 20px !important;
        font-weight: bold !important;
    }

    div[data-testid="stPopoverBody"] {
        background-color: #FFFFFF !important;
        border: 2px solid #00f2ff !important;
    }
    
    div[data-testid="stPopoverBody"] p, 
    div[data-testid="stPopoverBody"] li, 
    div[data-testid="stPopoverBody"] strong,
    div[data-testid="stPopoverBody"] h3 {
        color: #000000 !important;
    }

    /* CHỮ TRONG TABS - MÀU TRẮNG */
    button[data-baseweb="tab"] p {
        color: #FFFFFF !important;
        font-family: 'Orbitron', sans-serif;
    }

    /* GLASS CARD */
    .glass {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 18px 25px;
        margin-bottom: 15px;
        color: #FFFFFF !important;
        backdrop-filter: blur(10px);
    }

    /* BUTTONS */
    div.stButton > button {
        background: linear-gradient(90deg, #7000ff, #00f2ff) !important;
        color: white !important;
        font-weight: bold;
        border-radius: 25px;
    }

    .manifesto-box {
        font-family: 'Playfair Display', serif;
        border: 1px solid #FFD700;
        background: rgba(255, 215, 0, 0.1);
        padding: 25px;
        color: #FFFFFF !important;
        text-align: center;
        font-size: 1.2rem;
    }

    .stSlider label { color: #00f2ff !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)
    for i in range(3):
        st.markdown(f'<div class="shooting-star" style="left:{random.randint(0,95)}%; animation-delay:{random.random()*5}s"></div>', unsafe_allow_html=True)

# ==========================================================
# DIVERSIFIED ENGINE (TRẢ LẠI TÍNH ĐA DẠNG)
# ==========================================================

def get_deep_analysis(skill, score):
    banks = {
        1: [f"Năng lực {skill} hiện chỉ là một đốm lửa nhỏ, cần sự đầu tư tái cấu trúc toàn diện để bắt kịp xu hướng.", 
            f"Vùng {skill} đang ở trạng thái sơ khai, đòi hỏi một lộ trình rèn luyện kỷ luật và nghiêm túc."],
        2: [f"Kỹ năng {skill} đã hình thành nhưng còn mỏng manh, cần thêm các dự án thực tế để rèn giũa bản lĩnh.",
            f"Bạn có tiềm năng về {skill}, nhưng hiện tại nó vẫn chưa thực sự tạo ra sức bật lớn."],
        3: [f"Năng lực {skill} đang vận hành ổn định, là bệ phóng sẵn sàng cho những cú hích chiến lược tiếp theo.",
            f"Tại ngưỡng {score}/5, {skill} đóng vai trò là một điểm tựa vững chắc trong hồ sơ của bạn."],
        4: [f"Thế mạnh {skill} của bạn cực kỳ ấn tượng, mang lại khả năng dẫn dắt và tầm ảnh hưởng sâu rộng.",
            f"Bạn đang làm chủ {skill} một cách điêu luyện, đây là vũ khí quan trọng để bạn bứt phá."],
        5: [f"Năng lực {skill} đã chạm ngưỡng bậc thầy, là biểu tượng cho thương hiệu cá nhân khác biệt của bạn.",
            f"Đỉnh cao {skill} cho cho phép bạn kiến tạo những giá trị mà số đông không thể thực hiện được."]
    }
    return random.choice(banks[score])

def get_manifesto(hi, lo):
    manifestos = [
        f"Sứ mệnh của bạn là lấy {hi} làm mũi nhọn bứt phá, đồng thời hoàn thiện {lo} để xây dựng một đế chế năng lực bền vững.",
        f"Khi {hi} trở thành ánh sáng dẫn đường, việc khắc phục {lo} sẽ là chìa khóa mở ra cánh cửa thành công vĩnh cửu.",
        f"Hãy để thế giới kinh ngạc trước sức mạnh của {hi}. Đừng quên rèn luyện {lo} để trở nên không thể bị đánh bại."
    ]
    return random.choice(manifestos)

# ==========================================================
# MAIN APP
# ==========================================================

setup_ui()

# --- NAVBAR ---
st.markdown('<div style="background: rgba(255,255,255,0.05); border-bottom: 1px solid rgba(0, 242, 255, 0.3); padding: 5px 0; margin-bottom: 15px;">', unsafe_allow_html=True)
nav_cols = st.columns([1, 1, 1, 1])
with nav_cols[0]:
    if st.button("🏠 Trang chủ", use_container_width=True):
        st.session_state.page = "home"; st.session_state.analysis_done = False; st.rerun()
with nav_cols[1]:
    with st.popover("🌟 Lợi ích", use_container_width=True):
        st.markdown("### Lợi ích chiến lược\n* **Định vị chính xác:** Khám phá trục năng lực cốt lõi.\n* **Tối ưu lộ trình:** Tập trung vào kỹ năng giá trị cao.\n* **Nhận diện điểm mù:** Cảnh báo sớm các thiếu hụt.")
with nav_cols[2]:
    with st.popover("📖 Hướng dẫn", use_container_width=True):
        st.markdown("### 3 Bước khai phá\n1. **Đánh giá:** Kéo Slider cho 5 nhóm năng lực.\n2. **Kích hoạt:** Nhấn 'AI Quét Năng Lực'.\n3. **Khám phá:** Xem Biểu đồ, Phân tích & Tuyên ngôn.")
with nav_cols[3]:
    st.markdown('<div style="text-align:right; color:#00f2ff; font-weight:bold; padding-top:8px; padding-right:15px;">v3.9.6 FINAL</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- PAGES ---
if st.session_state.page == "home":
    st.markdown('<div class="main-title">FUTURIO</div>', unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; margin-top:-10px; opacity:0.8;'>See Your Future. Shape Your Path.</h3>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""<div class="glass" style="text-align: center; max-width: 650px; margin: auto;">
        <p style="font-size:1.15rem; font-weight:500;">Hệ thống mô phỏng năng lực AI giúp bạn định vị bản sắc và kiến tạo tương lai sự nghiệp.</p>
    </div>""", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    _, btn_center, _ = st.columns([1.2, 1, 1.2])
    with btn_center:
        if st.button("🚀 BẮT ĐẦU HÀNH TRÌNH", use_container_width=True):
            st.session_state.page = "assessment"; st.rerun()

elif st.session_state.page == "assessment":
    st.markdown("<h2 style='text-align:center;'>🌌 ĐÁNH GIÁ NĂNG LỰC</h2>", unsafe_allow_html=True)
    skills = {}
    c1, c2 = st.columns(2)
    with c1:
        for s in ["🧠 Logic", "🎨 Sáng tạo", "📊 Phân tích"]:
            st.markdown('<div class="glass">', unsafe_allow_html=True)
            skills[s] = st.slider(s, 1, 5, 3); st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        for s in ["📢 Giao tiếp", "📁 Quản lý"]:
            st.markdown('<div class="glass">', unsafe_allow_html=True)
            skills[s] = st.slider(s, 1, 5, 3); st.markdown('</div>', unsafe_allow_html=True)
            
    if st.button("AI QUÉT NĂNG LỰC"):
        with st.spinner("Đang mô phỏng tinh cầu năng lực..."): time.sleep(1.2)
        st.session_state.skills = skills; st.session_state.analysis_done = True
        hi = max(skills, key=skills.get); lo = min(skills, key=skills.get)
        st.session_state.manifesto = get_manifesto(hi, lo)

    if st.session_state.analysis_done:
        tab1, tab2, tab3 = st.tabs(["📊 BIỂU ĐỒ", "🔮 PHÂN TÍCH", "📜 TUYÊN NGÔN"])
        with tab1:
            vals = list(st.session_state.skills.values())
            fig = go.Figure(go.Scatterpolar(r=vals + [vals[0]], theta=list(st.session_state.skills.keys()) + [list(st.session_state.skills.keys())[0]], fill='toself', fillcolor='rgba(0, 242, 255, 0.25)', line_color='#00f2ff'))
            fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])), paper_bgcolor="rgba(0,0,0,0)", font_color="white")
            st.plotly_chart(fig, use_container_width=True)
            
        with tab2:
            for k, v in st.session_state.skills.items():
                st.markdown(f'<div class="glass">{get_deep_analysis(k, v)}</div>', unsafe_allow_html=True)
        with tab3:
            st.markdown(f'<div class="glass manifesto-box">{st.session_state.manifesto}</div>', unsafe_allow_html=True)
