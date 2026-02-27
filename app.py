import streamlit as st
import random
import time
import plotly.graph_objects as go

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="Futurio - See Your Future",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================
# STATE MANAGEMENT
# ==============================
def initialize_state():
    if "page" not in st.session_state:
        st.session_state.page = "home"
    if "analysis_done" not in st.session_state:
        st.session_state.analysis_done = False
    if "scores" not in st.session_state:
        st.session_state.scores = {}

initialize_state()

# ==============================
# UI SETUP (CSS + FONTS + EFFECTS)
# ==============================
def setup_ui():
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Playfair+Display:ital@1&display=swap" rel="stylesheet">
    <style>

    html, body, [class*="css"] {
        font-family: sans-serif;
        background: radial-gradient(circle at center, #0f172a 0%, #020617 100%);
        color: #FFFFFF !important;
    }

    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif;
        color: #FFFFFF !important;
        text-shadow: 0 0 10px rgba(0,242,255,0.5);
    }

    /* NAVBAR */
    .navbar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        padding: 10px 40px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: transparent;
        z-index: 999;
    }

    .logo-circle {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        border: 2px solid #00f2ff;
        box-shadow: 0 0 20px #00f2ff;
        position: relative;
    }

    .logo-circle::after {
        content: "";
        position: absolute;
        top: 8px;
        left: 8px;
        width: 20px;
        height: 20px;
        border-radius: 50%;
        border: 2px solid #9333ea;
        box-shadow: 0 0 10px #9333ea;
    }

    /* GLASS CARD */
    .glass {
        background: rgba(255
