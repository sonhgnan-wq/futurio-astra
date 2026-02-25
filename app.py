import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Futurio AI", layout="wide")

st.title("🚀 Futurio AI")
st.subheader("Phân tích thiên hướng học tập & nghề nghiệp")

st.info("Thang điểm: 1 = Rất không đúng | 5 = Rất đúng")
st.markdown("---")

# =========================
# CÂU HỎI
# =========================

questions = {
    "Logic": [
        "Tôi thích giải quyết vấn đề phức tạp",
        "Tôi thích làm việc với số liệu",
        "Tôi suy nghĩ có hệ thống"
    ],
    "Sáng tạo": [
        "Tôi có nhiều ý tưởng độc đáo",
        "Tôi thích thiết kế hoặc nghệ thuật",
        "Tôi dễ tưởng tượng điều mới"
    ],
    "Lãnh đạo": [
        "Tôi tự tin nói trước đám đông",
        "Tôi thích dẫn dắt người khác",
        "Tôi có khả năng thuyết phục"
    ],
    "Công nghệ": [
        "Tôi thích tìm hiểu công nghệ",
        "Tôi muốn học lập trình",
        "Tôi tò mò cách hệ thống hoạt động"
    ],
    "Kinh doanh": [
        "Tôi quan tâm đến tài chính",
        "Tôi thích lập kế hoạch dài hạn",
        "Tôi thích xây dựng dự án riêng"
    ]
}

responses = {}

# =========================
# SLIDER + PROGRESS
# =========================

total_questions = sum(len(q) for q in questions.values())
answered = 0

for category, qs in questions.items():
    st.markdown(f"## {category}")
    responses[category] = []

    for q in qs:
        score = st.slider(q, 1, 5, 3)
        responses[category].append(score)
        answered += 1

    st.markdown("---")

st.progress(answered / total_questions)

# =========================
# PHÂN TÍCH THÔNG MINH HƠN
# =========================

def smart_analysis(scores):
    max_score = max(scores.values())
    min_score = min(scores.values())

    strong = [k for k,v in scores.items() if v >= max_score - 0.4]
    weak = [k for k,v in scores.items() if v <= min_score + 0.4]

    text = "## 🧠 Phân tích chuyên sâu\n\n"

    text += f"### 🔥 Thiên hướng nổi bật: {', '.join(strong)}\n\n"
    text += "Bạn có xu hướng tự nhiên phù hợp với nhóm trên. Nếu được đầu tư đúng hướng, bạn có thể phát triển vượt trội.\n\n"

    text += f"### ⚠️ Cần cải thiện: {', '.join(weak)}\n\n"

    if "Logic" in strong and "Công nghệ" in strong:
        text += "💡 Bạn có profile thiên về kỹ thuật – rất phù hợp với AI, Data, Engineering.\n\n"

    if "Sáng tạo" in strong and "Lãnh đạo" in strong:
        text += "💡 Bạn có tố chất sáng tạo kết hợp ảnh hưởng xã hội – phù hợp Marketing, Media, Startup.\n\n"

    text += "### 🚀 Lộ trình 3 năm đề xuất:\n"
    text += "- Năm 1: Học nền tảng và khám phá chuyên sâu lĩnh vực mạnh nhất\n"
    text += "- Năm 2: Làm dự án thực tế hoặc thực tập\n"
    text += "- Năm 3: Xây portfolio và định vị cá nhân\n"

    return text

# =========================
# BIỂU ĐỒ RADAR
# =========================

def radar_chart(scores):

    categories = list(scores.keys())
    values = list(scores.values())

    values += values[:1]
    angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]

    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)

    ax.set_ylim(0,5)

    st.pyplot(fig)

# =========================
# NÚT PHÂN TÍCH
# =========================

if st.button("🚀 Phân tích toàn diện"):

    category_scores = {}
    for category, scores in responses.items():
        avg = sum(scores)/len(scores)
        category_scores[category] = round(avg,2)

    st.markdown("## 📊 Điểm trung bình")
    for k,v in category_scores.items():
        st.write(f"**{k}**: {v}")

    st.markdown("## 📈 Biểu đồ năng lực")
    radar_chart(category_scores)

    analysis = smart_analysis(category_scores)
    st.markdown(analysis)