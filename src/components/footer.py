import streamlit as st


def footer_home():
    st.markdown("""
        <div style="margin-top:2.5rem; margin-bottom:1rem; display:flex; gap:8px; justify-content:center; align-items:center;">
            <p style="font-weight:600; font-size:1.05rem; color:#FFFFFF; margin:0;">
                Created with ❤️ by <span style="color:#FFE066; font-weight:800; letter-spacing:0.5px;">Subham Acharya</span>
            </p>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <div style="margin-top:2.5rem; margin-bottom:1rem; display:flex; gap:8px; justify-content:center; align-items:center;">
            <p style="font-weight:600; font-size:1.05rem; color:#1e293b; margin:0;">
                Created with ❤️ by <span style="color:#5865F2; font-weight:800; letter-spacing:0.5px;">Subham Acharya</span>
            </p>
        </div>
    """, unsafe_allow_html=True)
