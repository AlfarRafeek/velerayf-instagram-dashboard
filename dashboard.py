import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="VELÉRAYF Luxury Dashboard", layout="wide")

# -------------------------------
# LUXURY THEME
# -------------------------------
st.markdown("""
    <style>
    .main {
        background-color: #0a0a0a;
        color: white;
    }
    .stMetric {
        background-color: #111111;
        padding: 15px;
        border-radius: 15px;
        border: 1px solid gold;
    }
    h1, h2, h3 {
        color: gold;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# TITLE
# -------------------------------
st.title("VELÉRAYF Instagram Performance Dashboard")
st.write("Luxury Analytics for Premium Brand Growth")

# -------------------------------
# LOAD DATA
# -------------------------------
data = pd.read_excel("instagram_data.xlsx")

# -------------------------------
# SIDEBAR FILTERS
# -------------------------------
st.sidebar.header("Filters")

post_type = st.sidebar.multiselect(
    "Select Post Type",
    data["Post Type"].unique(),
    default=data["Post Type"].unique()
)

filtered_data = data[data["Post Type"].isin(post_type)]

# -------------------------------
# KPI METRICS
# -------------------------------
total_reach = int(filtered_data["Reach"].sum())
total_engagement = int(filtered_data["Engagement"].sum())
followers = int(filtered_data["Followers"].max())
eng_rate = round((total_engagement / total_reach) * 100, 2)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Reach", total_reach)
col2.metric("Total Engagement", total_engagement)
col3.metric("Followers", followers)
col4.metric("Engagement Rate %", eng_rate)

st.markdown("---")

# -------------------------------
# CHART 1 – Reach Over Time
# -------------------------------
fig1 = px.line(
    filtered_data,
    x="Date",
    y="Reach",
    title="Reach Growth Over Time",
    markers=True
)
st.plotly_chart(fig1, use_container_width=True)

# -------------------------------
# CHART 2 – Engagement by Post Type
# -------------------------------
fig2 = px.bar(
    filtered_data,
    x="Post Type",
    y="Engagement",
    color="Post Type",
    title="Engagement by Content Type"
)
st.plotly_chart(fig2, use_container_width=True)

# -------------------------------
# CHART 3 – Likes vs Comments
# -------------------------------
fig3 = px.scatter(
    filtered_data,
    x="Likes",
    y="Comments",
    size="Shares",
    color="Post Type",
    title="Content Interaction Analysis"
)
st.plotly_chart(fig3, use_container_width=True)

# -------------------------------
# BEST & WORST POST
# -------------------------------
best_post = filtered_data.sort_values("Engagement", ascending=False).iloc[0]
worst_post = filtered_data.sort_values("Engagement").iloc[0]

col5, col6 = st.columns(2)

with col5:
    st.success("Best Performing Post")
    st.write(best_post)

with col6:
    st.error("Worst Performing Post")
    st.write(worst_post)

# -------------------------------
# DATA TABLE
# -------------------------------
st.subheader("Full Dataset")
st.dataframe(filtered_data)
