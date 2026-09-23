import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background: #5865F2 !important;
                color: #FFFFFF !important;
            }
            .stApp div[data-testid="stColumn"] {
                background-color: #E0E3FF !important;
                padding: 2.5rem !important;
                border-radius: 2.5rem !important;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15) !important;
            }
            .stApp div[data-testid="stColumn"] h1,
            .stApp div[data-testid="stColumn"] h2,
            .stApp div[data-testid="stColumn"] h3,
            .stApp div[data-testid="stColumn"] p {
                color: #0F172A !important;
                font-weight: 700 !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: #E0E3FF !important;
                color: #0F172A !important;
            }

            /* Universal High-Contrast Text for Dashboard */
            .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {
                color: #0F172A !important;
                font-weight: 800 !important;
                letter-spacing: -0.5px !important;
            }

            .stApp p, .stApp span, .stApp div, .stApp label {
                color: #1E293B !important;
            }

            /* Widget Labels (e.g. camera, inputs, audio) */
            [data-testid="stWidgetLabel"] p,
            [data-testid="stWidgetLabel"] label,
            label[data-testid="stWidgetLabel"] {
                color: #0F172A !important;
                font-weight: 700 !important;
                font-size: 1rem !important;
            }

            /* Container cards (Bordered containers like Registration) */
            div[data-testid="stVerticalBlockBorderWrapper"] {
                background-color: #FFFFFF !important;
                border-radius: 1.5rem !important;
                padding: 1.8rem !important;
                border: 1.5px solid #CBD5E1 !important;
                box-shadow: 0 10px 30px rgba(88, 101, 242, 0.08) !important;
            }

            div[data-testid="stVerticalBlockBorderWrapper"] h1,
            div[data-testid="stVerticalBlockBorderWrapper"] h2,
            div[data-testid="stVerticalBlockBorderWrapper"] h3,
            div[data-testid="stVerticalBlockBorderWrapper"] h4,
            div[data-testid="stVerticalBlockBorderWrapper"] p,
            div[data-testid="stVerticalBlockBorderWrapper"] label,
            div[data-testid="stVerticalBlockBorderWrapper"] span {
                color: #0F172A !important;
            }

            /* Input Fields (Text input, password, etc.) */
            .stTextInput input {
                background-color: #F8FAFC !important;
                color: #0F172A !important;
                border: 2px solid #CBD5E1 !important;
                border-radius: 0.8rem !important;
                font-size: 1rem !important;
                font-weight: 600 !important;
                padding: 10px 16px !important;
            }

            .stTextInput input:focus {
                border-color: #5865F2 !important;
                background-color: #FFFFFF !important;
                box-shadow: 0 0 0 3px rgba(88, 101, 242, 0.25) !important;
            }

            /* Select boxes */
            .stSelectbox div[data-baseweb="select"] > div {
                background-color: #FFFFFF !important;
                color: #0F172A !important;
                border: 2px solid #CBD5E1 !important;
                border-radius: 0.8rem !important;
            }

            /* Informational / Alert Boxes */
            .stAlert {
                border-radius: 1rem !important;
                border: 1px solid #CBD5E1 !important;
            }
            .stAlert p {
                font-weight: 600 !important;
                font-size: 0.95rem !important;
                color: #1E293B !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&display=swap');

            /* Hide Streamlit Top Bar & Footers */
            #MainMenu, footer, header {
                visibility: hidden;
            }

            .block-container {
                padding-top: 1.5rem !important;
                max-width: 1050px !important;
            }

            /* Clean, modern typography */
            html, body, [class*="css"], .stApp {
                font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
            }

            h1 {
                font-size: 2.6rem !important;
                font-weight: 800 !important;
                line-height: 1.2 !important;
                margin-bottom: 0.5rem !important;
            }

            h2 {
                font-size: 1.9rem !important;
                font-weight: 700 !important;
                line-height: 1.25 !important;
                margin-bottom: 0.5rem !important;
            }

            h3 {
                font-size: 1.35rem !important;
                font-weight: 700 !important;
                margin-bottom: 0.3rem !important;
            }

            h4, p {
                font-size: 1.05rem !important;
                line-height: 1.5 !important;
            }

            /* High visibility buttons */
            button {
                border-radius: 1.2rem !important;
                background-color: #5865F2 !important;
                color: #FFFFFF !important;
                font-weight: 700 !important;
                font-size: 1rem !important;
                padding: 10px 22px !important;
                border: none !important;
                transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out !important;
            }

            button[kind="secondary"] {
                background-color: #EB459E !important;
                color: #FFFFFF !important;
            }

            button[kind="tertiary"] {
                background-color: #0F172A !important;
                color: #FFFFFF !important;
            }

            button:hover {
                transform: scale(1.03) !important;
                box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15) !important;
            }
        </style>
    """, unsafe_allow_html=True)