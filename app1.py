# ==============================================================================
# WORLD CUP 2026: PREMIUM ANALYTICS PLATFORM v5.1 (AUTOMATED SECURE AI)
# ==============================================================================
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import os
from groq import Groq

# 1. Page Configuration
st.set_page_config(page_title="2026 World Cup Predictive Engine", layout="wide")

# ==============================================================================
# SECURE BACKEND CREDENTIAL LOADING
# ==============================================================================

# 1. Safely check if we are running locally before trying to load a .env file
if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv()

# 2. Fetch the key from the environment OR Streamlit Secrets seamlessly
GROQ_API_KEY = os.environ.get("GROQ_API_KEY") 
if not GROQ_API_KEY:
    try:
        GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    except (KeyError, FileNotFoundError):
        GROQ_API_KEY = None

# ==============================================================================
# HERO SECTION & METHODOLOGY
# ==============================================================================
st.title("🏆 2026 World Cup Hybrid Intelligence Engine")
st.markdown(f"**Live Engine Status:** Active | **Last Sync:** {datetime.now().strftime('%B %d, %Y')}")

with st.expander("📖 Platform Guide: Methodology & Metric Definitions", expanded=False):
    st.markdown("""
    ### How This Platform Works
    This dashboard visualizes the results of a **10,000-iteration Monte Carlo simulation**. Using a custom Poisson Distribution model, it simulates every match of the 2026 World Cup to find the true mathematical probabilities of success.
    
    **Understanding the Core Metrics:**
    * 📈 **Win Probability:** The percentage of times this team won the tournament across all 10,000 simulated realities.
    * ⚔️ **Elo Strength Rating:** A rolling mathematical score calculated from historical match results. It measures a team's traditional global dominance and pedigree.
    * 🕸️ **Network Synergy Score:** A proprietary metric derived from network graph density. It measures spatial positioning, squad chemistry, and off-ball movement. High synergy is often the key to underdog upsets.
    """)
st.markdown("---")

# ==============================================================================
# DATA INGESTION & SIDEBAR CONTROLS
# ==============================================================================
@st.cache_data
def load_data():
    try:
        return pd.read_csv("world_cup_2026_forecast_10k.csv")
    except FileNotFoundError:
        return pd.DataFrame({"Team": ["Error"], "Win Probability (%)": [0], "Elo Rating": [1500], "Tactical Synergy": [0.0]})

df = load_data()

st.sidebar.header("🎯 Team Selection Hub")
selected_team = st.sidebar.selectbox("Select a country to analyze:", df['Team'].tolist())

# AI Status Tracker in Sidebar
st.sidebar.markdown("---")
st.sidebar.header("🔑 AI Integration")
if GROQ_API_KEY:
    st.sidebar.success("🔒 Live AI active. Key loaded securely.")
else:
    st.sidebar.error("⚠️ API Key not found. Please check your .env file.")

# ==============================================================================
# TOP TIER: MACRO VISUALIZATIONS
# ==============================================================================
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("Global Win Probability")
    df_plot = df[df['Win Probability (%)'] >= 0.1].copy()
    fig_bar = px.bar(df_plot, x='Win Probability (%)', y='Team', orientation='h', color='Win Probability (%)', color_continuous_scale='Viridis', text='Win Probability (%)')
    opacities = [1.0 if team == selected_team else 0.25 for team in df_plot['Team']]
    fig_bar.update_traces(marker_opacity=opacities, texttemplate='%{text:.2f}%', textposition='outside', cliponaxis=False)
    fig_bar.update_layout(yaxis={'categoryorder': 'total ascending', 'dtick': 1}, height=550, margin=dict(l=10, r=50, t=40, b=10))
    st.plotly_chart(fig_bar, use_container_width=True, theme="streamlit")

with col_chart2:
    st.subheader("Elo vs. Synergy Landscape")
    fig_scatter = px.scatter(df, x='Elo Rating', y='Tactical Synergy', size='Win Probability (%)', color='Win Probability (%)', color_continuous_scale='Viridis', hover_name='Team', size_max=40)
    sel_data = df[df['Team'] == selected_team].iloc[0]
    fig_scatter.add_annotation(x=sel_data['Elo Rating'], y=sel_data['Tactical Synergy'], text=f"🎯 {selected_team}", showarrow=True, arrowhead=2, arrowsize=1.5, arrowcolor="#888888", font=dict(color="#888888", size=14))
    fig_scatter.update_layout(height=550, margin=dict(l=10, r=50, t=40, b=10))
    st.plotly_chart(fig_scatter, use_container_width=True, theme="streamlit")

