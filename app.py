# ==========================================================
# FUTURIO v3.7 – ULTRA SLIM EDITION
# ==========================================================

import streamlit as st
import plotly.graph_objects as go
import random
import time

# ==========================================================
# CONFIG & STATE
# ==========================================================

st.set_page_config(page_title="Futurio", page_icon="🚀", layout="wide")

def initialize_state():
    if "page" not in st.session_state: st.session_state.page = "home"
    if "analysis_done" not in st.session_state: st.session_state.analysis_done = False

# ==========================================================
# UI SYSTEM (CLEAN & CONTRAST)
# ==========================================================

def setup_ui():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Playfair+Display:ital,wght@1,600&display=swap');

    /* Nền và phông chữ tổng thể */
    .stApp {
        background: radial-gradient(circle at center, #0f172a, #020617);
        color: #FFFFFF !important;
    }

    /* Sao rơi ẩn dưới nền */
    .shooting-star {
        position: fixed; width: 2px; height: 50px;
        background: linear-gradient(to bottom, #00f2ff, transparent);
        animation: shoot 4s linear infinite; opacity: 0.2; z-index: 0;
    }
    @keyframes shoot {
        0% { transform: translateY(-100px) translateX(0); opacity: 1; }
        100% { transform: translateY(100vh) translateX(150px); opacity: 0; }
    }

    /* NAVBAR SIÊU GỌN */
    .nav-container {
        display: flex; justify-content: space-between; align-items: center;
        padding: 5px 20px; background: rgba(255, 255, 255, 0.05);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
    }

    /* LOGO NHỎ GỌN */
    .logo-mini {
        width: 30px; height: 30px; border-radius: 50%;
        border: 2px solid #00f2ff; box-shadow: 0 0 10px #00f2ff;
    }

    /* CHỮ FUTURIO TO & RÕ NÉT */
    .main-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 85px !important;
        font-weight: 900;
        color: #FFFFFF !important;
        text-shadow: 0 0 30px rgba(0, 242, 255, 0.8), 0 0 10px rgba(112, 0, 255, 0.5);
        text-align: center; margin: 20px 0;
        letter-spacing: 5px;
    }

    /* GLASS CARD (FIX MÀU CHỮ) */
    .glass {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px; padding: 20px; margin-bottom: 15px;
        backdrop-filter: blur(10px);
        color: #FFFFFF !important; /* Đảm bảo chữ luôn trắng */
    }
    .glass b, .glass p, .glass h3 {
        color: #FFFFFF !important;
    }

    /* SLIDER & BUTTON */
    .stSlider label { color: #00f2ff !important; font-weight: bold; }
    div.stButton > button {
        background: linear-gradient(90deg, #7000ff, #00f2ff) !important;
        color: white !important; border-radius: 20px; font-weight: bold;
    }

    /* MANIFESTO */
    .manifesto-box {
        font-family: 'Playfair Display', serif;
        border: 1px solid #FFD700; background: rgba(255, 215, 0, 0.05);
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)
    for i in range(3):
        st.markdown(f'<div class="shooting-star" style="left:{random.randint(0,95)}%; animation-delay:{random.random()*5}s"></div>', unsafe_allow_html=True)

# ==========================================================
# MAIN APP
# ==========================================================

def main():
    initialize_state()
    setup_ui()

    # --- THANH NAVBAR NHỎ GỌN PHÍA TRÊN ---
    cols = st.columns([0.5, 1.5, 1.5, 1.5, 0.5])
    with cols[1]:
        if st.button("🏠 Home", use_container_width=True):
            st.session_state.page = "home"
            st.session_state.analysis_done = False
            st.rerun()
    with cols[2]:
        with st.popover("🌟 Lợi ích", use_container_width=True):
            st.write("Định hướng nghề nghiệp & Khám phá tiềm năng ẩn qua AI.")
    with cols[3]:
        with st.popover("📖 Hướng dẫn", use_container_width=True):
            st.write("Kéo Slider ➔ Nhấn Quét ➔ Nhận Tuyên ngôn.")

    st.markdown("---") # Đường kẻ mảnh phân cách navbar

    # --- TRANG CHỦ ---
    if st.session_state.page == "home":
        st.markdown('<div class="main-title">FUTURIO</div>', unsafe_allow_html=True)
        st.markdown("<h3 style='text-align:center; opacity:0.8;'>See Your Future. Shape Your Path.</h3>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div class="glass" style="text-align: center; max-width: 700px; margin: auto;">
            <h3>Chào mừng tới tinh cầu năng lực</h3>
            <p>Thuật toán mô phỏng sự nghiệp của bạn sẽ bắt đầu ngay phía sau cánh cửa này.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        _, btn_col, _ = st.columns([1, 1, 1])
        with btn_col:
            if st.button("🚀 BẮT ĐẦU"):
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
            msg = st.empty()
            msg.markdown('<div class="glass" style="text-align:center;">🔄 <b>Đang phân tích dữ liệu...</b></div>', unsafe_allow_html=True)
            time.sleep(1.5)
            msg.empty()
            st.session_state.skills = skills
            st.session_state.analysis_done = True
            hi = max(skills, key=skills.get); lo = min(skills, key=skills.get)
            st.session_state.manifesto = f"Dùng sức mạnh của {hi} để chinh phục mục tiêu, và rèn luyện {lo} để bảo vệ thành quả."

        if st.session_state.analysis_done:
            t1, t2, t3 = st.tabs(["📊 BIỂU ĐỒ", "🔮 PHÂN TÍCH", "📜 TUYÊN NGÔN"])
            with t1:
                vals = list(st.session_state.skills.values())
                fig = go.Figure(go.Scatterpolar(r=vals + [vals[0]], theta=list(st.session_state.skills.keys()) + [list(st.session_state.skills.keys())[0]], fill='toself', fillcolor='rgba(0, 242, 255, 0.2)', line_color='#00f2ff'))
                fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])), paper_bgcolor="rgba(0,0,0,0)", font_color="white")
                st.plotly_chart(fig, use_container_width=True)
                
            with t2:
                for k, v in st.session_state.skills.items():
                    st.markdown(f'<div class="glass"><b>{k}</b>: Ở mức {v}/5. Đây là nhân tố quan trọng trong lộ trình của bạn.</div>', unsafe_allow_html=True)
            with t3:
                st.markdown(f'<div class="glass manifesto-box">{st.session_state.manifesto}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
