# 💼 Job Skill Recommendation System

This project analyzes job descriptions to find the most in-demand skills across various job roles and industries using data mining and market trend analysis.

---

## 📌 Objective

To help job seekers, students, and professionals align their learning paths with market needs by recommending relevant technical skills based on real job postings.

---

## 📊 Dataset

- **Source**: job_postings.csv (cleaned as `cleaned_job_data.csv`)
- **Columns Used**: Job Title, Years of Experience, Job Skills, Pay, Industry, etc.
- **Rows**: Thousands of real job postings containing skill requirements.

---

## 🧹 Preprocessing Steps

- Parsed nested skill lists from string format.
- Normalized all skills to lowercase.
- Removed duplicate and similar terms (`"ml"` vs `"machine learning"`).
- Cleaned nulls and filtered irrelevant columns.

---

## 🔍 Exploratory Data Analysis (EDA)

- Top 20 in-demand skills overall and by role.
- Pay range distribution per job title.
- Heatmaps of skill co-occurrence.

---

## 📈 Machine Learning Used

- **Algorithm**: Association Rule Mining (Apriori)
- **Library**: `mlxtend`
- **Goal**: Recommend skill(s) based on a selected skill — e.g., if you know Python, it may recommend SQL, Pandas, etc.

---

## 🧠 Model Output

- Rules are saved in `skill_rules.pkl` for fast use.
- Example Rule:
    - **If you know:** `python`
    - **Then you should learn:** `sql`, `pandas`

---

## 💻 Files

| File | Description |
|------|-------------|
| `job_postings.csv` | Original dataset |
| `cleaned_job_data.csv` | Preprocessed dataset |
| `job_skill_recommendation_ml.ipynb` | Main notebook with code and EDA |
| `skill_rules.pkl` | Final model (association rules) |
| `app.py` (optional) | Streamlit interface to try out the skill recommender |

---

## 🛠️ Technologies Used

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Mlxtend
- Jupyter Notebook

---

## ✅ How to Run

1. Clone this repo.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
