import streamlit as st
import numpy as np
import time
import random

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Futurio AI Pro",
    page_icon="🚀",
    layout="wide"
)

# ===============================
# CUSTOM CSS – PROFESSIONAL UI
# ===============================
st.markdown("""
<style>

html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif;
}

.main {
    background: linear-gradient(135deg,#0f172a,#1e293b);
    color: white;
}

h1, h2, h3 {
    color: white;
}

.section-card {
    background: #1e293b;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.4);
    margin-bottom: 25px;
}

.metric-box {
    background: #0ea5e9;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    color: white;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ===============================
# TITLE
# ===============================
st.title("🚀 Futurio AI Pro")
st.subheader("Phân tích thiên hướng học tập & nghề nghiệp bằng AI mô phỏng")

st.markdown("---")

# ===============================
# WEIGHTED ANALYSIS SYSTEM
# ===============================

weights = {
    "Logic": 1.2,
    "Sáng tạo": 1.1,
    "Giao tiếp": 1.0,
    "Phân tích dữ liệu": 1.3,
    "Quản lý": 1.15
}

scores = {}

st.markdown("## 🎯 Bài đánh giá năng lực")

for category in weights.keys():
    scores[category] = st.slider(
        f"Mức độ {category}",
        1, 5, 3
    )

# ===============================
# ANALYZE BUTTON
# ===============================

if st.button("🚀 Phân tích bằng AI"):

    # Loading Simulation
    with st.spinner("AI đang phân tích dữ liệu..."):
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.02)
            progress.progress(i + 1)

    st.success("Phân tích hoàn tất!")

    # ===============================
    # WEIGHTED SCORE CALCULATION
    # ===============================

    weighted_scores = {}
    total_weight = sum(weights.values())

    for k in scores:
        weighted_scores[k] = scores[k] * weights[k]

    final_score = sum(weighted_scores.values()) / total_weight

    confidence = min(95, 60 + int(np.std(list(scores.values())) * 10))

    # ===============================
    # RESULT SECTION
    # ===============================

    st.markdown("## 📊 Kết quả phân tích")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("AI Career Score", round(final_score,2))

    with col2:
        st.metric("Confidence Score", f"{confidence}%")

    # ===============================
    # PERSONALIZED AI INSIGHT – DEEP VERSION
    # ===============================

    st.markdown("## 🧠 AI Insight Chuyên Sâu")

    dominant = max(weighted_scores, key=weighted_scores.get)

    insight_1 = f"""
    Dựa trên hệ thống phân tích trọng số, năng lực nổi trội nhất của bạn là **{dominant}**.
    Điều này cho thấy bạn có xu hướng ra quyết định dựa trên cấu trúc và hệ thống rõ ràng.
    Nếu được đặt trong môi trường có tính chiến lược hoặc giải quyết vấn đề,
    bạn có khả năng phát huy tốt hơn 68% so với môi trường thuần sáng tạo ngẫu hứng.
    """

    insight_2 = """
    Mô hình AI phát hiện rằng sự phân bổ điểm của bạn khá đồng đều,
    cho thấy bạn thuộc nhóm “Hybrid Thinker” – người có khả năng kết hợp tư duy phân tích
    và cảm xúc sáng tạo. Nhóm này thường phù hợp với các ngành
    như Product Management, Data Strategy hoặc AI Development.
    """

    insight_3 = f"""
    Dựa trên độ lệch chuẩn trong lựa chọn của bạn,
    hệ thống đánh giá độ ổn định tư duy của bạn ở mức {confidence}%.
    Nếu bạn tiếp tục rèn luyện ở nhóm kỹ năng {dominant},
    xác suất đạt hiệu suất cao trong môi trường chuyên môn có thể tăng thêm 15–22%.
    """

    insight_4 = """
    AI cũng nhận thấy tiềm năng phát triển dài hạn của bạn nằm ở khả năng
    xây dựng chiến lược hơn là thực thi ngắn hạn.
    Bạn nên tham gia các dự án có yếu tố hoạch định,
    nơi bạn được trao quyền thiết kế hệ thống thay vì chỉ vận hành.
    """

    st.markdown(f"""
    <div class="section-card">
    <p>{insight_1}</p>
    <p>{insight_2}</p>
    <p>{insight_3}</p>
    <p>{insight_4}</p>
    </div>
    """, unsafe_allow_html=True)

# ===============================
# SIDEBAR GUIDE
# ===============================

st.sidebar.title("📘 Hướng dẫn sử dụng")

st.sidebar.markdown("""
1. Điều chỉnh thanh điểm theo mức độ phù hợp với bản thân  
2. Nhấn nút “Phân tích bằng AI”  
3. Xem Career Score và Confidence Score  
4. Đọc AI Insight chuyên sâu để hiểu định hướng nghề nghiệp  
""")

st.sidebar.markdown("---")
st.sidebar.caption("Futurio AI Pro © 2026")

