import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="VELÊRAYF Insights Dashboard", layout="wide")

# ── Light blue Instagram-like theme ───────────────────────────────────
st.markdown("""
    <style>
    .main {background-color: #ffffff; color: #000000;}
    h1, h2 {color: #000000; font-family: -apple-system, BlinkMacSystemFont, sans-serif;}
    .stPlotlyChart {background-color: #ffffff;}
    .css-1aumxhk {background-color: #f0f2f6; border-radius: 8px; padding: 16px;}
    </style>
""", unsafe_allow_html=True)

# ── Load data (user replace with actual file paths) ────────────────────
# For demo, hard-coded from your CSVs. Replace with pd.read_csv('your_file.csv')
posts_data = {
    'Date': pd.to_datetime(['2026-02-28', '2026-02-13', '2026-02-09', '2026-02-17', '2026-01-28', '2026-02-28', '2026-02-25', '2026-02-25', '2026-02-24', '2026-02-24', '2026-02-24', '2026-02-24', '2026-02-22', '2026-02-22', '2026-02-17', '2026-02-17', '2026-02-13', '2026-02-13', '2026-02-09', '2026-01-28', '2026-01-28']),
    'Post Type': ['IG image', 'IG image', 'IG image', 'IG reel', 'IG image', 'IG reel', 'IG image', 'IG image', 'IG image', 'IG reel', 'IG reel', 'IG image', 'IG reel', 'IG reel', 'IG reel', 'IG reel', 'IG reel', 'IG image', 'IG image', 'IG reel', 'IG image'],
    'Views': [716, 630, 517, 489, 410, 367, 227, 214, 269, 171, 189, 156, 249, 194, 489, 412, 320, 630, 517, 427, 192],
}
df = pd.DataFrame(posts_data)
df['Date'] = df['Date'].dt.date  # Simplify to date only

stories_data = {
    'Date': pd.to_datetime(['2026-01-28', '2026-02-28', '2026-02-28', '2026-02-18', '2026-02-17', '2026-02-17', '2026-02-13']),
    'Post Type': ['IG story'] * 7,
    'Views': [35, 49, 216, 40, 34, 36, 45],
}
df_stories = pd.DataFrame(stories_data)
df_stories['Date'] = df_stories['Date'].dt.date

# Combine all
df_all = pd.concat([df, df_stories], ignore_index=True)

# ── Top Content Formats ───────────────────────────────────────────────
st.subheader("Top content formats")

# Content count bar
content_count = df_all['Post Type'].value_counts().reset_index()
content_count.columns = ['Type', 'Count']
content_count = content_count[content_count['Type'].isin(['IG image', 'IG reel', 'IG story'])]  # Filter relevant
content_count['Type'] = content_count['Type'].replace({'IG image': 'Posts', 'IG reel': 'Reels', 'IG story': 'Stories'})

fig_content = px.bar(
    content_count,
    x='Count',
    y='Type',
    orientation='h',
    text='Count',
    color_discrete_sequence=['#3182ce'] * len(content_count),
    height=200
)
fig_content.update_traces(textposition='auto', textfont_size=14)
fig_content.update_layout(
    xaxis_title=None,
    yaxis_title=None,
    showlegend=False,
    margin=dict(l=0, r=0, t=0, b=0),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)"
)
st.plotly_chart(fig_content, use_container_width=True)

# ── Published info ────────────────────────────────────────────────────
total_posts = len(df_all)
st.markdown(f"<div style='color: #16a34a; font-size: 14px;'>+100.0% vs. Dec 17, 2025 - Jan 23, ...</div>", unsafe_allow_html=True)
st.markdown(f"Published up to {total_posts} pieces of content", style="font-size: 16px; color: #1f2937;")

# ── Views Line Chart ──────────────────────────────────────────────────
st.subheader("Views")

views_by_date = df_all.groupby('Date')['Views'].sum().reset_index()

fig_views = px.line(
    views_by_date,
    x='Date',
    y='Views',
    markers=True,
    color_discrete_sequence=['#60a5fa'],
    height=300
)
fig_views.update_traces(line=dict(width=3))
fig_views.update_layout(
    xaxis_title=None,
    yaxis_title=None,
    showlegend=False,
    margin=dict(l=0, r=0, t=0, b=0),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)"
)
st.plotly_chart(fig_views, use_container_width=True)
