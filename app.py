import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import io

# Complete professional application
st.set_page_config(
    page_title="PennyStock Profiler by CMA.VIPIN MISHRA",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional look
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
        margin: 10px 0;
    }
    .metric-card {
        background: white;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        border-left: 4px solid #1f77b4;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .sector-card {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        margin: 15px 0;
        border: 1px solid #e9ecef;
    }
    .risk-green { background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%); border-left: 4px solid #28a745; }
    .risk-yellow { background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%); border-left: 4px solid #ffc107; }
    .risk-orange { background: linear-gradient(135deg, #ffeaa7 0%, #ffd8a8 100%); border-left: 4px solid #fd7e14; }
    .risk-red { background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%); border-left: 4px solid #dc3545; }
    .risk-black { background: linear-gradient(135deg, #d6d8db 0%, #c6c8ca 100%); border-left: 4px solid #6c757d; }
    .feature-card {
        background: white;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        border: 1px solid #e9ecef;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🧠 PennyStock Profiler AI</div>', unsafe_allow_html=True)
st.success("🚀 Phase 4: Complete Interactive Application Deployed!")

# COMPREHENSIVE DATA STRUCTURE
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
                    'market_cap': 450,
                    'volume': 125000,
                    'interpretation': "High growth potential with moderate risk. Strong bullish sentiment."
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
                    'market_cap': 320,
                    'volume': 89000,
                    'interpretation': "Stable growth stock with low volatility. Ideal for conservative investors."
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
                    'market_cap': 1200,
                    'volume': 450000,
                    'interpretation': "Exceptional returns with moderate risk. Strong sector momentum."
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
                    'market_cap': 850,
                    'volume': 320000,
                    'interpretation': "Extreme growth stock with high volatility. For aggressive investors only."
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
                    'market_cap': 1500,
                    'volume': 2800000,
                    'interpretation': "Mega multi-bagger with extreme risk. Purely speculative investment."
                }
            }
        },
        'Pharmaceuticals': {
            'companies': {
                'Syschem (India)': {
                    'prices': [6.43, 7.13, 16.51, 46.10, 47.84],
                    'stats': {
                        '2018-19': {'mean': 14.959, 'sd': 8.472, 'skewness': 0.176, 'kurtosis': -1.971},
                        '2019-20': {'mean': 33.859, 'sd': 25.855, 'skewness': 0.469, 'kurtosis': -1.034},
                        '2020-21': {'mean': 50.570, 'sd': 25.830, 'skewness': 0.239, 'kurtosis': -1.911},
                        '2021-22': {'mean': 37.924, 'sd': 19.807, 'skewness': 0.647, 'kurtosis': -1.285},
                        '2022-23': {'mean': 28.040, 'sd': 14.670, 'skewness': 0.239, 'kurtosis': -1.065}
                    },
                    'expected_return': 6.440,
                    'beta': 1.4,
                    'sharpe_ratio': 1.8,
                    'market_cap': 920,
                    'volume': 180000,
                    'interpretation': "Strong growth with good risk-reward ratio. Sector tailwinds from healthcare."
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
    if expected_return <= 0:
        rps = 0
    else:
        rps = min(50, (expected_return / 10.0) * 50)
    
    # Risk & Volatility Score (RVS) - 30 points
    latest_sd = company_data['stats']['2022-23']['sd']
    latest_mean = company_data['stats']['2022-23']['mean']
    
    if 'sharpe_ratio' in company_data:
        sharpe = company_data['sharpe_ratio']
        rvs = min(30, max(0, sharpe * 12))
    else:
        if latest_mean > 0:
            cv = latest_sd / latest_mean
            rvs = max(0, 30 - (cv * 8))
        else:
            rvs = 10
    
    # Beta adjustment
    if 'beta' in company_data:
        beta = company_data['beta']
        beta_penalty = max(0, (beta - 1) * 4)
        rvs = max(0, rvs - beta_penalty)
    
    # Stability & Distribution Score (SDS) - 20 points
    latest_skewness = abs(company_data['stats']['2022-23']['skewness'])
    latest_kurtosis = abs(company_data['stats']['2022-23']['kurtosis'])
    
    skewness_score = max(0, 10 - (latest_skewness * 3))
    kurtosis_score = max(0, 10 - (latest_kurtosis * 2))
    sds = skewness_score + kurtosis_score
    
    total_psr = rps + rvs + sds
    
    return {
        'total_score': round(total_psr, 1),
        'components': {
            'rps': round(rps, 1),
            'rvs': round(rvs, 1),
            'sds': round(sds, 1)
        }
    }

def get_risk_profile(psr_score):
    """Determine risk profile based on PSR score"""
    if psr_score >= 80:
        return "High Growth, Low Risk", "🟢", "risk-green", "Excellent investment"
    elif psr_score >= 65:
        return "Balanced Performer", "🟡", "risk-yellow", "Good risk-reward balance"
    elif psr_score >= 50:
        return "Speculative Opportunity", "🟠", "risk-orange", "High risk, high reward"
    elif psr_score >= 35:
        return "High Risk, Caution", "🔴", "risk-red", "Very risky, experienced only"
    else:
        return "Avoid - Extreme Risk", "⚫", "risk-black", "Not recommended"

# PORTFOLIO TRACKING
def initialize_portfolio():
    if 'portfolio' not in st.session_state:
        st.session_state.portfolio = []
    if 'watchlist' not in st.session_state:
        st.session_state.watchlist = []

def add_to_portfolio(company, sector, quantity, price):
    st.session_state.portfolio.append({
        'company': company,
        'sector': sector,
        'quantity': quantity,
        'buy_price': price,
        'date_added': datetime.now().strftime("%Y-%m-%d")
    })

def add_to_watchlist(company, sector):
    if company not in [item['company'] for item in st.session_state.watchlist]:
        st.session_state.watchlist.append({
            'company': company,
            'sector': sector,
            'date_added': datetime.now().strftime("%Y-%m-%d")
        })

# Load data and initialize
sectors_data = create_comprehensive_data()
initialize_portfolio()

# SIDEBAR - MAIN NAVIGATION
st.sidebar.title(" PennyStock Profiler by CMA.VIPIN MISHRA")
st.sidebar.markdown("---")

app_mode = st.sidebar.selectbox("Navigation", [
    " Dashboard Overview",
    " PSR Scoring Analysis", 
    " Advanced Stock Screener",
    " Portfolio Manager",
    " Sector Analysis",
    " Quick Insights"
])

st.sidebar.markdown("---")
st.sidebar.info("""
**Professional Features:**
- Multi-dimensional Scoring
- Advanced Screening
- Portfolio Management
- Sector Analysis
- Export Capabilities
""")

# MAIN APPLICATION MODULES
if app_mode == "🏠 Dashboard Overview":
    st.header("📈 Executive Dashboard")
    
    # Calculate all scores
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
                'Current Price': company_data['prices'][-1],
                'Volatility': company_data['stats']['2022-23']['sd'],
                'Market Cap (Cr)': company_data.get('market_cap', 'N/A')
            })
    
    df = pd.DataFrame(all_companies_data)
    
    # KPI Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Companies", len(df))
        st.metric("Average PSR", f"{df['PSR Score'].mean():.1f}")
    with col2:
        st.metric("Quality Stocks", len(df[df['PSR Score'] >= 65]))
        st.metric("High Risk Stocks", len(df[df['PSR Score'] < 50]))
    with col3:
        st.metric("Avg Return", f"{df['Expected Return %'].mean():.1f}%")
        st.metric("Max Return", f"{df['Expected Return %'].max():.1f}%")
    with col4:
        st.metric("Your Portfolio", len(st.session_state.portfolio))
        st.metric("Watchlist", len(st.session_state.watchlist))
    
    # Top Performers
    st.subheader("🏆 Top Rated Stocks")
    top_stocks = df.nlargest(5, 'PSR Score')
    
    for _, stock in top_stocks.iterrows():
        risk_class = "risk-green" if stock['PSR Score'] >= 80 else "risk-yellow"
        st.markdown(f"""
        <div class="{risk_class} metric-card">
            <h4>{stock['Company']} ({stock['Sector']})</h4>
            <p><strong>PSR Score:</strong> {stock['PSR Score']}/100 | 
            <strong>Return:</strong> {stock['Expected Return %']:.1f}% | 
            <strong>Risk:</strong> {stock['Risk Profile']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Visualizations
    col1, col2 = st.columns(2)
    with col1:
        fig = px.scatter(df, x='Expected Return %', y='PSR Score',
                        color='Risk Profile', size='Current Price',
                        hover_data=['Company', 'Sector', 'Volatility'],
                        title='Risk-Return Analysis',
                        color_discrete_map={
                            '🟢 High Growth, Low Risk': 'green',
                            '🟡 Balanced Performer': 'yellow', 
                            '🟠 Speculative Opportunity': 'orange',
                            '🔴 High Risk, Caution': 'red',
                            '⚫ Avoid - Extreme Risk': 'black'
                        })
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        sector_perf = df.groupby('Sector').agg({
            'PSR Score': 'mean',
            'Expected Return %': 'mean',
            'Company': 'count'
        }).reset_index()
        
        fig2 = px.bar(sector_perf, x='Sector', y='PSR Score',
                     color='Expected Return %',
                     title='Sector Performance (PSR Scores)',
                     hover_data=['Company'])
        fig2.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig2, use_container_width=True)

elif app_mode == "🎯 PSR Scoring Analysis":
    st.header("🎯 Intelligent Stock Analysis")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        sector = st.selectbox("Select Sector", list(sectors_data.keys()))
        companies = list(sectors_data[sector]['companies'].keys())
        company = st.selectbox("Select Company", companies)
        
        if company:
            company_data = sectors_data[sector]['companies'][company]
            psr_score = calculate_psr_score(company_data)
            risk_profile, emoji, risk_class, risk_desc = get_risk_profile(psr_score['total_score'])
            
            # PSR Score Card
            st.markdown(f"""
            <div class="score-card">
                <h3>PSR Score</h3>
                <h1 style="font-size: 4rem; margin: 0;">{psr_score['total_score']}/100</h1>
                <h4>{emoji} {risk_profile}</h4>
                <p>{risk_desc}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Action Buttons
            col1a, col1b = st.columns(2)
            with col1a:
                if st.button("📈 Add to Portfolio", use_container_width=True):
                    add_to_portfolio(company, sector, 100, company_data['prices'][-1])
                    st.success(f"Added {company} to portfolio!")
            with col1b:
                if st.button("👀 Add to Watchlist", use_container_width=True):
                    add_to_watchlist(company, sector)
                    st.success(f"Added {company} to watchlist!")
            
            # Quick Stats
            st.subheader("📊 Key Metrics")
            st.metric("Current Price", f"₹{company_data['prices'][-1]:.2f}")
            st.metric("Expected Return", f"{company_data['expected_return']*100:.1f}%")
            st.metric("Volatility (SD)", f"₹{company_data['stats']['2022-23']['sd']:.2f}")
            st.metric("Market Cap", f"₹{company_data.get('market_cap', 'N/A')} Cr")
    
    with col2:
        if company:
            # Radar Chart
            components = psr_score['components']
            categories = ['Return Potential', 'Risk Management', 'Stability']
            values = [components['rps']/50, components['rvs']/30, components['sds']/20]
            
            fig = go.Figure()
            fig.add_trace(go.Scatterpolar(
                r=values + [values[0]],
                theta=categories + [categories[0]],
                fill='toself',
                fillcolor='rgba(31, 119, 180, 0.6)',
                line=dict(color='rgb(31, 119, 180)', width=2),
                name='PSR Components'
            ))
            fig.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
                showlegend=False,
                title="PSR Component Analysis",
                height=300
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Price Performance
            years = ['2018-19', '2019-20', '2020-21', '2021-22', '2022-23']
            fig2 = go.Figure()
            fig2.add_trace(go.Scatter(x=years, y=company_data['prices'],
                                    mode='lines+markers',
                                    name='Stock Price',
                                    line=dict(width=3)))
            fig2.update_layout(title='5-Year Price Trend',
                             xaxis_title='Financial Year',
                             yaxis_title='Price (₹)')
            st.plotly_chart(fig2, use_container_width=True)
            
            # Detailed Analysis
            st.subheader("🔍 Detailed Analysis")
            st.markdown(f"""
            <div class="metric-card">
                <h4>Investment Thesis</h4>
                <p>{company_data['interpretation']}</p>
                <p><strong>Sector:</strong> {sector} | <strong>Beta:</strong> {company_data.get('beta', 'N/A')} | 
                <strong>Sharpe Ratio:</strong> {company_data.get('sharpe_ratio', 'N/A')}</p>
            </div>
            """, unsafe_allow_html=True)

elif app_mode == "🔍 Advanced Stock Screener":
    st.header("🔍 Advanced Stock Screening")
    
    # Screening Filters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        min_psr = st.slider("Minimum PSR Score", 0, 100, 60)
        min_return = st.slider("Minimum Return %", 0, 1000, 100)
    with col2:
        max_volatility = st.slider("Max Volatility", 0.0, 50.0, 25.0)
        risk_filter = st.selectbox("Risk Profile", ["All", "Green", "Yellow", "Orange", "Red"])
    with col3:
        sector_filter = st.multiselect("Sectors", list(sectors_data.keys()), default=list(sectors_data.keys()))
        market_cap_min = st.number_input("Min Market Cap (Cr)", 0, 5000, 100)
    
    # Screening Results
    st.subheader("📊 Screening Results")
    
    results = []
    for sector in sector_filter:
        for company, data in sectors_data[sector]['companies'].items():
            psr_score = calculate_psr_score(data)
            latest_sd = data['stats']['2022-23']['sd']
            market_cap = data.get('market_cap', 0)
            
            if (psr_score['total_score'] >= min_psr and 
                data['expected_return'] >= min_return/100 and 
                latest_sd <= max_volatility and
                market_cap >= market_cap_min):
                
                risk_cat, emoji, _, _ = get_risk_profile(psr_score['total_score'])
                
                if risk_filter == "All" or risk_cat.startswith(risk_filter):
                    results.append({
                        'Company': company,
                        'Sector': sector,
                        'PSR Score': psr_score['total_score'],
                        'Risk Profile': f"{emoji} {risk_cat}",
                        'Expected Return %': data['expected_return'] * 100,
                        'Current Price': data['prices'][-1],
                        'Volatility': latest_sd,
                        'Market Cap (Cr)': market_cap,
                        'Sharpe Ratio': data.get('sharpe_ratio', 'N/A')
                    })
    
    if results:
        results_df = pd.DataFrame(results)
        st.dataframe(results_df.sort_values('PSR Score', ascending=False), 
                    use_container_width=True)
        
        # Export Results
        csv = results_df.to_csv(index=False)
        st.download_button(
            label="📥 Export Results as CSV",
            data=csv,
            file_name=f"stock_screening_results_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv",
            use_container_width=True
        )
    else:
        st.warning("No stocks match your criteria. Try adjusting filters.")

elif app_mode == "💼 Portfolio Manager":
    st.header("💼 Portfolio Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Your Portfolio")
        if st.session_state.portfolio:
            portfolio_df = pd.DataFrame(st.session_state.portfolio)
            st.dataframe(portfolio_df, use_container_width=True)
            
            # Portfolio Analytics
            total_investment = sum(item['quantity'] * item['buy_price'] for item in st.session_state.portfolio)
            st.metric("Total Investment", f"₹{total_investment:,.2f}")
        else:
            st.info("Your portfolio is empty. Add stocks from the PSR Analysis page.")
    
    with col2:
        st.subheader("Watchlist")
        if st.session_state.watchlist:
            watchlist_df = pd.DataFrame(st.session_state.watchlist)
            st.dataframe(watchlist_df, use_container_width=True)
        else:
            st.info("Your watchlist is empty. Add stocks to track them.")
    
    # Portfolio Analytics
    if st.session_state.portfolio:
        st.subheader("📈 Portfolio Analytics")
        
        # Sector Distribution
        sector_dist = {}
        for item in st.session_state.portfolio:
            sector = item['sector']
            value = item['quantity'] * item['buy_price']
            sector_dist[sector] = sector_dist.get(sector, 0) + value
        
        if sector_dist:
            fig = px.pie(values=list(sector_dist.values()), names=list(sector_dist.keys()),
                        title="Portfolio Sector Distribution")
            st.plotly_chart(fig, use_container_width=True)

elif app_mode == "📊 Sector Analysis":
    st.header("📊 Comprehensive Sector Analysis")
    
    selected_sector = st.selectbox("Choose Sector for Deep Analysis", list(sectors_data.keys()))
    
    if selected_sector:
        sector_data = sectors_data[selected_sector]
        
        # Sector Overview
        st.subheader(f"Sector Overview: {selected_sector}")
        
        companies_data = []
        for company_name, company_data in sector_data['companies'].items():
            psr_score = calculate_psr_score(company_data)
            companies_data.append({
                'Company': company_name,
                'Expected Return %': company_data['expected_return'] * 100,
                'PSR Score': psr_score['total_score'],
                'Current Price': company_data['prices'][-1],
                'Volatility': company_data['stats']['2022-23']['sd'],
                'Market Cap': company_data.get('market_cap', 'N/A')
            })
        
        sector_df = pd.DataFrame(companies_data)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.dataframe(sector_df, use_container_width=True)
        
        with col2:
            fig = px.bar(sector_df, x='Company', y='Expected Return %',
                        title=f'Returns in {selected_sector} Sector',
                        color='PSR Score')
            fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig, use_container_width=True)
        
        # Sector Performance Trends
        st.subheader("📈 Sector Performance Trends")
        
        # Calculate sector averages over years
        years = ['2018-19', '2019-20', '2020-21', '2021-22', '2022-23']
        sector_means = []
        
        for year in years:
            year_means = [company_data['stats'][year]['mean'] for company_data in sector_data['companies'].values()]
            sector_means.append(np.mean(year_means))
        
        fig = px.line(x=years, y=sector_means, title=f'{selected_sector} - Average Price Trend',
                     labels={'x': 'Year', 'y': 'Average Price (₹)'})
        st.plotly_chart(fig, use_container_width=True)

elif app_mode == "⚡ Quick Insights":
    st.header("⚡ Quick Insights & Alerts")
    
    # Generate insights
    all_companies = []
    for sector_name, sector_data in sectors_data.items():
        for company_name, company_data in sector_data['companies'].items():
            psr_score = calculate_psr_score(company_data)
            all_companies.append({
                'Company': company_name,
                'Sector': sector_name,
                'PSR Score': psr_score['total_score'],
                'Expected Return %': company_data['expected_return'] * 100,
                'Volatility': company_data['stats']['2022-23']['sd']
            })
    
    insights_df = pd.DataFrame(all_companies)
    
    # Top Insights
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🚀 Top Opportunities")
        top_opportunities = insights_df.nlargest(3, 'Expected Return %')
        for _, opp in top_opportunities.iterrows():
            st.markdown(f"""
            <div class="feature-card">
                <strong>{opp['Company']}</strong><br>
                Return: {opp['Expected Return %']:.1f}%<br>
                PSR: {opp['PSR Score']}/100
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("🛡️ Safest Bets")
        safe_bets = insights_df[insights_df['PSR Score'] >= 75].nlargest(3, 'PSR Score')
        for _, safe in safe_bets.iterrows():
            st.markdown(f"""
            <div class="feature-card">
                <strong>{safe['Company']}</strong><br>
                PSR: {safe['PSR Score']}/100<br>
                Volatility: ₹{safe['Volatility']:.1f}
            </div>
            """, unsafe_allow_html=True)
    
    with col3:
        st.subheader("⚠️ High Risk Alerts")
        high_risk = insights_df[insights_df['PSR Score'] < 40].nsmallest(3, 'PSR Score')
        for _, risk in high_risk.iterrows():
            st.markdown(f"""
            <div class="feature-card">
                <strong>{risk['Company']}</strong><br>
                PSR: {risk['PSR Score']}/100<br>
                Return: {risk['Expected Return %']:.1f}%
            </div>
            """, unsafe_allow_html=True)

# FOOTER
st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <h3>🎉 PennyStock Profiler AI - Complete Professional Platform</h3>
    <p><strong>Professional Grade Stock Analysis Tool</strong> • Built on BSE Micro-cap Research • Multi-dimensional Scoring</p>
    <p>📊 Advanced Analytics | 🎯 Intelligent Scoring | 🔍 Professional Screening | 💼 Portfolio Management</p>
</div>
""", unsafe_allow_html=True)
