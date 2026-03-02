import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="VELÊRAYF Instagram Insights", layout="wide")

# ── Clean & colorful Instagram Insights style ─────────────────────────
st.markdown("""
    <style>
    .main {background-color: #ffffff;}
    h1, h2, h3 {color: #000000; font-family: -apple-system, BlinkMacSystemFont, sans-serif;}
    .card {
        background: white;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid #e2e8f0;
        margin-bottom: 24px;
    }
    .highlight-green {color: #16a34a; font-weight: 700;}
    .metric-value {font-size: 48px; font-weight: 800; color: #1e40af;}
    .metric-label {font-size: 16px; color: #64748b; margin-top: 4px;}
    </style>
""", unsafe_allow_html=True)

st.title("VELÊRAYF Instagram Insights")
st.caption("Last 30 days • March 2026 • @velerayf")

# ── Top content formats section ───────────────────────────────────────
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    st.subheader("Top content formats")
    
    st.markdown("""
        <div style="font-size: 15px; color: #64748b; margin-bottom: 8px;">
            Published up to <strong>200</strong> pieces of content
        </div>
        <div class="highlight-green" style="font-size: 14px; margin-bottom: 16px;">
            +100.0% vs. Dec 17, 2025 - Jan 23, ...
        </div>
    """, unsafe_allow_html=True)
    
    formats = pd.DataFrame({
        "Format": ["Posts", "Stories"],
        "Count": [17, 7]
    })
    
    fig_formats = px.bar(
        formats,
        x="Count",
        y="Format",
        orientation="h",
        text="Count",
        color_discrete_sequence=["#3b82f6"] * 2,
        height=180
    )
    fig_formats.update_traces(textposition="auto", textfont_size=14, marker_line_width=0)
    fig_formats.update_layout(
        xaxis_title=None,
        yaxis_title=None,
        showlegend=False,
        margin=dict(l=0, r=0, t=0, b=0),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)"
    )
    st.plotly_chart(fig_formats, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Views section ─────────────────────────────────────────────────────
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    st.subheader("Views")
    
    # Big number + green arrow
    col_num, col_chart = st.columns([2.5, 7.5])
    
    with col_num:
        st.markdown("""
            <div class="metric-value">5.6K</div>
            <div class="highlight-green" style="font-size: 24px; margin-top: 8px;">
                ↑ 965.1%
            </div>
            <div class="metric-label">Views</div>
        """, unsafe_allow_html=True)
    
    with col_chart:
        # Exact dates from your screenshot (Feb 2 → Feb 27)
        dates = pd.to_datetime([
            "2026-02-02", "2026-02-07", "2026-02-12", "2026-02-17",
            "2026-02-22", "2026-02-27"
        ])
        
        # Approximate values matching the peaks and shape in your screenshot
        views = [120, 80, 350, 520, 300, 950]  # ends high around 5.6K total
        
        df_views = pd.DataFrame({"Date": dates, "Views": views})
        
        fig_views = px.line(
            df_views,
            x="Date",
            y="Views",
            markers=True,
            color_discrete_sequence=["#60a5fa"],
            height=320
        )
        fig_views.update_traces(line=dict(width=3), marker_size=10)
        fig_views.update_layout(
            xaxis_title=None,
            yaxis_title=None,
            showlegend=False,
            margin=dict(l=20, r=20, t=20, b=20),
            yaxis=dict(range=[0, 1100], tickvals=[0, 500, 1000], ticktext=["0", "500", "1K"]),
            xaxis=dict(tickformat="%b %d")
        )
        st.plotly_chart(fig_views, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("© 2026 Instagram Insights • VELÊRAYF • Colombo, Sri Lanka • Built with Streamlit")
