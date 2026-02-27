import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from dataclasses import dataclass
from typing import Dict, List

# ===============================
# CONFIGURATION
# ===============================

st.set_page_config(
    page_title="Futurio AI Pro",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===============================
# DATA MODEL
# ===============================

@dataclass
class Category:
    name: str
    questions: List[str]


CATEGORIES = [
    Category("Logic", [
        "Tôi thích giải quyết vấn đề phức tạp",
        "Tôi thích làm việc với số liệu",
        "Tôi suy nghĩ có hệ thống"
    ]),
    Category("Sáng tạo", [
        "Tôi có nhiều ý tưởng độc đáo",
        "Tôi thích thiết kế hoặc nghệ thuật",
        "Tôi dễ tưởng tượng điều mới"
    ]),
    Category("Lãnh đạo", [
        "Tôi tự tin nói trước đám đông",
        "Tôi thích dẫn dắt người khác",
        "Tôi có khả năng thuyết phục"
    ]),
    Category("Công nghệ", [
        "Tôi thích tìm hiểu công nghệ",
        "Tôi muốn học lập trình",
        "Tôi tò mò cách hệ thống hoạt động"
    ]),
    Category("Kinh doanh", [
        "Tôi quan tâm đến tài chính",
        "Tôi thích lập kế hoạch dài hạn",
        "Tôi thích xây dựng dự án riêng"
    ])
]

# ===============================
# ANALYSIS ENGINE
# ===============================

class CareerAnalyzer:

    @staticmethod
    def calculate_scores(responses: Dict[str, List[int]]) -> Dict[str, float]:
        return {
            category: round(sum(scores) / len(scores), 2)
            for category, scores in responses.items()
        }

    @staticmethod
    def classify_strengths(scores: Dict[str, float]):
        max_score = max(scores.values())
        min_score = min(scores.values())

        strong = [k for k, v in scores.items() if v >= max_score - 0.3]
        weak = [k for k, v in scores.items() if v <= min_score + 0.3]

        return strong, weak

    @staticmethod
    def generate_analysis(scores: Dict[str, float]) -> str:
        strong, weak = CareerAnalyzer.classify_strengths(scores)

        text = "## 🧠 Phân tích chuyên sâu\n\n"

        text += f"### 🔥 Thiên hướng nổi bật: {', '.join(strong)}\n\n"
        text += "Bạn có lợi thế tự nhiên trong nhóm năng lực này. Nếu được đầu tư bài bản, đây có thể là trục phát triển dài hạn của bạn.\n\n"

        text += f"### ⚠️ Nhóm cần cải thiện: {', '.join(weak)}\n\n"
        text += "Việc nâng cấp những kỹ năng này sẽ giúp bạn phát triển cân bằng hơn.\n\n"

        if "Logic" in strong and "Công nghệ" in strong:
            text += "💡 Profile kỹ thuật: Phù hợp AI, Data, Engineering, Software.\n\n"

        if "Sáng tạo" in strong and "Lãnh đạo" in strong:
            text += "💡 Profile ảnh hưởng – sáng tạo: Marketing, Media, Startup, Branding.\n\n"

        text += "### 🚀 Lộ trình đề xuất 3 năm:\n"
        text += "- Năm 1: Học nền tảng & chọn 1 chuyên môn trọng tâm\n"
        text += "- Năm 2: Làm dự án thực tế / thực tập\n"
        text += "- Năm 3: Xây portfolio & thương hiệu cá nhân\n"

        return text


# ===============================
# VISUALIZATION
# ===============================

def render_radar_chart(scores: Dict[str, float]):

    categories = list(scores.keys())
    values = list(scores.values())

    values += values[:1]
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, polar=True)

    ax.plot(angles, values, linewidth=2)
    ax.fill(angles, values, alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_ylim(0, 5)

    st.pyplot(fig)


# ===============================
# SIDEBAR - USER GUIDE
# ===============================

with st.sidebar:
    st.title("📘 Hướng dẫn sử dụng")

    st.markdown("""
    ### Cách sử dụng Futurio AI

    1️⃣ Trả lời tất cả câu hỏi theo thang điểm 1–5  
    2️⃣ Nhấn **Phân tích toàn diện**  
    3️⃣ Xem biểu đồ năng lực và phân tích chuyên sâu  
    4️⃣ Dựa vào lộ trình 3 năm để định hướng phát triển  

    ### Thang điểm
    - 1 = Rất không đúng
    - 3 = Trung bình
    - 5 = Rất đúng

    ### Mục tiêu hệ thống
    Futurio AI giúp bạn:
    - Hiểu thiên hướng cá nhân
    - Nhận diện nhóm năng lực nổi bật
    - Xây lộ trình phát triển dài hạn
    """)

    st.markdown("---")
    st.caption("Futurio AI Pro v2.0")

# ===============================
# MAIN UI
# ===============================

st.title("🚀 Futurio AI Pro")
st.subheader("Phân tích thiên hướng học tập & nghề nghiệp")

st.markdown("---")

responses = {}
total_questions = sum(len(cat.questions) for cat in CATEGORIES)
answered = 0

for category in CATEGORIES:
    st.markdown(f"## {category.name}")
    responses[category.name] = []

    cols = st.columns(1)

    for question in category.questions:
        score = st.slider(
            question,
            min_value=1,
            max_value=5,
            value=3,
            key=f"{category.name}_{question}"
        )
        responses[category.name].append(score)
        answered += 1

    st.markdown("---")

st.progress(answered / total_questions)

# ===============================
# ANALYZE BUTTON
# ===============================

if st.button("🚀 Phân tích toàn diện", use_container_width=True):

    analyzer = CareerAnalyzer()
    category_scores = analyzer.calculate_scores(responses)

    st.markdown("## 📊 Điểm trung bình")

    for k, v in category_scores.items():
        st.write(f"**{k}**: {v}")

    st.markdown("## 📈 Biểu đồ năng lực")
    render_radar_chart(category_scores)

    analysis_text = analyzer.generate_analysis(category_scores)
    st.markdown(analysis_text)

# ===============================
# FOOTER
# ===============================

st.markdown("---")
st.caption("© 2026 Futurio AI Pro | Designed for Strategic Career Development")
