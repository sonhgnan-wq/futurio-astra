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

# ==========================================================
# UI SYSTEM (RESTORING v3.2 AESTHETICS & FIXING LOGO)
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

    /* Navbar tinh tế v3.6 */
    .nav-bar {
        background: rgba(255, 255, 255, 0.03);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        padding: 10px 0;
        margin-bottom: 30px;
    }

    /* Logo vòng tròn v3.2 (Đã sửa lỗi đen xì) */
    .logo-circle {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        border: 2px solid #00f2ff;
        box-shadow: 0 0 15px #00f2ff;
        margin: auto;
        position: relative;
    }
    .logo-circle::after {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        border-radius: 50%;
        border: 2px solid #7000ff;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); opacity: 1;}
        100% { transform: scale(1.4); opacity: 0;}
    }

    /* Chữ nổi bật trên nền tối */
    h1, h2, h3, .slogan {
        font-family: 'Orbitron', sans-serif;
        color: #FFFFFF !important;
        text-shadow: 0 0 15px rgba(0, 242, 255, 0.8);
        text-align: center;
    }

    /* Glass Card Premium v3.2 */
    .glass {
        background: rgba(255, 255, 255, 0.07);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
        transition: 0.4s ease;
        backdrop-filter: blur(12px);
        color: #FFFFFF !important;
    }
    .glass:hover {
        transform: translateY(-8px);
        box-shadow: 0 10px 30px rgba(0, 242, 255, 0.3);
    }

    /* Tuyên ngôn vinh quang */
    .manifesto-box {
        font-family: 'Playfair Display', serif;
        border: 2px solid gold;
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.5);
        background: rgba(255, 215, 0, 0.05);
    }

    /* Slider styling v3.2 */
    .stSlider label {
        font-family: 'Orbitron', sans-serif;
        color: #00f2ff !important;
        font-size: 18px !important;
        font-weight: 700;
    }
    
    /* Button Premium */
    div.stButton > button {
        border-radius: 30px !important;
        background: linear-gradient(90deg, #7000ff, #00f2ff) !important;
        color: white !important;
        font-weight: bold;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.5);
    }

    </style>
    """, unsafe_allow_html=True)
    
    for i in range(5):
        st.markdown(f'<div class="shooting-star" style="left:{random.randint(0,90)}%; animation-delay:{random.random()*5}s"></div>', unsafe_allow_html=True)

# ==========================================================
# CONTENT ENGINE (DIVERSIFIED ANALYSIS)
# ==========================================================

def get_deep_analysis(skill, score):
    banks = {
        1: [f"Năng lực {skill} hiện tại là vùng tiềm năng sơ khai, cần một chiến lược tái cấu trúc tư duy toàn diện.", 
            f"Mức điểm này cho thấy {skill} đang ngủ yên, đòi hỏi sự đầu tư rèn luyện kỷ luật để đánh thức bản sắc."],
        2: [f"Kỹ năng {skill} đang trong giai đoạn hình thành, cần được cọ xát qua các dự án thực tế để tăng độ nhạy bén.",
            f"Nền tảng về {skill} của bạn đã có, nhưng thiếu sự ổn định để trở thành một vũ khí chiến lược."],
        3: [f"Năng lực {skill} đang ở ngưỡng cân bằng tuyệt vời, sẵn sàng bứt phá trở thành điểm nhấn trong hồ sơ cá nhân.",
            f"Vận hành ổn định ở mức {score}/5, {skill} là bệ phóng an toàn cho các quyết định nghề nghiệp của bạn."],
        4: [f"Thế mạnh {skill} của bạn cực kỳ sắc sảo, đủ khả năng dẫn dắt và tạo ra tầm ảnh hưởng trong môi trường chuyên nghiệp.",
            f"Đây là năng lực mũi nhọn, giúp bạn tạo ra lợi thế cạnh tranh khác biệt so với số đông."],
        5: [f"Đỉnh cao {skill} cho thấy bạn tiệm cận mức độ chuyên gia, có khả năng kiến tạo những giá trị mang tính định danh.",
            f"Sự xuất sắc ở {skill} chính là trục chiến lược để bạn xây dựng thương hiệu cá nhân bền vững."]
    }
    return random.choice(banks[score])

# ==========================================================
# MAIN APP
# ==========================================================

def main():
    initialize_state()
    setup_ui()

    # --- NAVBAR (Thanh điều hướng trên cùng) ---
    st.markdown('<div class="nav-bar">', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns([1, 1, 1, 1])
    with c1:
        if st.button("🏠 Trang chủ", key="nav_home"):
            st.session_state.page = "home"
            st.session_state.analysis_done = False
            st.rerun()
    with c2:
        with st.popover("🌟 Tính năng & Lợi ích"):
            st.markdown("""
            **Hệ thống Futurio giúp bạn:**
            * Phân tích đa chiều 5 trục năng lực cốt lõi.
            * Nhận diện 'Điểm mù' và 'Điểm sáng' trong sự nghiệp.
            * Tối ưu hóa lộ trình phát triển cá nhân dựa trên AI.
            """)
    with c3:
        with st.popover("📖 Hướng dẫn"):
            st.markdown("""
            1. **Đánh giá:** Di chuyển Slider theo cảm nhận thực tế về bản thân.
            2. **Phân tích:** Nhấn nút 'AI Quét' để hệ thống xử lý dữ liệu.
            3. **Ứng dụng:** Đọc kỹ Tuyên ngôn sứ mệnh để định hướng hành động.
            """)
    with c4:
        st.markdown('<div class="logo-circle"></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- PAGES ---
    if st.session_state.page == "home":
        st.markdown('<h1 style="margin-top: 50px;">FUTURIO</h1>', unsafe_allow_html=True)
        st.markdown('<div class="slogan">See Your Future. Shape Your Path.</div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div class="glass" style="text-align: center; max-width: 800px; margin: auto;">
            <h3>Khám phá tinh cầu năng lực của bạn</h3>
            <p style="opacity: 0.9;">Sử dụng thuật toán mô phỏng để đo lường và định hướng tương lai chuyên nghiệp.</p>
            <hr style="border-color: rgba(255,255,255,0.1)">
            <div style="display: flex; justify-content: space-around; font-size: 14px;">
                <div><b>TỪ: Mơ hồ</b></div>
                <div><b>➔</b></div>
                <div><b>ĐẾN: Chiến lược</b></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        col_btn, _ = st.columns([1, 2])
        with col_btn:
            if st.button("🚀 BẮT ĐẦU HÀNH TRÌNH"):
                st.session_state.page = "assessment"
                st.rerun()

    elif st.session_state.page == "assessment":
        st.markdown("<h2>🌌 ĐÁNH GIÁ NĂNG LỰC</h2>", unsafe_allow_html=True)
        
        # Sắp xếp Slider trong các thẻ Glass
        skills = {}
        col_left, col_right = st.columns(2)
        
        with col_left:
            for s in ["🧠 Logic", "🎨 Sáng tạo", "📊 Phân tích"]:
                st.markdown('<div class="glass">', unsafe_allow_html=True)
                skills[s] = st.slider(s, 1, 5, 3)
                st.markdown('</div>', unsafe_allow_html=True)
        with col_right:
            for s in ["📢 Giao tiếp", "📁 Quản lý"]:
                st.markdown('<div class="glass">', unsafe_allow_html=True)
                skills[s] = st.slider(s, 1, 5, 3)
                st.markdown('</div>', unsafe_allow_html=True)
            
        if st.button("AI QUÉT NĂNG LỰC"):
            placeholder = st.empty()
            placeholder.markdown('<div class="glass" style="text-align:center;">🔄 <b>AI ĐANG MÔ PHỎNG DỮ LIỆU TƯƠNG LAI...</b></div>', unsafe_allow_html=True)
            time.sleep(1.5)
            placeholder.empty()
            
            st.session_state.skills = skills
            st.session_state.analysis_done = True
            
            hi = max(skills, key=skills.get)
            lo = min(skills, key=skills.get)
            st.session_state.manifesto = f"""
            Sứ mệnh của bạn là sử dụng sự đột phá của {hi} làm mũi nhọn tấn công, 
            đồng thời tinh chỉnh {lo} để tạo ra thế cân bằng chiến lược bền vững. 
            Tương lai thuộc về người biết dùng ưu điểm để làm chủ nghịch cảnh.
            """

        if st.session_state.analysis_done:
            tab1, tab2, tab3 = st.tabs(["📊 BIỂU ĐỒ", "🔮 PHÂN TÍCH", "📜 TUYÊN NGÔN"])
            
            with tab1:
                labels = list(st.session_state.skills.keys())
                values = list(st.session_state.skills.values())
                values += [values[0]]
                fig = go.Figure(go.Scatterpolar(
                    r=values,
                    theta=labels + [labels[0]],
                    fill='toself',
                    fillcolor='rgba(0, 242, 255, 0.25)',
                    line_color='#00f2ff'
                ))
                fig.update_layout(
                    polar=dict(radialaxis=dict(visible=True, range=[0, 5], gridcolor="rgba(255,255,255,0.1)")),
                    paper_bgcolor="rgba(0,0,0,0)",
                    font_color="white",
                    margin=dict(t=30, b=30)
                )
                st.plotly_chart(fig, use_container_width=True)
                

            with tab2:
                for k, v in st.session_state.skills.items():
                    st.markdown(f'<div class="glass">{get_deep_analysis(k, v)}</div>', unsafe_allow_html=True)

            with tab3:
                st.markdown(f'<div class="glass manifesto-box">{st.session_state.manifesto}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
