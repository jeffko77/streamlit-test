import streamlit as st
import playwright

# Test each import individually
try:
    from playwright.sync_api import sync_playwright
    st.write("✅ Playwright works")
except Exception as e:
    st.write(f"❌ Playwright failed: {e}")