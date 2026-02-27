# ==========================================================
# FUTURIO v3.8 – ULTIMATE COMPACT EDITION
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
# UI SYSTEM (MAX CONTRAST & COMPACT)
# ==========================================================

def setup_ui():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Playfair+Display:ital,wght@1,600&display=swap');

    .stApp {
        background: radial-gradient(circle at center, #0f172a, #020617);
        color: #FFFFFF !important;
    }

    /* NAVBAR SIÊU GỌN */
    .nav-bar {
        background: rgba(255, 255, 255, 0.05);
        border-bottom: 1px solid rgba(0, 242, 255, 0.3);
        padding: 5px 0;
        margin-bottom: 10px;
    }

    /* CHỮ FUTURIO TO & RÕ */
    .main-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 80px !important;
        font-weight: 900;
        color: #FFFFFF !important;
        text-shadow: 0 0 20px #00f2ff;
        text-align: center;
        margin-bottom: 0px;
    }

    /* FIX LỖI MÀU TRONG POPOVER */
    div[data-testid="stPopoverBody"] {
        background-color: #0f172a !important;
        color: #FFFFFF !important;
        border: 1px solid #00f2ff;
    }
    div[data-testid="stPopoverBody"] p, div[data-testid="stPopoverBody"] span {
        color: #FFFFFF !important;
    }

    /* GLASS CARD V3.2 */
    .glass {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 15px 25px;
        margin-bottom: 15px;
        color: #FFFFFF !important;
        backdrop-filter: blur(10px);
    }

    /* NÚT BẮT ĐẦU GỌN GÀNG */
    div.stButton > button {
        background: linear-gradient(90deg, #7000ff, #00f2ff) !important;
        color: white !important;
        font-weight: bold;
        border-radius: 25px;
        padding: 10px 40px !important;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.4);
    }

    /* MANIFESTO GOLD */
    .manifesto-box {
        font-family: 'Playfair Display', serif;
        border: 1px solid #FFD700;
        background: rgba(255, 215, 0, 0.05);
        padding: 20px;
        text-align: center;
        font-size: 1.2rem;
    }

    .stSlider label { color: #00f2ff !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================================
# DIVERSIFIED ANALYSIS BANK (TRẢ LẠI PHẦN ĐA DẠNG)
# ==========================================================

def get_deep_analysis(skill, score):
    banks = {
        1: [f"Kỹ năng {skill} đang ở mức nền tảng, cần đầu tư nghiêm túc để tái cấu trúc.",
            f"Vùng {skill} hiện tại là 'điểm mù' cần được khai phá bằng các lộ trình học tập mới."],
        2: [f"Năng lực {skill} đang phát triển nhưng chưa ổn định chiến lược.",
            f"Bạn có dấu hiệu tiến bộ ở {skill}, nhưng cần môi trường thực hành khốc liệt hơn."],
        3: [f"Năng lực {skill} đang ở ngưỡng ổn định, sẵn sàng bứt phá thành lợi thế cạnh tranh.",
            f"Tại mức {score}/5, {skill} đóng vai trò là trụ cột giữ vững sự cân bằng trong hồ sơ năng lực."],
        4: [f"Thế mạnh {skill} của bạn cực kỳ nổi bật, mang lại khả năng dẫn dắt và tầm ảnh hưởng.",
            f"Đây là điểm sáng giúp bạn tạo ra sự khác biệt hoàn toàn so với các đối thủ khác."],
        5: [f"Năng lực {skill} đạt cấp độ xuất sắc, tiệm cận chuyên gia và mang tính định danh cá nhân.",
            f"Sự xuất sắc ở {skill} chính là 'thương hiệu' giúp bạn mở ra những cơ hội đỉnh cao."]
    }
    return random.choice(banks[score])

# ==========================================================
# MAIN APP
# ==========================================================

setup_ui()

# --- NAVBAR SIÊU GỌN PHÍA TRÊN ---
st.markdown('<div class="nav-bar">', unsafe_allow_html=True)
nav_cols = st.columns([1, 1, 1, 1])
with nav_cols[0]:
    if st.button("🏠 Trang chủ", use_container_width=True):
        st.session_state.page = "home"
        st.session_state.analysis_done = False
        st.rerun()
with nav_cols[1]:
    with st.popover("🌟 Lợi ích", use_container_width=True):
        st.markdown("**Futurio giúp bạn:**\n- Hiểu rõ 5 trục năng lực.\n- Nhận diện điểm mạnh mũi nhọn.\n- Tối ưu lộ trình sự nghiệp.")
with nav_cols[2]:
    with st.popover("📖 Hướng dẫn", use_container_width=True):
        st.markdown("1. Chấm điểm Slider.\n2. Nhấn AI Quét.\n3. Xem phân tích đa chiều.")
with nav_cols[3]:
    st.markdown('<div style="text-align:right; color:#00f2ff; font-weight:bold; padding-top:5px;">v3.8 PRO</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- TRANG CHỦ (GỌN LÊN KHÔNG CẦN KÉO) ---
if st.session_state.page == "home":
    st.markdown('<div class="main-title">FUTURIO</div>', unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; margin-top:-10px; opacity:0.8;'>See Your Future. Shape Your Path.</h3>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="glass" style="text-align: center; max-width: 600px; margin: auto;">
        <p style="font-size:1.1rem;">Chào mừng bạn đến với hệ thống mô phỏng năng lực AI. 
        Hãy khám phá bản sắc chuyên nghiệp của mình ngay bây giờ.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    _, btn_center, _ = st.columns([1.2, 1, 1.2])
    with btn_center:
        if st.button("🚀 BẮT ĐẦU HÀNH TRÌNH", use_container_width=True):
            st.session_state.page = "assessment"
            st.rerun()

# --- TRANG ĐÁNH GIÁ (GIỮ NGUYÊN BỐ CỤC) ---
elif st.session_state.page == "assessment":
    st.markdown("<h2 style='text-align:center;'>🌌 ĐÁNH GIÁ NĂNG LỰC</h2>", unsafe_allow_html=True)
    
    skills = {}
    c1, c2 = st.columns(2)
    with c1:
        for s in ["🧠 Logic", "🎨 Sáng tạo", "📊 Phân tích"]:
            st.markdown('<div class="glass">', unsafe_allow_html=True)
            skills[s] = st.slider(s, 1, 5, 3)
            st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        for s in ["📢 Giao tiếp", "📁 Quản lý"]:
            st.markdown('<div class="glass">', unsafe_allow_html=True)
            skills[s] = st.slider(s, 1, 5, 3)
            st.markdown('</div>', unsafe_allow_html=True)
            
    if st.button("AI QUÉT NĂNG LỰC"):
        with st.spinner("AI đang xử lý tinh cầu năng lực..."):
            time.sleep(1.2)
        st.session_state.skills = skills
        st.session_state.analysis_done = True
        hi = max(skills, key=skills.get); lo = min(skills, key=skills.get)
        st.session_state.manifesto = f"Sứ mệnh của bạn là lấy {hi} làm mũi nhọn bứt phá, đồng thời hoàn thiện {lo} để xây dựng một đế chế năng lực bền vững."

    if st.session_state.analysis_done:
        tab1, tab2, tab3 = st.tabs(["📊 BIỂU ĐỒ", "🔮 PHÂN TÍCH CHI TIẾT", "📜 TUYÊN NGÔN"])
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
