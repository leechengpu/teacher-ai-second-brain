# 🧠 教師個人知識萃取系統
### Teacher AI Second Brain

> 讓每一個靈感都不再消失

國立東華大學第一屆「AI 教育博覽會」參賽作品｜AI 系統開發組

---

## 系統簡介

本系統是一套專為國小教師設計的 AI 個人知識管理平台，整合 **Claude API**，透過自然語言介面幫助教師：

- 💡 **捕捉靈感**：隨時記錄想法，自動整理成結構化筆記
- 📄 **摘要文件**：上傳論文或文章，萃取教學應用重點
- 🔍 **知識搜尋**：用自然語言搜尋，跨筆記整合回答
- 📝 **生成教案**：輸入主題，自動生成符合 108 課綱的教案草稿

---

## 技術架構

```
使用者（自然語言）
    ↓
Streamlit Web 介面
    ↓
Claude API（claude-sonnet-4-6）
    ↓
結構化輸出（Markdown 筆記 / 教案）
```

---

## 安裝與執行

### 環境需求
- Python 3.10+
- Anthropic API Key

### 安裝步驟

```bash
git clone https://github.com/leechengpu/teacher-ai-second-brain.git
cd teacher-ai-second-brain
pip install -r requirements.txt
streamlit run app.py
```

### 取得 API Key
1. 前往 [console.anthropic.com](https://console.anthropic.com)
2. 建立 API Key
3. 在系統左側欄位貼上 Key 即可使用

---

## 解決的教師痛點

| 痛點 | 本系統的解決方式 |
|------|-----------------|
| 靈感閃現，沒時間記，忘了 | 自動整理成結構化筆記 |
| 論文讀不完，找不到重點 | AI 萃取教學應用重點 |
| 每次備課都要重新想 | 知識搜尋 + 教案生成 |
| 好想法隨時間消失 | 永久保存，越用越聰明 |

---

## 研究背景

- **就讀**：國立東華大學科學教育研究所博士班
- **指導教授**：蔡仁哲 助理教授
- **相關計劃**：東華「AI 精師培育計劃」
- **理論依據**：UNESCO AI CFT、個人知識管理理論（PKM）

---

## 授權

MIT License｜參賽作品著作財產權依競賽規範辦理
