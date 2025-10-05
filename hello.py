import streamlit as st
import subprocess
import sys
import os

# Install Playwright browsers on first run
if not os.path.exists('/home/adminuser/.cache/ms-playwright'):
    subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"])
    subprocess.run([sys.executable, "-m", "playwright", "install-deps", "chromium"])
    

st.title("Dependency Diagnostic Test")
st.write("Testing each import to find what's breaking...")

# Test 1: Basic imports
try:
    import pandas as pd
    st.write("✅ pandas")
except Exception as e:
    st.write(f"❌ pandas: {e}")

try:
    import numpy as np
    st.write("✅ numpy")
except Exception as e:
    st.write(f"❌ numpy: {e}")

try:
    import psycopg2
    st.write("✅ psycopg2-binary")
except Exception as e:
    st.write(f"❌ psycopg2-binary: {e}")

try:
    from playwright.sync_api import sync_playwright
    st.write("✅ playwright imported")
    # Try to actually use it
    st.write("⚠️ Playwright imported but browsers NOT installed yet")
except Exception as e:
    st.write(f"❌ playwright: {e}")

try:
    from bs4 import BeautifulSoup
    st.write("✅ beautifulsoup4")
except Exception as e:
    st.write(f"❌ beautifulsoup4: {e}")

try:
    import requests
    st.write("✅ requests")
except Exception as e:
    st.write(f"❌ requests: {e}")

try:
    import openpyxl
    st.write("✅ openpyxl")
except Exception as e:
    st.write(f"❌ openpyxl: {e}")

try:
    from apscheduler.schedulers.background import BackgroundScheduler
    st.write("✅ APScheduler")
except Exception as e:
    st.write(f"❌ APScheduler: {e}")

try:
    import flask
    st.write("✅ Flask")
except Exception as e:
    st.write(f"❌ Flask: {e}")

try:
    from flask_cors import CORS
    st.write("✅ flask-cors")
except Exception as e:
    st.write(f"❌ flask-cors: {e}")

try:
    import sqlalchemy
    st.write("✅ SQLAlchemy")
except Exception as e:
    st.write(f"❌ SQLAlchemy: {e}")

try:
    import pdfkit
    st.write("✅ pdfkit")
    st.write("⚠️ pdfkit needs wkhtmltopdf binary")
except Exception as e:
    st.write(f"❌ pdfkit: {e}")

try:
    import pdfkit
    # Try to find wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
    st.write("✅ pdfkit + wkhtmltopdf binary found")
except Exception as e:
    st.write(f"❌ pdfkit binary test: {e}")

try:
    import weasyprint
    st.write("✅ weasyprint")
except Exception as e:
    st.write(f"❌ weasyprint: {e}")

try:
    import reportlab
    st.write("✅ reportlab")
except Exception as e:
    st.write(f"❌ reportlab: {e}")

try:
    import trafilatura
    st.write("✅ trafilatura")
except Exception as e:
    st.write(f"❌ trafilatura: {e}")

try:
    import lxml
    st.write("✅ lxml")
except Exception as e:
    st.write(f"❌ lxml: {e}")

try:
    from PIL import Image
    st.write("✅ pillow")
except Exception as e:
    st.write(f"❌ pillow: {e}")

try:
    import git
    st.write("✅ GitPython")
except Exception as e:
    st.write(f"❌ GitPython: {e}")

try:
    import altair as alt
    st.write("✅ altair")
except Exception as e:
    st.write(f"❌ altair: {e}")

st.write("---")
st.write("Test complete! If you see this, Streamlit is working.")