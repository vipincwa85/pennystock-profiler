import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Test version with Plotly
st.set_page_config(
    page_title="PennyStock Profiler AI",
    page_icon="📈",
    layout="wide"
)

st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🧠 PennyStock Profiler AI</div>', unsafe_allow_html=True)
st.success("🚀 Phase 1: Plotly Visualizations Added Successfully!")

# Sample data with price history
sample_data = [
    {'Company': 'Edvenswa Enter', 'Sector': 'Electrical Equipment', '2018-19': 15.31, '2019-20': 14.05, '2020-21': 26.00, '2021-22': 78.55, '2022-23': 44.90, 'Return': 193.3},
    {'Company': 'Dhanashree Elect', 'Sector': 'Electrical Equipment', '2018-19': 16.00, '2019-20': 17.35, '2020-21': 17.60, '2021-22': 21.10, '2022-23': 23.50, 'Return': 46.9},
    {'Company': 'Shiva Cement', 'Sector': 'Cement', '2018-19': 13.60, '2019-20': 19.43, '2020-21': 35.10, '2021-22': 55.90, '2022-23': 46.93, 'Return': 245.1},
    {'Company': 'Pentokey Organy', 'Sector': 'Chemicals', '2018-19': 7.98, '2019-20': 5.61, '2020-21': 21.40, '2021-22': 21.00, '2022-23': 48.00, 'Return': 501.5}
]

df = pd.DataFrame(sample_data)

# Display data
st.subheader("📊 Company Data")
st.dataframe(df, use_container_width=True)

# Plotly Charts
col1, col2 = st.columns(2)

with col1:
    # Returns Bar Chart
    fig1 = px.bar(df, x='Company', y='Return', 
                 title='Expected Returns by Company',
                 color='Return', color_continuous_scale='Viridis')
    fig1.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    # Price Trend Chart
    years = ['2018-19', '2019-20', '2020-21', '2021-22', '2022-23']
    fig2 = go.Figure()
    
    for company in sample_data:
        prices = [company[year] for year in years]
        fig2.add_trace(go.Scatter(
            x=years, y=prices,
            mode='lines+markers',
            name=company['Company']
        ))
    
    fig2.update_layout(title='Stock Price Trends (2018-2023)',
                      xaxis_title='Financial Year',
                      yaxis_title='Stock Price (₹)')
    st.plotly_chart(fig2, use_container_width=True)

# Sector Analysis
st.subheader("📈 Sector Performance")
sector_analysis = df.groupby('Sector').agg({
    'Return': 'mean',
    'Company': 'count'
}).reset_index()
sector_analysis.columns = ['Sector', 'Avg Return %', 'Number of Companies']

col3, col4 = st.columns(2)

with col3:
    fig3 = px.pie(sector_analysis, values='Number of Companies', names='Sector',
                 title='Companies Distribution by Sector')
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    fig4 = px.bar(sector_analysis, x='Sector', y='Avg Return %',
                 title='Average Returns by Sector',
                 color='Avg Return %')
    st.plotly_chart(fig4, use_container_width=True)

# Next Steps
st.subheader("🎯 Next Phase Preview")
st.info("""
✅ **Phase 1 Complete**: Plotly visualizations working!
🔄 **Phase 2 Ready**: Full data structure from your research
📈 **Phase 3**: PSR Scoring algorithm
🚀 **Phase 4**: Complete interactive application

**Next**: We'll add all 200 companies from your PDF analysis!
""")

st.markdown("---")
st.markdown("**PennyStock Profiler AI** • Phase 1: Visualization • BSE Micro-cap Analysis")
