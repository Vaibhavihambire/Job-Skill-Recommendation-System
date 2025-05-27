import streamlit as st
import pandas as pd
import pickle

# Load association rules
with open("skill_rules.pkl", "rb") as f:
    skill_rules = pickle.load(f)

# Page setup
st.set_page_config(page_title="Job Skill Recommender", layout="wide")

# Header
st.markdown("""
    <div style='background: linear-gradient(to right, #1e3c72, #2a5298); padding: 25px; border-radius: 12px;'>
        <h1 style='color: white; text-align: center;'>🚀 Job Skill Recommendation System</h1>
        <p style='color: #f1f1f1; text-align: center; font-size:18px;'>Get intelligent skill suggestions based on real job market data</p>
    </div>
    <br>
""", unsafe_allow_html=True)

# Input Section in Columns
col1, col2, col3 = st.columns([1.5, 2, 1.5])

with col2:
    st.markdown("### 🎯 Enter a Skill You Know")
    selected_skill = st.text_input("e.g. python, sql, aws", placeholder="Type a skill here...")

    recommend = st.button("🔍 Recommend Skills", use_container_width=True)

    if recommend:
        if selected_skill.strip() == "":
            st.warning("⚠️ Please enter a skill to get recommendations.")
        else:
            # Find matching rules
            recommendations = skill_rules[skill_rules['antecedents'].apply(lambda x: selected_skill.lower() in x)]

            st.markdown("### 📌 Recommended Skills to Learn Next")

            if not recommendations.empty:
                rec_skills = set()
                for consequent in recommendations['consequents']:
                    rec_skills.update(consequent)
                rec_skills.discard(selected_skill.lower())

                if rec_skills:
                    for skill in sorted(rec_skills):
                        st.markdown(
                            f"<span style='background-color:#dfe6e9; color:#2d3436; padding:6px 12px; margin:4px; border-radius:18px; display:inline-block;'>{skill}</span>",
                            unsafe_allow_html=True
                        )
                else:
                    st.info("✅ Skill is already highly specialized. No new suggestions found.")
            else:
                st.error("❌ No related skills found. Try another input like 'sql', 'excel', or 'aws'.")

# Explanation below
st.markdown("---")
st.markdown("### 🔍 How Does This Work?")
st.markdown("""
- This tool uses **association rule mining (Apriori)** to discover common skill patterns in job postings.
- When you type a skill, it searches for rules like: *"If you know X, then Y is often also required."*
- Helps identify **what to learn next** to become a stronger job candidate!

📌 **Popular skills to try**: `python`, `sql`, `excel`, `aws`, `machine learning`, `agile`, `linux`

---

👨‍💻 **Built with**: Python, Pandas, MLxtend, Streamlit  
📊 **Dataset**: Real-world job postings  
""")

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray'>✨ Made with ❤️ by Vaibhavi Hambire — 2025</p>", unsafe_allow_html=True)
