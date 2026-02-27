# ===============================
# FUTURIO ASTRA - COMMERCIAL EDITION
# ===============================

import streamlit as st
import numpy as np
import random
import plotly.graph_objects as go

# ===============================
# 1️⃣ UI SETUP
# ===============================

def setup_ui():
    st.set_page_config(
        page_title="Futurio Astra",
        page_icon="🚀",
        layout="wide"
    )

    st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at 20% 20%, #111827, #050816);
        color: white;
    }

    /* Particle effect */
    body::before {
        content: "";
        position: fixed;
        width: 100%;
        height: 100%;
        background-image: radial-gradient(white 1px, transparent 1px);
        background-size: 40px 40px;
        opacity: 0.07;
        z-index: -1;
    }

    /* Glass Card */
    .glass {
        background: rgba(255,255,255,0.05);
        padding: 30px;
        border-radius: 20px;
        backdrop-filter: blur(12px);
        box-shadow: 0 0 25px #00f2ff40, 0 0 40px #7000ff40;
        margin-bottom: 30px;
    }

    /* Custom Button */
    .custom-btn {
        background: linear-gradient(90deg,#00f2ff,#7000ff);
        padding: 12px 28px;
        border-radius: 14px;
        font-weight: bold;
        text-align: center;
        cursor: pointer;
        transition: 0.3s;
        display: inline-block;
    }

    .custom-btn:hover {
        transform: scale(1.05);
        opacity: 0.9;
    }

    </style>
    """, unsafe_allow_html=True)


# ===============================
# 2️⃣ CONTENT LIBRARY
# ===============================

@st.cache_data
def load_content_library():
    return {
        "Logic": {
            5: ["Tư duy hệ thống xuất sắc.",
                "Khả năng phân tích đa chiều nổi bật.",
                "Năng lực xử lý vấn đề ở cấp độ chiến lược."],
            3: ["Tư duy logic ổn định.",
                "Khả năng phân tích ở mức khá.",
                "Có nền tảng suy luận tốt."],
            1: ["Cần củng cố tư duy cấu trúc.",
                "Nên rèn luyện khả năng phân tích.",
                "Chưa phát huy hết tiềm năng logic."]
        },
        "Giao tiếp": {
            5: ["Sở hữu tư duy kết nối vượt trội.",
                "Khả năng điều phối nhóm tiềm năng.",
                "Tạo ảnh hưởng mạnh mẽ trong giao tiếp."],
            3: ["Giao tiếp tương đối linh hoạt.",
                "Có thể kết nối nhóm hiệu quả.",
                "Khả năng diễn đạt khá tốt."],
            1: ["Cần cải thiện sự tự tin khi trao đổi.",
                "Nên rèn kỹ năng trình bày.",
                "Giao tiếp cần được đầu tư thêm."]
        }
    }


# ===============================
# 3️⃣ CALCULATION ENGINE
# ===============================

def calculation_engine(skills):

    weights = {
        "Logic": 1.4,
        "Sáng tạo": 1.2,
        "Giao tiếp": 1.1,
        "Phân tích": 1.5,
        "Quản lý": 1.3
    }

    # Scenario 1 - Status Quo
    current_score = np.mean(list(skills.values()))

    # Scenario 2 - Power Up
    sorted_skills = sorted(skills.items(), key=lambda x: x[1], reverse=True)
    boosted = dict(sorted_skills[:2])
    power_score = sum(boosted[k]*weights.get(k,1) for k in boosted)

    # Scenario 3 - Pivot
    weakest = min(skills, key=skills.get)
    pivot_skills = skills.copy()
    pivot_skills[weakest] += 1
    pivot_score = np.mean(list(pivot_skills.values()))

    return current_score, power_score, pivot_score


# ===============================
# 4️⃣ RENDER STEP 1
# ===============================

def render_step_1():
    st.markdown("## 🚀 Bước 1: Đánh giá năng lực")

    with st.form("skill_form"):
        col1, col2 = st.columns(2)

        skills = {}

        with col1:
            skills["Logic"] = st.slider("Logic",0,5,3,key="logic")
            skills["Sáng tạo"] = st.slider("Sáng tạo",0,5,3,key="creative")
            skills["Phân tích"] = st.slider("Phân tích dữ liệu",0,5,3,key="analysis")

        with col2:
            skills["Giao tiếp"] = st.slider("Giao tiếp",0,5,3,key="communication")
            skills["Quản lý"] = st.slider("Quản lý",0,5,3,key="management")

        submit = st.form_submit_button("Phân tích Astra")

    if submit:
        st.session_state["skills"] = skills
        st.session_state["step"] = 2


# ===============================
# 5️⃣ RENDER STEP 2 (RESULTS)
# ===============================

def render_step_2():
    st.markdown("## 📊 Bước 2: Kết quả & Kịch bản")

    skills = st.session_state["skills"]

    current, power, pivot = calculation_engine(skills)

    # Radar Chart
    categories = list(skills.keys())
    values = list(skills.values())
    values += values[:1]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories+categories[:1],
        fill='toself',
        name='Hiện tại',
        line_color='cyan'
    ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0,5])),
        showlegend=True
    )

    st.plotly_chart(fig, use_container_width=True)

    st.write("### 🔮 3 Kịch bản")
    st.write(f"Hiện tại: {round(current,2)}")
    st.write(f"Tối ưu hóa: {round(power,2)}")
    st.write(f"Chuyển hướng: {round(pivot,2)}")

    if st.button("Tiếp tục"):
        st.session_state["step"] = 3


# ===============================
# 6️⃣ RENDER STEP 3 (ACTION PLAN)
# ===============================

def render_step_3():
    st.markdown("## 🎯 Bước 3: Action Plan")

    missions = [
        "Hoàn thành 1 khóa kỹ năng nâng cao",
        "Tham gia 1 dự án thực tế",
        "Xây dựng portfolio cá nhân"
    ]

    for m in missions:
        if st.checkbox(m):
            st.success("🚀 Tuyệt vời! Bạn đang tiến gần hơn đến phiên bản tương lai của mình.")

    if st.button("Tạo Tuyên ngôn"):
        st.session_state["step"] = 4


# ===============================
# 7️⃣ AI SUMMARY
# ===============================

def render_step_4():
    st.markdown("## 🧠 Tuyên ngôn Tương lai")

    skills = st.session_state["skills"]
    dominant = max(skills, key=skills.get)

    templates = [
        f"Bạn sở hữu nền tảng {dominant} nổi bật. Khi được đặt vào môi trường phù hợp, bạn có thể bứt phá mạnh mẽ. Hãy hành động ngay hôm nay.",
        f"Năng lực {dominant} là trục chính trong hồ sơ của bạn. Tương lai mở rộng khi bạn khai thác triệt để lợi thế này. Đừng chần chừ.",
        f"{dominant} chính là động cơ chiến lược của bạn. Nếu duy trì kỷ luật phát triển, bạn có thể vươn tới cấp độ chuyên gia."
    ]

    st.markdown(random.choice(templates))


# ===============================
# MAIN ROUTING
# ===============================

def main():
    setup_ui()

    if "step" not in st.session_state:
        st.session_state["step"] = 1

    if st.session_state["step"] == 1:
        render_step_1()
    elif st.session_state["step"] == 2:
        render_step_2()
    elif st.session_state["step"] == 3:
        render_step_3()
    elif st.session_state["step"] == 4:
        render_step_4()


if __name__ == "__main__":
    main()
