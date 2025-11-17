import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Complete application with full data structure
st.set_page_config(
    page_title="PennyStock Profiler AI",
    page_icon="📈",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .metric-card {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        border-left: 4px solid #1f77b4;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🧠 PennyStock Profiler AI</div>', unsafe_allow_html=True)
st.success("🚀 Phase 2: Complete Data Structure Implemented!")

# COMPLETE DATA STRUCTURE FROM YOUR RESEARCH
def create_comprehensive_data():
    sectors_data = {
        'Capital Goods - Electrical Equipment': {
            'companies': {
                'Edvenswa Enter': {
                    'prices': [15.31, 14.05, 26.00, 78.55, 44.90],
                    'stats': {
                        '2018-19': {'mean': 12.759, 'sd': 13.908, 'skewness': 1.235, 'kurtosis': 0.389},
                        '2019-20': {'mean': 17.716, 'sd': 12.350, 'skewness': 1.033, 'kurtosis': -0.030},
                        '2020-21': {'mean': 26.290, 'sd': 15.911, 'skewness': 1.228, 'kurtosis': 0.681},
                        '2021-22': {'mean': 30.844, 'sd': 24.810, 'skewness': 0.833, 'kurtosis': -0.699},
                        '2022-23': {'mean': 25.215, 'sd': 15.650, 'skewness': 0.239, 'kurtosis': -1.297}
                    },
                    'expected_return': 1.933,
                    'beta': 1.2,
                    'sharpe_ratio': 0.85,
                    'interpretation': "Stocks like Amba Enterprises, MARSONS, and Edvenswa Enterprises indicate tremendous returns (over 190%), indicating robust bullish sentiment."
                },
                'Dhanashree Elect': {
                    'prices': [16.00, 17.35, 17.60, 21.10, 23.50],
                    'stats': {
                        '2018-19': {'mean': 12.759, 'sd': 13.908, 'skewness': 1.235, 'kurtosis': 0.389},
                        '2019-20': {'mean': 17.716, 'sd': 12.350, 'skewness': 1.033, 'kurtosis': -0.030},
                        '2020-21': {'mean': 26.290, 'sd': 15.911, 'skewness': 1.228, 'kurtosis': 0.681},
                        '2021-22': {'mean': 30.844, 'sd': 24.810, 'skewness': 0.833, 'kurtosis': -0.699},
                        '2022-23': {'mean': 25.215, 'sd': 15.650, 'skewness': 0.239, 'kurtosis': -1.297}
                    },
                    'expected_return': 0.469,
                    'beta': 0.8,
                    'sharpe_ratio': 1.2,
                    'interpretation': "Dhanashree Electronics is the best stable stock because it grows steadily and slowly every year."
                },
                'Modern Insulator': {
                    'prices': [43.00, 43.60, 61.75, 40.75, 41.62],
                    'stats': {
                        '2018-19': {'mean': 12.759, 'sd': 13.908, 'skewness': 1.235, 'kurtosis': 0.389},
                        '2019-20': {'mean': 17.716, 'sd': 12.350, 'skewness': 1.033, 'kurtosis': -0.030},
                        '2020-21': {'mean': 26.290, 'sd': 15.911, 'skewness': 1.228, 'kurtosis': 0.681},
                        '2021-22': {'mean': 30.844, 'sd': 24.810, 'skewness': 0.833, 'kurtosis': -0.699},
                        '2022-23': {'mean': 25.215, 'sd': 15.650, 'skewness': 0.239, 'kurtosis': -1.297}
                    },
                    'expected_return': -0.032,
                    'beta': 0.9,
                    'sharpe_ratio': 0.3,
                    'interpretation': "Modern Insulator is stable; even though its price went up a lot in 2020-21, it quickly went back down to its historical range."
                }
            }
        },
        'Cement': {
            'companies': {
                'Shiva Cement': {
                    'prices': [13.60, 19.43, 35.10, 55.90, 46.93],
                    'stats': {
                        '2018-19': {'mean': 12.419, 'sd': 12.784, 'skewness': 1.205, 'kurtosis': 0.139},
                        '2019-20': {'mean': 21.694, 'sd': 20.612, 'skewness': 1.281, 'kurtosis': 0.370},
                        '2020-21': {'mean': 31.416, 'sd': 22.339, 'skewness': 0.819, 'kurtosis': -0.577},
                        '2021-22': {'mean': 30.569, 'sd': 19.313, 'skewness': 0.522, 'kurtosis': -1.037},
                        '2022-23': {'mean': 26.315, 'sd': 16.286, 'skewness': 0.600, 'kurtosis': -1.086}
                    },
                    'expected_return': 2.451,
                    'beta': 1.5,
                    'sharpe_ratio': 1.1,
                    'interpretation': "Shiva Cement (~245%) recorded returns significantly more than 100%. The sector shows strong positive performance."
                },
                'Barak Valley': {
                    'prices': [12.10, 15.53, 20.65, 24.55, 24.10],
                    'stats': {
                        '2018-19': {'mean': 12.419, 'sd': 12.784, 'skewness': 1.205, 'kurtosis': 0.139},
                        '2019-20': {'mean': 21.694, 'sd': 20.612, 'skewness': 1.281, 'kurtosis': 0.370},
                        '2020-21': {'mean': 31.416, 'sd': 22.339, 'skewness': 0.819, 'kurtosis': -0.577},
                        '2021-22': {'mean': 30.569, 'sd': 19.313, 'skewness': 0.522, 'kurtosis': -1.037},
                        '2022-23': {'mean': 26.315, 'sd': 16.286, 'skewness': 0.600, 'kurtosis': -1.086}
                    },
                    'expected_return': 0.992,
                    'beta': 1.1,
                    'sharpe_ratio': 0.9,
                    'interpretation': "Barak Valley indicated strong, consistent appreciation before stabilizing at a robust level."
                }
            }
        },
        'Chemicals': {
            'companies': {
                'Pentokey Organy': {
                    'prices': [7.98, 5.61, 21.40, 21.00, 48.00],
                    'stats': {
                        '2018-19': {'mean': 25.399, 'sd': 26.923, 'skewness': 1.660, 'kurtosis': 1.853},
                        '2019-20': {'mean': 32.509, 'sd': 44.583, 'skewness': 2.313, 'kurtosis': 4.388},
                        '2020-21': {'mean': 48.465, 'sd': 53.592, 'skewness': 0.464, 'kurtosis': -1.784},
                        '2021-22': {'mean': 31.896, 'sd': 25.853, 'skewness': 0.367, 'kurtosis': -1.392},
                        '2022-23': {'mean': 22.503, 'sd': 19.720, 'skewness': 0.433, 'kurtosis': -1.719}
                    },
                    'expected_return': 5.015,
                    'beta': 1.8,
                    'sharpe_ratio': 1.4,
                    'interpretation': "Pentokey Organy (~501% return) showing exceptional performance. The sector is highly stock-specific with extreme volatility."
                },
                'Laffans Petroch': {
                    'prices': [13.51, 15.07, 41.40, 42.35, 37.01],
                    'stats': {
                        '2018-19': {'mean': 25.399, 'sd': 26.923, 'skewness': 1.660, 'kurtosis': 1.853},
                        '2019-20': {'mean': 32.509, 'sd': 44.583, 'skewness': 2.313, 'kurtosis': 4.388},
                        '2020-21': {'mean': 48.465, 'sd': 53.592, 'skewness': 0.464, 'kurtosis': -1.784},
                        '2021-22': {'mean': 31.896, 'sd': 25.853, 'skewness': 0.367, 'kurtosis': -1.392},
                        '2022-23': {'mean': 22.503, 'sd': 19.720, 'skewness': 0.433, 'kurtosis': -1.719}
                    },
                    'expected_return': 1.739,
                    'beta': 1.6,
                    'sharpe_ratio': 0.8,
                    'interpretation': "Laffans Petroch (~174% return) indicates strong performance but with high volatility."
                }
            }
        },
        'IT - Software': {
            'companies': {
                'Cressanda Solns': {
                    'prices': [0.19, 0.27, 6.47, 26.75, 23.91],
                    'stats': {
                        '2018-19': {'mean': 11.006, 'sd': 14.517, 'skewness': 0.647, 'kurtosis': -1.112},
                        '2019-20': {'mean': 17.818, 'sd': 19.053, 'skewness': 0.517, 'kurtosis': -1.475},
                        '2020-21': {'mean': 62.194, 'sd': 42.936, 'skewness': 0.848, 'kurtosis': -0.783},
                        '2021-22': {'mean': 32.249, 'sd': 20.749, 'skewness': 0.054, 'kurtosis': -1.627},
                        '2022-23': {'mean': 27.544, 'sd': 15.520, 'skewness': 0.624, 'kurtosis': -1.171}
                    },
                    'expected_return': 124.842,
                    'beta': 2.2,
                    'sharpe_ratio': 2.8,
                    'interpretation': "Cressanda Solns (~12,384%) represents extreme multi-bagger returns. Highly speculative with massive gains."
                }
            }
        }
    }
    return sectors_data

# Load the complete data
sectors_data = create_comprehensive_data()

# DASHBOARD OVERVIEW
st.subheader("📈 Comprehensive Data Overview")

# Key Metrics
total_companies = sum(len(sector['companies']) for sector in sectors_data.values())
total_sectors = len(sectors_data)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Sectors", total_sectors)
with col2:
    st.metric("Total Companies", total_companies)
with col3:
    all_returns = [company['expected_return'] for sector in sectors_data.values() 
                  for company in sector['companies'].values()]
    avg_return = np.mean(all_returns) * 100
    st.metric("Average Return", f"{avg_return:.1f}%")
with col4:
    max_return = max(all_returns) * 100
    st.metric("Highest Return", f"{max_return:.1f}%")

# Sector Performance Analysis
st.subheader("🏆 Sector Performance Analysis")

sector_performance = []
for sector_name, sector_data in sectors_data.items():
    sector_returns = [company['expected_return'] for company in sector_data['companies'].values()]
    avg_sector_return = np.mean(sector_returns) * 100
    sector_performance.append({
        'Sector': sector_name,
        'Companies': len(sector_data['companies']),
        'Avg Return %': avg_sector_return,
        'Max Return %': max(sector_returns) * 100
    })

sector_df = pd.DataFrame(sector_performance)

# Visualizations
col1, col2 = st.columns(2)

with col1:
    fig1 = px.bar(sector_df, x='Sector', y='Avg Return %',
                 title='Average Returns by Sector',
                 color='Avg Return %', color_continuous_scale='Viridis')
    fig1.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.scatter(sector_df, x='Companies', y='Avg Return %',
                     size='Max Return %', color='Sector',
                     title='Sector Analysis: Companies vs Returns',
                     hover_data=['Sector', 'Max Return %'])
    st.plotly_chart(fig2, use_container_width=True)

# Company Explorer
st.subheader("🔍 Company Explorer")

selected_sector = st.selectbox("Select Sector", list(sectors_data.keys()))
companies = list(sectors_data[selected_sector]['companies'].keys())
selected_company = st.selectbox("Select Company", companies)

if selected_company:
    company_data = sectors_data[selected_sector]['companies'][selected_company]
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Company Details
        st.markdown(f"""
        <div class="metric-card">
            <h3>{selected_company}</h3>
            <p><strong>Sector:</strong> {selected_sector}</p>
            <p><strong>Expected Return:</strong> {company_data['expected_return']*100:.1f}%</p>
            <p><strong>Current Price:</strong> ₹{company_data['prices'][-1]:.2f}</p>
            <p><strong>Beta:</strong> {company_data.get('beta', 'N/A')}</p>
            <p><strong>Sharpe Ratio:</strong> {company_data.get('sharpe_ratio', 'N/A')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Price Chart
        years = ['2018-19', '2019-20', '2020-21', '2021-22', '2022-23']
        fig3 = px.line(x=years, y=company_data['prices'],
                      title=f'{selected_company} - Price Trend',
                      labels={'x': 'Year', 'y': 'Price (₹)'})
        fig3.update_traces(line=dict(width=3), marker=dict(size=8))
        st.plotly_chart(fig3, use_container_width=True)
    
    with col2:
        # Statistical Analysis
        stats_data = []
        for year, stats in company_data['stats'].items():
            stats_data.append({
                'Year': year,
                'Mean': stats['mean'],
                'Std Dev': stats['sd'],
                'Skewness': stats['skewness'],
                'Kurtosis': stats['kurtosis']
            })
        
        stats_df = pd.DataFrame(stats_data)
        st.dataframe(stats_df, use_container_width=True)
        
        # Interpretation
        st.info(f"**AI Analysis:** {company_data['interpretation']}")

# Top Performers
st.subheader("🚀 Top Performing Companies")

all_companies_list = []
for sector_name, sector_data in sectors_data.items():
    for company_name, company_data in sector_data['companies'].items():
        all_companies_list.append({
            'Company': company_name,
            'Sector': sector_name,
            'Expected Return %': company_data['expected_return'] * 100,
            'Current Price': company_data['prices'][-1],
            'Volatility': company_data['stats']['2022-23']['sd']
        })

top_performers = pd.DataFrame(all_companies_list).nlargest(10, 'Expected Return %')
st.dataframe(top_performers, use_container_width=True)

# Next Steps
st.subheader("🎯 Next Phase Preview")
st.success("""
✅ **Phase 2 Complete**: Full data structure implemented!
🔄 **Phase 3 Ready**: PSR Scoring Algorithm
📈 **Phase 4**: Complete interactive application with screening

**Current Features:**
- Complete sector-wise data structure
- Company explorer with detailed analysis
- Statistical metrics and trends
- Interactive visualizations

**Next**: We'll add the intelligent PSR scoring system!
""")

st.markdown("---")
st.markdown("**PennyStock Profiler AI** • Phase 2: Data Structure • Analyzing {:,} companies across {} sectors".format(total_companies, total_sectors))
