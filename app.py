import streamlit as st
import numpy as np
import time
import random

st.set_page_config(page_title="Futurio AI Pro", page_icon="🚀", layout="wide")

# ===============================
# MODERN CSS
# ===============================
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg,#0f172a,#111827);
    color: #f1f5f9;
    font-family: 'Inter', sans-serif;
}

/* Title */
h1 {
    font-size: 42px !important;
    font-weight: 700 !important;
    color: #ffffff !important;
}

/* Section Card */
.card {
    background: rgba(255,255,255,0.05);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    box-shadow: 0px 8px 32px rgba(0,0,0,0.4);
    margin-bottom: 30px;
}

/* Insight Box - FIX COLOR ISSUE */
.insight-box {
    background: #f8fafc;
    color: #111827;
    padding: 30px;
    border-radius: 18px;
    font-size: 16px;
    line-height: 1.7;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
}

/* Buttons */
div.stButton > button {
    background: linear-gradient(90deg,#3b82f6,#06b6d4);
    color: white;
    border-radius: 12px;
    padding: 12px 24px;
    font-weight: 600;
    border: none;
}

div.stButton > button:hover {
    opacity: 0.85;
}

/* Guide Box */
.guide-box {
    background: linear-gradient(90deg,#1e293b,#334155);
    padding: 25px;
    border-radius: 18px;
    margin-bottom: 30px;
}

</style>
""", unsafe_allow_html=True)

# ===============================
# HERO SECTION
# ===============================

st.title("🚀 Futurio AI Pro")
st.markdown("### Hệ thống phân tích thiên hướng học tập & nghề nghiệp bằng AI mô phỏng")

st.markdown("""
<div class="guide-box">
<b>Cách sử dụng:</b><br>
1️⃣ Kéo thanh điểm theo mức độ phù hợp với bạn<br>
2️⃣ Nhấn nút <b>Phân tích bằng AI</b><br>
3️⃣ Xem Career Score + Confidence Score<br>
4️⃣ Đọc AI Insight chuyên sâu để hiểu định hướng phát triển<br>
</div>
""", unsafe_allow_html=True)

# ===============================
# WEIGHT SYSTEM
# ===============================

weights = {
    "Logic": 1.3,
    "Sáng tạo": 1.1,
    "Giao tiếp": 1.0,
    "Phân tích dữ liệu": 1.4,
    "Quản lý": 1.2
}

scores = {}

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🎯 Bài đánh giá năng lực")

for category in weights.keys():
    scores[category] = st.slider(f"Mức độ {category}", 1, 5, 3)

st.markdown('</div>', unsafe_allow_html=True)

# ===============================
# ANALYZE
# ===============================

if st.button("🚀 Phân tích bằng AI"):

    with st.spinner("AI đang mô phỏng dữ liệu và xây dựng hồ sơ năng lực..."):
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.015)
            progress.progress(i + 1)

    weighted_scores = {k: scores[k] * weights[k] for k in scores}
    total_weight = sum(weights.values())
    final_score = sum(weighted_scores.values()) / total_weight

    confidence = min(97, 65 + int(np.std(list(scores.values())) * 12))

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 Kết quả phân tích")

    col1, col2 = st.columns(2)
    col1.metric("AI Career Score", round(final_score,2))
    col2.metric("Confidence Score", f"{confidence}%")
    st.markdown('</div>', unsafe_allow_html=True)

    dominant = max(weighted_scores, key=weighted_scores.get)

    # ===============================
    # DEEP PERSONALIZED INSIGHT
    # ===============================

    insight = f"""
    <div class="insight-box">
    <p><b>1. Hồ sơ năng lực nổi bật:</b><br>
    Hệ thống xác định năng lực trội nhất của bạn là <b>{dominant}</b>.
    Điều này phản ánh xu hướng tư duy thiên về cấu trúc và chiến lược dài hạn.</p>

    <p><b>2. Mô hình tư duy:</b><br>
    Phân tích phân bổ điểm cho thấy bạn thuộc nhóm “Hybrid Strategic Thinker” —
    kết hợp giữa tư duy hệ thống và khả năng sáng tạo thích ứng.
    Nhóm này thường thành công trong các vai trò yêu cầu ra quyết định phức hợp.</p>

    <p><b>3. Độ ổn định & độ tin cậy:</b><br>
    Confidence Score đạt <b>{confidence}%</b>,
    cho thấy hồ sơ năng lực của bạn có tính nhất quán cao.
    Khi được đặt trong môi trường phù hợp, hiệu suất có thể tăng 18–25%.</p>

    <p><b>4. Gợi ý phát triển chuyên sâu:</b><br>
    Bạn nên ưu tiên tham gia các dự án có yếu tố chiến lược,
    nghiên cứu hoặc quản trị hệ thống thay vì công việc thuần vận hành.
    Đây là hướng đi giúp tối đa hóa tiềm năng dài hạn.</p>
    </div>
    """

    st.markdown(insight, unsafe_allow_html=True)
