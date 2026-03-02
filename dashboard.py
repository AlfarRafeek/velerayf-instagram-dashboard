import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="VELÊRAYF Instagram Dashboard", layout="wide")

# ── Clean white/blue Instagram Insights style ─────────────────────────
st.markdown("""
    <style>
    .main {background-color: #ffffff;}
    h1, h2, h3 {color: #000000; font-family: -apple-system, BlinkMacSystemFont, sans-serif;}
    .stMetric {background: #f8fafc; border-radius: 12px; padding: 16px; border: 1px solid #e2e8f0;}
    .highlight-green {color: #16a34a; font-weight: 600;}
    .card {
        background: white;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        border: 1px solid #e2e8f0;
    }
    </style>
""", unsafe_allow_html=True)

st.title("VELÊRAYF Instagram Insights")
st.caption("Last 30 days • March 2026 • @velerayf")

# ── Top content formats section ───────────────────────────────────────
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

# Blue bars
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

# ── Views line chart section ──────────────────────────────────────────
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("Views")

# Big number + green arrow
col_left, col_right = st.columns([2, 5])

with col_left:
    st.markdown("""
        <div style="font-size: 48px; font-weight: 800; color: #1e40af;">
            5.6K
        </div>
        <div class="highlight-green" style="font-size: 20px; margin-top: 4px;">
            ↑ 965.1%
        </div>
    """, unsafe_allow_html=True)

with col_right:
    # Fake dates & values based on your screenshot pattern
    dates = pd.date_range(start="2026-02-02", end="2026-02-27", freq="3D")
    views = [50, 120, 80, 350, 200, 520, 300, 680, 450, 950, 820]  # approximate curve

    df_views = pd.DataFrame({"Date": dates[:len(views)], "Views": views})

    fig_views = px.line(
        df_views,
        x="Date",
        y="Views",
        markers=True,
        color_discrete_sequence=["#60a5fa"],
        height=280
    )
    fig_views.update_traces(line=dict(width=3), marker_size=10)
    fig_views.update_layout(
        xaxis_title=None,
        yaxis_title=None,
        showlegend=False,
        margin=dict(l=20, r=20, t=20, b=20),
        yaxis=dict(range=[0, 1100]),
        xaxis=dict(tickformat="%b %d")
    )
    st.plotly_chart(fig_views, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("© 2026 Instagram Insights • VELÊRAYF • Built with Streamlit")
