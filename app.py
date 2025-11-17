import streamlit as st
import pandas as pd
import numpy as np

# Test version - minimal dependencies
st.set_page_config(page_title="PennyStock Profiler", layout="wide")

st.title("🧠 PennyStock Profiler AI")
st.success("✅ Application loaded successfully!")

# Simple data for testing
sectors = {
    'Capital Goods': ['Edvenswa Enter', 'Dhanashree Elect'],
    'Cement': ['Shiva Cement', 'Barak Valley'],
    'Chemicals': ['Pentokey Organy']
}

st.subheader("📊 Available Sectors & Companies")
for sector, companies in sectors.items():
    st.write(f"**{sector}**: {', '.join(companies)}")

st.subheader("🚀 Next Steps")
st.info("""
1. ✅ Basic app is working
2. 🔄 Add Plotly visualizations  
3. 📈 Implement full analysis features
4. 🎯 Deploy complete version
""")