st.markdown("---")

# ==============================================================================
# BOTTOM TIER: ISOLATED METRICS
# ==============================================================================
st.subheader(f"📊 {selected_team} Tactical Profile & AI Analysis")

m1, m2, m3 = st.columns(3)
win_prob = sel_data['Win Probability (%)']
elo_rating = int(sel_data['Elo Rating'])
synergy = round(sel_data['Tactical Synergy'], 4)

m1.metric("Tournament Win Probability", f"{win_prob}%")
m2.metric("Elo Strength Rating", elo_rating)
m3.metric("Network Synergy Score", synergy)

st.markdown("<br>", unsafe_allow_html=True)

# ==============================================================================
# LIVE AI INFERENCE LOGIC (CACHED)
# ==============================================================================
@st.cache_data(show_spinner=False)
def generate_live_debate(team, wp, elo, syn, api_key):
    """Hits the Groq API to generate team-specific analysis. Cached for speed."""
    try:
        client = Groq(api_key=api_key)
        
        # 1. Quant Prompt
        q_prompt = f"Act as a strict quantitative sports analyst. Analyze {team}'s chances at the 2026 World Cup. They have a Win Probability of {wp}% and an Elo of {elo}. Explain this purely through historical data and mathematical dominance in 3 concise sentences."
        q_res = client.chat.completions.create(messages=[{"role": "user", "content": q_prompt}], model="openai/gpt-oss-120b").choices[0].message.content
        
        # 2. Scout Prompt
        s_prompt = f"Act as a rogue tactical football scout. Read this quant report: '{q_res}'. Now, analyze {team} focusing ONLY on their Tactical Synergy score of {syn}. Explain their spatial chemistry or upset potential in 3 concise sentences."
        s_res = client.chat.completions.create(messages=[{"role": "user", "content": s_prompt}], model="meta-llama/llama-4-scout-17b-16e-instruct").choices[0].message.content
        
        # 3. Editor Prompt
        e_prompt = f"Act as the Chief Editor. Synthesize these two views on {team}. Quant: '{q_res}'. Scout: '{s_res}'. Give a 2-sentence final executive verdict on their tournament outlook."
        e_res = client.chat.completions.create(messages=[{"role": "user", "content": e_prompt}], model="llama-3.3-70b-versatile").choices[0].message.content
        
        return {"quant": q_res, "scout": s_res, "editor": e_res}
    except Exception as e:
        return {"error": str(e)}

# ==============================================================================
# DYNAMIC AI UI RENDER
# ==============================================================================
if not GROQ_API_KEY:
    st.info("👈 Please ensure your .env file contains GROQ_API_KEY to unlock Live AI Debates.")
else:
    with st.spinner(f"🧠 AI Panel is actively analyzing {selected_team}..."):
        debate_data = generate_live_debate(selected_team, win_prob, elo_rating, synergy, GROQ_API_KEY)
        
        if "error" in debate_data:
            st.error(f"API Error: {debate_data['error']}. Check your API key or model availability.")
        else:
            col_q, col_s = st.columns(2)
            with col_q:
                with st.container(border=True):
                    st.subheader("🤖 The Quant Analyst", divider="blue")
                    st.caption("**Model:** openai/gpt-oss-120b | **Focus:** Pure Elo Math")
                    st.write(debate_data['quant'])
                    
            with col_s:
                with st.container(border=True):
                    st.subheader("🕵️ The Tactical Scout", divider="orange")
                    st.caption("**Model:** meta-llama/llama-4-scout | **Focus:** Synergy & Upsets")
                    st.write(debate_data['scout'])

            with st.container(border=True):
                st.subheader("📰 Executive Verdict", divider="green")
                st.caption("**Model:** llama-3.3-70b-versatile | **Focus:** Balanced Synthesis")
                st.write(debate_data['editor'])
