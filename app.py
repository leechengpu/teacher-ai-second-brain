import streamlit as st
import anthropic
import os
from datetime import datetime

# Page config
st.set_page_config(
    page_title="教師 AI 第二大腦",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 教師個人知識萃取系統")
st.caption("Teacher AI Second Brain — 讓每一個靈感都不再消失")

# Sidebar
with st.sidebar:
    st.header("⚙️ 設定")
    api_key = st.text_input("Anthropic API Key", type="password", help="輸入你的 Claude API Key")
    st.divider()
    st.markdown("**功能選單**")
    mode = st.radio("選擇功能", [
        "💡 捕捉靈感",
        "📄 摘要文件",
        "🔍 知識搜尋",
        "📝 生成教案"
    ])

if not api_key:
    st.info("請在左側輸入 Anthropic API Key 以開始使用。")
    st.stop()

client = anthropic.Anthropic(api_key=api_key)

# ── 功能一：捕捉靈感 ──
if mode == "💡 捕捉靈感":
    st.subheader("💡 捕捉靈感")
    st.markdown("輸入任何想法，系統自動整理成結構化筆記。")

    user_input = st.text_area("你的想法或靈感", placeholder="例如：想用 AI 幫學生自動批改作業，並給出個別化回饋...", height=120)

    col1, col2 = st.columns(2)
    with col1:
        subject = st.selectbox("科目", ["國語", "數學", "自然", "社會", "藝術", "體育", "綜合", "其他"])
    with col2:
        grade = st.selectbox("年段", ["低年級（1-2年級）", "中年級（3-4年級）", "高年級（5-6年級）", "全年段"])

    if st.button("✨ 整理成筆記", type="primary") and user_input:
        with st.spinner("AI 正在整理中..."):
            prompt = f"""你是一位國小全科老師的個人知識管理助手。
請將以下靈感整理成一篇結構化的 Obsidian 筆記（Markdown 格式）。

靈感內容：{user_input}
科目：{subject}
年段：{grade}

請產出包含以下內容的筆記：
1. frontmatter（title, date: {datetime.now().strftime('%Y-%m-%d')}, tags）
2. 核心想法摘要
3. 可能的應用方式（2-3點）
4. 後續行動建議
5. 教學建議

請用繁體中文回答，格式清晰。"""

            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1500,
                messages=[{"role": "user", "content": prompt}]
            )
            result = response.content[0].text

        st.success("整理完成！")
        st.code(result, language="markdown")
        st.download_button("⬇️ 下載筆記", result, file_name=f"靈感_{datetime.now().strftime('%Y%m%d_%H%M')}.md", mime="text/markdown")

# ── 功能二：摘要文件 ──
elif mode == "📄 摘要文件":
    st.subheader("📄 文件摘要")
    st.markdown("貼上論文、文章或任何文字，AI 自動萃取教學重點。")

    doc_text = st.text_area("貼上文件內容", placeholder="貼上論文摘要、文章段落...", height=200)

    if st.button("📋 生成教學摘要", type="primary") and doc_text:
        with st.spinner("AI 正在分析..."):
            prompt = f"""你是一位國小全科老師的個人知識管理助手。
請分析以下文件，從國小教師的角度萃取出最有價值的教學知識。

文件內容：
{doc_text}

請用繁體中文輸出：
1. **核心重點**（3-5點）
2. **對國小教學的啟示**
3. **可以立即應用的教學策略**
4. **建議延伸閱讀方向**"""

            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1200,
                messages=[{"role": "user", "content": prompt}]
            )
            result = response.content[0].text

        st.success("分析完成！")
        st.markdown(result)

# ── 功能三：知識搜尋 ──
elif mode == "🔍 知識搜尋":
    st.subheader("🔍 知識搜尋")
    st.markdown("描述你想找的內容，AI 協助整理相關知識。")

    query = st.text_input("你想搜尋什麼？", placeholder="例如：有沒有關於 AI 融入數學教學的想法？")

    if st.button("🔍 搜尋", type="primary") and query:
        with st.spinner("搜尋中..."):
            prompt = f"""你是一位國小全科老師的個人知識管理助手。
針對以下問題，從教師知識管理的角度提供整合性的回答與建議。

問題：{query}

請用繁體中文輸出：
1. **相關知識整理**
2. **教學應用建議**（具體可操作）
3. **值得記錄的關鍵概念**
4. **下一步行動建議**"""

            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1200,
                messages=[{"role": "user", "content": prompt}]
            )
            result = response.content[0].text

        st.markdown(result)

# ── 功能四：生成教案 ──
elif mode == "📝 生成教案":
    st.subheader("📝 AI 教案生成")
    st.markdown("描述教學目標，AI 自動生成符合 108 課綱的教案草稿。")

    col1, col2, col3 = st.columns(3)
    with col1:
        lesson_subject = st.selectbox("科目", ["國語", "數學", "自然", "社會", "藝術", "體育", "綜合"])
    with col2:
        lesson_grade = st.selectbox("年級", ["一年級", "二年級", "三年級", "四年級", "五年級", "六年級"])
    with col3:
        lesson_time = st.selectbox("節數", ["1節（40分鐘）", "2節", "3節"])

    lesson_topic = st.text_input("教學主題", placeholder="例如：認識分數的概念")
    lesson_goal = st.text_area("教學目標", placeholder="例如：學生能理解分數的意義，並能進行簡單分數比較", height=80)

    if st.button("📝 生成教案草稿", type="primary") and lesson_topic:
        with st.spinner("AI 正在生成教案..."):
            prompt = f"""你是一位資深國小全科老師與課程設計專家。
請根據 108 課綱精神，生成一份完整的教案草稿。

科目：{lesson_subject}
年級：{lesson_grade}
時間：{lesson_time}
主題：{lesson_topic}
教學目標：{lesson_goal or '請依主題自行設定適合的教學目標'}

請用繁體中文生成包含以下內容的教案：
1. 單元名稱與教學目標
2. 核心素養對應
3. 教學流程（引起動機 → 發展活動 → 綜合活動）
4. 評量方式
5. 教學資源與材料
6. AI 融入教學的建議"""

            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=2000,
                messages=[{"role": "user", "content": prompt}]
            )
            result = response.content[0].text

        st.success("教案生成完成！")
        st.markdown(result)
        st.download_button("⬇️ 下載教案", result, file_name=f"教案_{lesson_subject}_{lesson_grade}_{lesson_topic}.md", mime="text/markdown")

st.divider()
st.caption("國立東華大學科學教育研究所｜AI 教育博覽會參賽作品｜2026")
