# 🏆 2026 World Cup Hybrid Intelligence Engine

![Live Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Cloud-FF4B4B)
![Groq](https://img.shields.io/badge/LLM-Groq_API-black)

## Read The Report

https://k-ashik.github.io/fifa_world_cup_2026_simulation_forecast/

## 📌 Executive Summary
This project is an advanced sports analytics platform that forecasts the 2026 FIFA World Cup. It breaks away from traditional prediction models by combining a **mathematical Monte Carlo simulator** with a **Multi-Agent LLM inference layer**. 

Instead of just presenting sterile probabilities, the dashboard dynamically generates a live debate between heterogeneous AI agents (a Quant Analyst, a Tactical Scout, and an Executive Editor) to explain the *why* behind the numbers.

## 🏗️ System Architecture

The pipeline consists of three distinct layers:

1. **The Data Ingestion Layer (API-Football)**
   * Dynamically fetches completed real-world tournament matches to update the simulation baseline in real-time.
2. **The Predictive Engine (Phase 1-5)**
   * A Python-based Monte Carlo simulator running 10,000 tournament iterations.
   * Utilizes an adjusted Poisson distribution matrix.
3. **The AI Presentation Layer (Streamlit & Groq)**
   * A responsive front-end UI displaying interactive Plotly visualizations.
   * Real-time inference using `@st.cache_data` to generate team-specific tactical briefings without exhausting API rate limits.

## 🧮 Mathematical Methodology

The Poisson distribution for Expected Goals (xG) is modified by four custom metrics:

* **Historical Pedigree (Elo Rating):** A dynamic rating updated post-match, measuring global dominance.
* **Tactical Synergy Score:** A proprietary network-graph metric evaluating squad chemistry and positional familiarity.
* **Form Momentum Multiplier:** An exponential time-decay algorithm heavily weighting a team's last 10 matches.
* **Continental Climate Advantage:** A 5% xG boost applied to CONCACAF/CONMEBOL teams adapted to the altitude and travel demands of the North American host nations, paired with a slight travel penalty for overseas teams.

## 🤖 The Multi-Agent LLM Panel

The dashboard leverages the Groq API for near-instant inference, utilizing three distinct models prompted with unique personas:
* **The Quant Analyst (`gpt-oss-120b`):** Focuses strictly on Elo differentials and win probabilities.
* **The Tactical Scout (`llama-4-scout`):** Ignores the math, focusing purely on the Synergy score and spatial upset potential.
* **The Executive Editor (`llama-3.3-70b-versatile`):** Synthesizes the quantitative and qualitative reports into a final executive verdict.

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/K-Ashik/fifa_world_cup_2026_simulation_forecast.git

## ⚠️ System Limitations & Future Work
While highly robust, the current model assumes a static injury roster. Future iterations would benefit from integrating live player-level xG/xA data and an "Impact Player Penalty" metric to account for squad attrition immediately prior to the tournament.
