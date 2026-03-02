import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="VELÊRAYF Insights", layout="wide")

# ── Bright colorful theme ─────────────────────────────────────────────
st.markdown("""
    <style>
    .main {background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);}
    h1 {color: #1e40af; text-align: center; font-weight: bold;}
    .metric-card {
        background: white;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.1);
        text-align: center;
        border: 1px solid #e5e7eb;
    }
    .metric-value {font-size: 2.5rem; font-weight: 800; color: #1d4ed8;}
    .metric-title {font-size: 1rem; color: #64748b; margin-bottom: 8px;}
    </style>
""", unsafe_allow_html=True)

st.title("VELÊRAYF Account Insights")
st.markdown("<p style='text-align:center; color:#64748b;'>Last 30 days • March 2026 • @velerayf</p>", unsafe_allow_html=True)

# ── Metric cards ──────────────────────────────────────────────────────
cols = st.columns(4)

metrics = [
    ("Views", "5,464", "#eab308"),
    ("Accounts Reached", "898", "#f97316"),
    ("Profile Visits", "527", "#06b6d4"),
    ("Followers", "130", "#84cc16")
]

for col, (label, value, color) in zip(cols, metrics):
    with col:
        st.markdown(f"""
        <div class="metric-card" style="border-top: 5px solid {color};">
            <div class="metric-title">{label}</div>
            <div class="metric-value">{value}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# ── Views section ─────────────────────────────────────────────────────
st.subheader("Views")

col_left, col_right = st.columns([1.3, 3.7])

with col_left:
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=40.6,
        number={'font': {'size': 50, 'color': '#1e40af'}},
        title={'text': "Followers %", 'font': {'size': 20}},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#3b82f6"},
            'bgcolor': "#e5e7eb",
            'steps': [
                {'range': [0, 40.6], 'color': 'rgba(59,130,246,0.35)'},
                {'range': [40.6, 100], 'color': 'rgba(200,200,200,0.3)'}
            ]
        }
    ))
    fig_gauge.update_layout(height=240, margin=dict(l=0,r=0,t=30,b=0))
    st.plotly_chart(fig_gauge, use_container_width=True)
    st.caption("Non-followers: 59.4%")

with col_right:
    content_df = pd.DataFrame({
        "Type": ["Posts", "Reels", "Stories"],
        "Percentage": [46.5, 46.1, 7.4]
    })

    fig_bar = px.bar(
        content_df,
        x="Percentage",
        y="Type",
        orientation="h",
        text_auto=True,
        title="By content type",
        color="Type",
        color_discrete_sequence=["#ec4899", "#8b5cf6", "#f43f5e"]
    )
    fig_bar.update_traces(textposition="auto", textfont_size=14)
    fig_bar.update_layout(
        xaxis_title=None,
        yaxis_title=None,
        showlegend=False,
        height=280,
        margin=dict(l=20,r=20,t=50,b=20),
        plot_bgcolor="rgba(255,255,255,0.6)",
        paper_bgcolor="rgba(0,0,0,0)"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# ── Top content cards ─────────────────────────────────────────────────
st.markdown("---")
st.subheader("Top content based on views")

top_posts = [
    {"views":709, "date":"Feb 28", "label":"Giveaway – Elevate Your Style", "color":"#ec4899"},
    {"views":630, "date":"Feb 13", "label":"Blue sapphire earring",         "color":"#8b5cf6"},
    {"views":517, "date":"Feb 9",  "label":"Green emerald ring",            "color":"#06b6d4"},
    {"views":478, "date":"Feb 17", "label":"Necklace / Reel",               "color":"#84cc16"},
    {"views":410, "date":"Jan 28", "label":"Post – early content",          "color":"#eab308"}
]

cols = st.columns(5)
for col, post in zip(cols, top_posts):
    with col:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, {post['color']}22 0%, white 100%);
            border-radius: 16px;
            padding: 16px 12px;
            text-align: center;
            box-shadow: 0 8px 25px rgba(0,0,0,0.08);
            border: 1px solid {post['color']}40;
            min-height: 180px;
        ">
            <div style="font-size: 2.8rem; font-weight: 900; color: #1e40af;">{post['views']}</div>
            <div style="font-size: 0.9rem; color: #64748b; margin: 4px 0;">{post['date']}</div>
            <div style="font-size: 0.95rem; color: #1f2937; line-height: 1.4;">
                {post['label'][:38]}{'...' if len(post['label']) > 38 else ''}
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("VELÊRAYF Dashboard • March 2026 • Colombo, Sri Lanka")
