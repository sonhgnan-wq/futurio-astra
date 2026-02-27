# ==========================================================
# FUTURIO v3.6 – THE COSMIC RESURRECTION (FINAL)
# ==========================================================

import streamlit as st
import plotly.graph_objects as go
import random
import time

# ==========================================================
# CONFIG & STATE
# ==========================================================

st.set_page_config(page_title="Futurio v3.6", page_icon="🚀", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "home"
if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

# ==========================================================
# UI SYSTEM (RESTORING v3.2 AESTHETICS)
# ==========================================================

def setup_ui():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800&family=Playfair+Display:ital,wght@1,600&display=swap');

    /* Toàn bộ giao diện */
    .stApp {
        background: radial-gradient(circle at center, #0f172a, #020617);
        color: #FFFFFF;
    }

    /* Hiệu ứng sao rơi */
    .shooting-star {
        position: fixed;
        width: 2px;
        height: 70px;
        background: linear-gradient(to bottom, white, transparent);
        animation: shoot 4s linear infinite;
        opacity: 0.3;
        z-index: 0;
    }
    @keyframes shoot {
        0% { transform: translateY(-100px) translateX(0); opacity: 1; }
        100% { transform: translateY(100vh) translateX(200px); opacity: 0; }
    }

    /* Navbar tinh tế */
    .nav-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 5%;
        background: rgba(255, 255, 255, 0.03);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }

    /* Logo vòng tròn v3.2 */
    .logo-circle {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        border: 2px solid #00f2ff;
        box-shadow: 0 0 15px #00f2ff;
        position: relative;
    }

    /* Chữ nổi bật */
    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif;
        color: #FFFFFF !important;
        text-shadow: 0 0 15px rgba(0, 242, 255, 0.7);
        text-align: center;
    }

    /* Glass Card Premium */
    .glass {
        background: rgba(255, 255, 255, 0.07);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
        transition: 0.4s ease;
        backdrop-filter: blur(12px);
    }
    .glass:hover {
        transform: translateY(-8px);
        box-shadow: 0 10px 30px rgba(0, 242, 255, 0.3);
        border-color: #00f2ff;
    }

    /* Tuyên ngôn vinh quang */
    .manifesto-box {
        font-family: 'Playfair Display', serif;
        font-size: 20px;
        border: 2px solid #FFD700;
        box-shadow: 0 0 25px rgba(255, 215, 0, 0.4);
        padding: 30px;
        text-align: center;
        background: rgba(255, 215, 0, 0.05);
    }

    /* Slider styling */
    .stSlider label {
        font-family: 'Orbitron', sans-serif;
        color: #00f2ff !important;
        font-size: 16px !important;
    }
    
    /* Button Premium */
    div.stButton > button {
        width: 100%;
        border-radius: 30px !important;
        background: linear-gradient(90deg, #7000ff, #00f2ff) !important;
        color: white !important;
        font-family: 'Orbitron', sans-serif;
        font-weight: bold;
        border: none;
        padding: 15px;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.5);
    }

    </style>
    """, unsafe_allow_html=True)
    
    # Hiệu ứng sao rơi
    for i in range(5):
        st.markdown(f'<div class="shooting-star" style="left:{random.randint(0,90)}%; animation-delay:{random.random()*5}s"></div>', unsafe_allow_html=True)

# ==========================================================
# CONTENT ENGINE (DIVERSIFIED)
# ==========================================================

def get_analysis(skill, score):
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
            f"Đỉnh cao {skill} cho phép bạn kiến tạo những giá trị mà số đông không thể thực hiện được."]
    }
    return random.choice(banks[score])

# ==========================================================
# MAIN APP
# ==========================================================

setup_ui()

# --- NAVBAR ---
col_nav1, col_nav2, col_nav3, col_nav4 = st.columns([1, 2, 2, 2])
with col_nav1:
    st.markdown('<div class="logo-circle"></div>', unsafe_allow_html=True)
with col_nav2:
    if st.button("🏠 Trang chủ"):
        st.session_state.page = "home"
        st.session_state.analysis_done = False
        st.rerun()
with col_nav3:
    with st.popover("🌟 Tính năng & Lợi ích"):
        st.write("**Lợi ích:** Xác định trục năng lực, tối ưu lộ trình sự nghiệp và khám phá tiềm năng ẩn.")
with col_nav4:
    with st.popover("📖 Hướng dẫn"):
        st.write("1. Chấm điểm năng lực hiện tại.\n2. Nhấn AI Quét để phân tích.\n3. Nhận Tuyên ngôn sứ mệnh.")

st.markdown("<br><br>", unsafe_allow_html=True)

# --- PAGES ---
if st.session_state.page == "home":
    st.markdown("<h1>FUTURIO</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='opacity: 0.8;'>See Your Future. Shape Your Path.</h3>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="glass" style="text-align: center;">
        <p>Hệ thống mô phỏng năng lực dựa trên thuật toán AI giúp bạn nhìn thấu bản sắc cá nhân.</p>
        <div style="display: flex; justify-content: space-around; margin-top: 20px;">
            <div><b>Mơ hồ ➔ Tự tin</b></div>
            <div><b>Cảm tính ➔ Chiến lược</b></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 BẮT ĐẦU HÀNH TRÌNH"):
        st.session_state.page = "assessment"
        st.rerun()

elif st.session_state.page == "assessment":
    st.markdown("<h2>🌌 ĐÁNH GIÁ NĂNG LỰC</h2>", unsafe_allow_html=True)
    
    skills = {}
    col_l, col_r = st.columns(2)
    
    with col_l:
        for s in ["Logic", "Sáng tạo", "Phân tích"]:
            st.markdown('<div class="glass">', unsafe_allow_html=True)
            skills[s] = st.slider(s, 1, 5, 3)
            st.markdown('</div>', unsafe_allow_html=True)
    with col_r:
        for s in ["Giao tiếp", "Quản lý"]:
            st.markdown('<div class="glass">', unsafe_allow_html=True)
            skills[s] = st.slider(s, 1, 5, 3)
            st.markdown('</div>', unsafe_allow_html=True)
            
    if st.button("🧠 AI QUÉT NĂNG LỰC"):
        placeholder = st.empty()
        placeholder.markdown('<div style="text-align:center;"><br><br>🔄 <b>AI ĐANG MÔ PHỎNG TƯƠNG LAI...</b></div>', unsafe_allow_html=True)
        time.sleep(1.5)
        placeholder.empty()
        
        st.session_state.skills = skills
        st.session_state.analysis_done = True
        
        hi = max(skills, key=skills.get)
        lo = min(skills, key=skills.get)
        st.session_state.manifesto = f"Sứ mệnh của bạn là sử dụng sự vượt trội của **{hi}** để dẫn dắt hành động, đồng thời biến điểm yếu **{lo}** thành bài học thực tế để tạo nên một hệ sinh thái năng lực hoàn hảo."

    if st.session_state.analysis_done:
        tab1, tab2, tab3 = st.tabs(["📊 BIỂU ĐỒ", "🔮 PHÂN TÍCH", "📜 TUYÊN NGÔN"])
        
        with tab1:
            labels = list(st.session_state.skills.keys())
            values = list(st.session_state.skills.values())
            fig = go.Figure(go.Scatterpolar(
                r=values + [values[0]],
                theta=labels + [labels[0]],
                fill='toself',
                fillcolor='rgba(0, 242, 255, 0.2)',
                line_color='#00f2ff'
            ))
            fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])), paper_bgcolor="rgba(0,0,0,0)", font_color="white")
            st.plotly_chart(fig, use_container_width=True)
            

        with tab2:
            for k, v in st.session_state.skills.items():
                st.markdown(f'<div class="glass">{get_analysis(k, v)}</div>', unsafe_allow_html=True)

        with tab3:
            st.markdown(f'<div class="glass manifesto-box">{st.session_state.manifesto}</div>', unsafe_allow_html=True)
