import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Complete application with PSR Scoring Algorithm
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
    .score-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 25px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .metric-card {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        border-left: 4px solid #1f77b4;
    }
    .risk-green { background: #d4edda; border-left: 4px solid #28a745; }
    .risk-yellow { background: #fff3cd; border-left: 4px solid #ffc107; }
    .risk-orange { background: #ffeaa7; border-left: 4px solid #fd7e14; }
    .risk-red { background: #f8d7da; border-left: 4px solid #dc3545; }
    .risk-black { background: #d6d8db; border-left: 4px solid #6c757d; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🧠 PennyStock Profiler AI</div>', unsafe_allow_html=True)
st.success("🚀 Phase 3: PSR Scoring Algorithm Implemented!")

# COMPLETE DATA STRUCTURE (Same as Phase 2)
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

# PSR SCORING ALGORITHM
def calculate_psr_score(company_data):
    """Calculate Penny Stock Score (0-100)"""
    
    # Return Potential Score (RPS) - 50 points
    expected_return = company_data['expected_return']
    # Cap at 1000% return = 50 points, scale appropriately
    if expected_return <= 0:
        rps = 0
    else:
        rps = min(50, (expected_return / 10.0) * 50)
    
    # Risk & Volatility Score (RVS) - 30 points
    latest_sd = company_data['stats']['2022-23']['sd']
    latest_mean = company_data['stats']['2022-23']['mean']
    
    # Use Sharpe Ratio if available
    if 'sharpe_ratio' in company_data:
        sharpe = company_data['sharpe_ratio']
        rvs = min(30, max(0, sharpe * 12))  # Convert Sharpe ratio to score
    else:
        if latest_mean > 0:
            cv = latest_sd / latest_mean  # Coefficient of Variation
            rvs = max(0, 30 - (cv * 8))   # Lower CV = better score
        else:
            rvs = 10
    
    # Beta adjustment (penalize high beta)
    if 'beta' in company_data:
        beta = company_data['beta']
        beta_penalty = max(0, (beta - 1) * 4)  # Penalty for beta > 1
        rvs = max(0, rvs - beta_penalty)
    
    # Stability & Distribution Score (SDS) - 20 points
    latest_skewness = abs(company_data['stats']['2022-23']['skewness'])
    latest_kurtosis = abs(company_data['stats']['2022-23']['kurtosis'])
    
    # Lower absolute skewness = more stable (max 10 points)
    skewness_score = max(0, 10 - (latest_skewness * 3))
    
    # Kurtosis near 0 = normal distribution (max 10 points)
    kurtosis_score = max(0, 10 - (latest_kurtosis * 2))
    
    sds = skewness_score + kurtosis_score
    
    total_psr = rps + rvs + sds
    
    return {
        'total_score': round(total_psr, 1),
        'components': {
            'rps': round(rps, 1),
            'rvs': round(rvs, 1),
            'sds': round(sds, 1)
        },
        'details': {
            'expected_return': expected_return,
            'volatility': latest_sd,
            'sharpe_ratio': company_data.get('sharpe_ratio', 0),
            'beta': company_data.get('beta', 1),
            'skewness': company_data['stats']['2022-23']['skewness'],
            'kurtosis': company_data['stats']['2022-23']['kurtosis']
        }
    }

def get_risk_profile(psr_score):
    """Determine risk profile based on PSR score"""
    if psr_score >= 80:
        return "High Growth, Low Risk", "🟢", "risk-green", "Excellent investment with high returns and manageable risk"
    elif psr_score >= 65:
        return "Balanced Performer", "🟡", "risk-yellow", "Good balance of risk and return potential"
    elif psr_score >= 50:
        return "Speculative Opportunity", "🟠", "risk-orange", "Higher risk but potential for significant returns"
    elif psr_score >= 35:
        return "High Risk, Caution", "🔴", "risk-red", "Very risky, only for experienced investors"
    else:
        return "Avoid - Extreme Risk", "⚫", "risk-black", "Extremely high risk, not recommended for investment"

# Load the complete data
sectors_data = create_comprehensive_data()

# SIDEBAR NAVIGATION
st.sidebar.title("🧠 Navigation")
app_mode = st.sidebar.selectbox("Choose Module", 
                               ["🏠 Dashboard Overview",
                                "🎯 PSR Scoring Analysis", 
                                "📊 Company Explorer"])

st.sidebar.markdown("---")
st.sidebar.info("""
**PSR Score Components:**
- **RPS** (50 pts): Return Potential
- **RVS** (30 pts): Risk Management  
- **SDS** (20 pts): Stability & Distribution
""")

# MAIN CONTENT
if app_mode == "🏠 Dashboard Overview":
    st.header("📈 Dashboard Overview")
    
    # Calculate scores for all companies
    all_companies_data = []
    for sector_name, sector_data in sectors_data.items():
        for company_name, company_data in sector_data['companies'].items():
            psr_score = calculate_psr_score(company_data)
            risk_profile, emoji, _, _ = get_risk_profile(psr_score['total_score'])
            
            all_companies_data.append({
                'Company': company_name,
                'Sector': sector_name,
                'PSR Score': psr_score['total_score'],
                'Risk Profile': f"{emoji} {risk_profile}",
                'Expected Return %': company_data['expected_return'] * 100,
                'RPS': psr_score['components']['rps'],
                'RVS': psr_score['components']['rvs'],
                'SDS': psr_score['components']['sds']
            })
    
    df = pd.DataFrame(all_companies_data)
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        avg_psr = df['PSR Score'].mean()
        st.metric("Average PSR Score", f"{avg_psr:.1f}/100")
    with col2:
        high_quality = len(df[df['PSR Score'] >= 65])
        st.metric("Quality Stocks (PSR ≥65)", high_quality)
    with col3:
        avg_return = df['Expected Return %'].mean()
        st.metric("Avg Expected Return", f"{avg_return:.1f}%")
    with col4:
        top_performer = df.loc[df['Expected Return %'].idxmax()]
        st.metric("Top Return", f"{top_performer['Expected Return %']:.1f}%")
    
    # Top PSR Scores
    st.subheader("🏆 Top Rated Stocks (PSR Score)")
    top_psr = df.nlargest(8, 'PSR Score')[['Company', 'Sector', 'PSR Score', 'Risk Profile', 'Expected Return %']]
    st.dataframe(top_psr, use_container_width=True)
    
    # PSR Distribution
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.histogram(df, x='PSR Score', nbins=20, 
                           title='Distribution of PSR Scores',
                           color_discrete_sequence=['#1f77b4'])
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        fig2 = px.scatter(df, x='Expected Return %', y='PSR Score',
                         color='Risk Profile', size='PSR Score',
                         hover_data=['Company', 'Sector'],
                         title='PSR Score vs Expected Returns',
                         color_discrete_map={
                             '🟢 High Growth, Low Risk': 'green',
                             '🟡 Balanced Performer': 'yellow',
                             '🟠 Speculative Opportunity': 'orange',
                             '🔴 High Risk, Caution': 'red',
                             '⚫ Avoid - Extreme Risk': 'black'
                         })
        st.plotly_chart(fig2, use_container_width=True)

elif app_mode == "🎯 PSR Scoring Analysis":
    st.header("🎯 PSR Scoring Analysis")
    
    # Sector selection
    selected_sector = st.selectbox("Select Sector", list(sectors_data.keys()))
    companies = list(sectors_data[selected_sector]['companies'].keys())
    selected_company = st.selectbox("Select Company", companies)
    
    if selected_company:
        company_data = sectors_data[selected_sector]['companies'][selected_company]
        psr_result = calculate_psr_score(company_data)
        risk_profile, emoji, risk_class, risk_desc = get_risk_profile(psr_result['total_score'])
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            # PSR Score Display
            st.markdown(f"""
            <div class="score-card">
                <h3>Overall PSR Score</h3>
                <h1 style="font-size: 4rem; margin: 0;">{psr_result['total_score']}/100</h1>
                <h4>{emoji} {risk_profile}</h4>
                <p>{risk_desc}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Component Scores
            st.subheader("📊 Component Scores")
            components = psr_result['components']
            st.metric("Return Potential (RPS)", f"{components['rps']}/50")
            st.metric("Risk Management (RVS)", f"{components['rvs']}/30")
            st.metric("Stability (SDS)", f"{components['sds']}/20")
            
            # Key Metrics
            st.subheader("🔍 Key Metrics")
            details = psr_result['details']
            st.metric("Expected Return", f"{details['expected_return']*100:.1f}%")
            st.metric("Volatility (SD)", f"₹{details['volatility']:.2f}")
            st.metric("Sharpe Ratio", f"{details['sharpe_ratio']:.2f}")
            st.metric("Beta", f"{details['beta']:.2f}")
        
        with col2:
            # Radar Chart
            categories = ['Return Potential', 'Risk Management', 'Stability']
            values = [
                components['rps']/50,
                components['rvs']/30, 
                components['sds']/20
            ]
            
            fig = go.Figure()
            fig.add_trace(go.Scatterpolar(
                r=values + [values[0]],
                theta=categories + [categories[0]],
                fill='toself',
                fillcolor='rgba(31, 119, 180, 0.6)',
                line=dict(color='rgb(31, 119, 180)'),
                name='PSR Components'
            ))
            fig.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
                showlegend=False,
                title="PSR Score Components Breakdown",
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Detailed Analysis
            st.subheader("📈 Detailed Analysis")
            
            analysis_data = {
                'Metric': ['Skewness', 'Kurtosis', 'Current Price', '5-Year High', '5-Year Low'],
                'Value': [
                    f"{details['skewness']:.3f}",
                    f"{details['kurtosis']:.3f}",
                    f"₹{company_data['prices'][-1]:.2f}",
                    f"₹{max(company_data['prices']):.2f}",
                    f"₹{min(company_data['prices']):.2f}"
                ],
                'Interpretation': [
                    "Near 0 is ideal" if abs(details['skewness']) < 0.5 else "Skewed distribution",
                    "Near 0 is ideal" if abs(details['kurtosis']) < 1 else "Extreme values likely",
                    f"{((company_data['prices'][-1]-company_data['prices'][0])/company_data['prices'][0]*100):+.1f}% from start",
                    f"{(company_data['prices'][-1]/max(company_data['prices'])*100):.1f}% of high",
                    f"{(company_data['prices'][-1]/min(company_data['prices'])*100):.1f}% above low"
                ]
            }
            
            analysis_df = pd.DataFrame(analysis_data)
            st.dataframe(analysis_df, use_container_width=True, hide_index=True)
            
            # Price Trend
            years = ['2018-19', '2019-20', '2020-21', '2021-22', '2022-23']
            fig2 = px.line(x=years, y=company_data['prices'],
                          title=f'{selected_company} - Price Trend',
                          labels={'x': 'Year', 'y': 'Price (₹)'})
            fig2.add_hline(y=company_data['prices'][-1], line_dash="dash", 
                          annotation_text="Current Price", line_color="red")
            st.plotly_chart(fig2, use_container_width=True)

elif app_mode == "📊 Company Explorer":
    st.header("📊 Company Explorer")
    
    # Calculate all PSR scores
    all_companies = []
    for sector_name, sector_data in sectors_data.items():
        for company_name, company_data in sector_data['companies'].items():
            psr_score = calculate_psr_score(company_data)
            risk_profile, emoji, _, _ = get_risk_profile(psr_score['total_score'])
            
            all_companies.append({
                'Sector': sector_name,
                'Company': company_name,
                'PSR Score': psr_score['total_score'],
                'Risk Profile': f"{emoji} {risk_profile}",
                'Expected Return %': company_data['expected_return'] * 100,
                'Current Price': f"₹{company_data['prices'][-1]:.2f}",
                'Volatility': company_data['stats']['2022-23']['sd'],
                'Sharpe Ratio': company_data.get('sharpe_ratio', 'N/A')
            })
    
    explorer_df = pd.DataFrame(all_companies)
    
    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        min_psr = st.slider("Minimum PSR Score", 0, 100, 50)
    with col2:
        min_return = st.slider("Minimum Return %", 0, 1000, 100)
    with col3:
        risk_filter = st.selectbox("Risk Profile", ["All", "Green", "Yellow", "Orange", "Red", "Black"])
    
    # Apply filters
    filtered_df = explorer_df[
        (explorer_df['PSR Score'] >= min_psr) & 
        (explorer_df['Expected Return %'] >= min_return)
    ]
    
    if risk_filter != "All":
        risk_map = {"Green": "🟢", "Yellow": "🟡", "Orange": "🟠", "Red": "🔴", "Black": "⚫"}
        filtered_df = filtered_df[filtered_df['Risk Profile'].str.startswith(risk_map[risk_filter])]
    
    st.dataframe(filtered_df.sort_values('PSR Score', ascending=False), 
                use_container_width=True)

# Next Steps
st.markdown("---")
st.subheader("🎯 Next Phase Preview")
st.success("""
✅ **Phase 3 Complete**: PSR Scoring Algorithm implemented!
🚀 **Phase 4 Ready**: Complete interactive application with:
- Advanced stock screening
- Portfolio management  
- Real-time alerts
- Export functionality
- User authentication

**Current Intelligent Features:**
- Multi-dimensional PSR scoring (0-100)
- Risk profiling with color coding
- Component-wise analysis
- Interactive radar charts
- Advanced filtering system
""")

st.markdown("---")
st.markdown("**PennyStock Profiler AI** • Phase 3: Intelligent Scoring • Powered by PSR Algorithm")
