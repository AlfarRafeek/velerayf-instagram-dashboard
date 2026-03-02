import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="VELÊRAYF Insights", layout="wide")

# ── Colorful modern theme ─────────────────────────────────────────────
st.markdown("""
    <style>
    .main {background: linear-gradient(135deg, #f5f7fa 0%, #e4e9fd 100%);}
    .stApp {background: transparent;}
    h1 {color: #1e3a8a; font-family: 'Segoe UI', sans-serif; font-weight: 700;}
    .metric-card {
        background: white;
        border-radius: 16px;
        padding: 20px 24px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid #e5e7eb;
        text-align: center;
    }
    .metric-title {font-size: 14px; color: #6b7280; margin-bottom: 8px;}
    .metric-value {font-size: 32px; font-weight: 700; color: #1e40af;}
    .content-bar {height: 32px; border-radius: 999px; overflow: hidden; margin: 8px 0;}
    </style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────
st.markdown("<h1 style='text-align:center; margin-bottom:8px;'>VELÊRAYF Account Insights</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#4b5563; font-size:15px;'>Last 30 days • March 2026 • @velerayf</p>", unsafe_allow_html=True)

# ── Main metrics cards ────────────────────────────────────────────────
cols = st.columns(4)

with cols[0]:
    st.markdown("""
    <div class="metric-card" style="border-left: 5px solid #eab308;">
        <div class="metric-title">Views</div>
        <div class="metric-value">5,464</div>
    </div>
    """, unsafe_allow_html=True)

with cols[1]:
    st.markdown("""
    <div class="metric-card" style="border-left: 5px solid #f97316;">
        <div class="metric-title">Accounts Reached</div>
        <div class="metric-value">898</div>
    </div>
    """, unsafe_allow_html=True)

with cols[2]:
    st.markdown("""
    <div class="metric-card" style="border-left: 5px solid #06b6d4;">
        <div class="metric-title">Profile Visits</div>
        <div class="metric-value">527</div>
    </div>
    """, unsafe_allow_html=True)

with cols[3]:
    st.markdown("""
    <div class="metric-card" style="border-left: 5px solid #84cc16;">
        <div class="metric-title">Followers</div>
        <div class="metric-value">130</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Views section ─────────────────────────────────────────────────────
st.subheader("Views")

col_gauge, col_bar = st.columns([1.2, 3])

with col_gauge:
    followers_pct = 40.6
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = followers_pct,
        number = {'font': {'size': 48, 'color': '#1e40af'}},
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Followers %", 'font': {'size': 18}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#1e40af"},
            'bar': {'color': "#3b82f6"},
            'bgcolor': "lightgray",
            'borderwidth': 2,
            'steps': [
                {'range': [0, followers_pct], 'color': 'rgba(59,130,246,0.4)'},
                {'range': [followers_pct, 100], 'color': 'rgba(200,200,200,0.3)'}
            ]
        }
    ))
    fig_gauge.update_layout(height=220, margin=dict(l=0,r=0,t=20,b=0))
    st.plotly_chart(fig_gauge, use_container_width=True)
    st.caption(f"Non-followers: 59.4%")

with col_bar:
    content_data = pd.DataFrame({
        "Type": ["Posts", "Reels", "Stories"],
        "Percentage": [46.5, 46.1, 7.4],
        "Color": ["#ec4899", "#8b5cf6", "#f43f5e"]
    })

    fig_bar = px.bar(
        content_data,
        x="Percentage",
        y="Type",
        orientation="h",
        color="Type",
        color_discrete_sequence=content_data["Color"],
        text_auto=True,
        title="By content type"
    )
    fig_bar.update_traces(textposition="auto", textfont_size=14, marker_line_width=0)
    fig_bar.update_layout(
        xaxis_title=None,
        yaxis_title=None,
        showlegend=False,
        height=260,
        margin=dict(l=20,r=20,t=40,b=20),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# ── Top content cards ─────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("Top content based on views")

top_data = [
    {"views":709, "date":"Feb 28", "label":"Giveaway – Elevate Your Style", "color":"#ec4899"},
    {"views":630, "date":"Feb 13", "label":"Blue sapphire earring",         "color":"#8b5cf6"},
    {"views":517, "date":"Feb 9",  "label":"Green emerald ring",            "color":"#06b6d4"},
    {"views":478, "date":"Feb 17", "label":"Necklace / Reel",               "color":"#84cc16"},
    {"views":410, "date":"Jan 28", "label":"Post – early content",          "color":"#eab308"}
]

cols = st.columns(5)
for i, item in enumerate(top_data):
    with cols[i]:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, {item['color']}22 0%, white 100%);
            border-radius: 16px;
            padding: 16px;
            text-align: center;
            box-shadow: 0 6px 20px rgba(0,0,0,0.08);
            border: 1px solid {item['color']}44;
        ">
            <div style="font-size: 36px; font-weight: 800; color: #1e40af;">{item['views']}</div>
            <div style="font-size: 13px; color: #6b7280; margin: 4px 0;">{item['date']}</div>
            <div style="font-size: 14px; color: #374151; line-height: 1.3;">
                {item['label'][:38]}{'...' if len(item['label']) > 38 else ''}
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("Dashboard built for VELÊRAYF • March 2026 • Colombo, LK")
