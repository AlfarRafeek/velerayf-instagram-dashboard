import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="VELÊRAYF Insights Dashboard", layout="wide")

# ── Dark Instagram-like theme ────────────────────────────────────────
st.markdown("""
    <style>
    .main {background-color: #0f0f0f; color: white;}
    .stApp {background-color: #0f0f0f;}
    h1, h2, h3 {color: #ffffff; font-family: -apple-system, BlinkMacSystemFont, sans-serif;}
    .stMetric {background: #1a1a1a; border-radius: 12px; padding: 16px; border: 1px solid #333;}
    .block-container {padding-top: 1rem !important;}
    section[data-testid="stSidebar"] {background-color: #111;}
    </style>
""", unsafe_allow_html=True)

# ── Title ─────────────────────────────────────────────────────────────
st.title("VELÊRAYF Account Insights")
st.caption("Last 30 days • March 2026 • @velerayf")

# ── Key metrics row ───────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Views", "5,464", help="Total views in selected period")

with col2:
    st.metric("Accounts Reached", "898")

with col3:
    st.metric("Profile Visits", "527")

with col4:
    st.metric("Followers", "130")

# ── Views split (donut-like) ──────────────────────────────────────────
st.subheader("Views")
col_left, col_right = st.columns([1, 3])

with col_left:
    followers_pct = 40.6
    non_followers_pct = 59.4

    fig_views_split = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = followers_pct,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Followers"},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': "#C13584"},
            'steps': [
                {'range': [0, followers_pct], 'color': "#C13584"},
                {'range': [followers_pct, 100], 'color': "#4a4a4a"}
            ],
            'threshold': {'line': {'color': "white", 'width': 2}, 'thickness': 0.8, 'value': followers_pct}
        }
    ))
    fig_views_split.update_layout(height=180, margin=dict(l=10,r=10,t=30,b=10), template="plotly_dark")
    st.plotly_chart(fig_views_split, use_container_width=True)

    st.caption(f"Non-followers: {non_followers_pct}%")

with col_right:
    content_data = pd.DataFrame({
        "Type": ["Posts", "Reels", "Stories"],
        "Percentage": [46.5, 46.1, 7.4]
    })

    fig_content = px.bar(
        content_data,
        x="Percentage",
        y="Type",
        orientation="h",
        color="Type",
        color_discrete_sequence=["#C13584", "#833AB4", "#E1306C"],
        title="By content type",
        text_auto=True
    )
    fig_content.update_layout(
        template="plotly_dark",
        showlegend=False,
        xaxis_title=None,
        yaxis_title=None,
        height=220,
        margin=dict(l=10,r=10,t=40,b=10)
    )
    fig_content.update_traces(textposition="auto", textfont_size=14)
    st.plotly_chart(fig_content, use_container_width=True)

# ── Top content grid ──────────────────────────────────────────────────
st.subheader("Top content based on views")

top_posts = [
    {"views": 709,  "date": "Feb 28", "label": "Giveaway – Elevate Your Style", "color": "#C13584"},
    {"views": 630,  "date": "Feb 13", "label": "Blue sapphire earring",         "color": "#833AB4"},
    {"views": 517,  "date": "Feb 9",  "label": "Green emerald ring",            "color": "#E1306C"},
    {"views": 478,  "date": "Feb 17", "label": "Necklace / Reel",               "color": "#F56040"},
    {"views": 410,  "date": "Jan 28", "label": "Post – early content",          "color": "#FCAF45"}
]

cols = st.columns(5)
for i, post in enumerate(top_posts):
    with cols[i]:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, {post['color']}22, #111);
            border-radius: 12px;
            padding: 12px;
            text-align: center;
            border: 1px solid {post['color']};
        ">
            <div style="font-size: 28px; font-weight: bold; color: white;">{post['views']}</div>
            <div style="font-size: 13px; color: #aaa;">{post['date']}</div>
            <div style="font-size: 14px; margin-top: 8px;">{post['label'][:30]}{'...' if len(post['label']) > 30 else ''}</div>
        </div>
        """, unsafe_allow_html=True)

# ── Interactions section ──────────────────────────────────────────────
st.markdown("---")
st.subheader("Interactions")
col_i1, col_i2 = st.columns([1, 3])

with col_i1:
    st.metric("Total Interactions", "717")

    fig_inter_split = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 84.2,
        title = {'text': "Followers"},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': "#C13584"},
            'steps': [{'range': [0, 84.2], 'color': "#C13584"}, {'range': [84.2, 100], 'color': "#333"}]
        }
    ))
    fig_inter_split.update_layout(height=180, margin=dict(l=0,r=0,t=0,b=0), template="plotly_dark")
    st.plotly_chart(fig_inter_split, use_container_width=True)
    st.caption("Non-followers: 15.8%")

with col_i2:
    inter_content = pd.DataFrame({
        "Type": ["Posts", "Reels", "Stories"],
        "Percentage": [56.6, 43.2, 0.1]
    })

    fig_inter_bar = px.bar(
        inter_content,
        x="Percentage",
        y="Type",
        orientation="h",
        color="Type",
        color_discrete_sequence=["#C13584", "#833AB4", "#444"],
        title="By content interactions",
        text_auto=True
    )
    fig_inter_bar.update_layout(template="plotly_dark", showlegend=False, height=220, margin=dict(l=10,r=10,t=40,b=10))
    st.plotly_chart(fig_inter_bar, use_container_width=True)

# ── Active times bar ──────────────────────────────────────────────────
st.markdown("---")
st.subheader("Most active times")

hours = ["12a","3a","6a","9a","12p","3p","6p","9p"]
values = [36,38,36,33,14,15,26,35]

fig_active = go.Figure()
fig_active.add_trace(go.Bar(
    y=hours,
    x=values,
    orientation='h',
    marker_color="#C13584",
    text=values,
    textposition='auto'
))
fig_active.update_layout(
    title="Followers activity by hour",
    xaxis_title="Activity level",
    yaxis_title="Time of day",
    template="plotly_dark",
    height=400,
    margin=dict(l=40,r=20,t=50,b=40)
)
st.plotly_chart(fig_active, use_container_width=True)

st.caption("© 2026 Instagram Insights • VELÊRAYF • Colombo, LK")
