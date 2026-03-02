import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import base64  # For potential image handling if you add thumbnails

# Set page config for wide layout and theme
st.set_page_config(
    page_title="VELÊRAYF Advanced Instagram Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for luxury theme (black/gold)
st.markdown("""
    <style>
    .main {background-color: #000000; color: #FFFFFF;}
    .stMetric {color: #D4AF37;}
    .stButton > button {background-color: #D4AF37; color: #000000;}
    .sidebar .sidebar-content {background-color: #1A1A1A;}
    h1, h2, h3 {color: #D4AF37; font-family: 'Cinzel', serif;}
    </style>
""", unsafe_allow_html=True)

# ───────────────────────────────────────────────
# Sidebar: Data Upload & Filters
# ───────────────────────────────────────────────
st.sidebar.title("Dashboard Controls")
uploaded_file = st.sidebar.file_uploader("Upload instagram_data.xlsx", type=["xlsx", "csv"])

if uploaded_file is not None:
    if uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
    else:
        df = pd.read_csv(uploaded_file)
    df['Date'] = pd.to_datetime(df['Date'])
    st.sidebar.success(f"Loaded {len(df)} posts!")
else:
    # Advanced sample data (expanded with more rows for demo)
    data = {
        'Date': pd.date_range(start='2026-01-24', periods=17, freq='D'),
        'Post Type': ['Post', 'Image', 'Image', 'Reel', 'Reel', 'Post', 'Story', 'Carousel', 'Reel', 'Post', 'Image', 'Reel', 'Post', 'Story', 'Image', 'Reel', 'Post'],
        'Reach': [500, 600, 550, 700, 650, 800, 200, 400, 750, 900, 630, 517, 489, 150, 427, 366, 707],
        'Engagement': [50, 60, 55, 70, 65, 80, 20, 40, 75, 90, 63, 52, 49, 15, 43, 37, 105],
        'Likes': [19, 20, 18, 25, 22, 30, 5, 15, 28, 35, 21, 19, 17, 3, 16, 12, 19],
        'Comments': [3, 4, 2, 5, 3, 6, 1, 2, 4, 7, 3, 2, 1, 0, 2, 1, 3],
        'Shares': [81, 85, 80, 90, 88, 95, 10, 30, 92, 100, 86, 82, 78, 5, 79, 70, 81],
        'Followers': [130, 128, 126, 124, 122, 120, 118, 116, 114, 112, 110, 108, 106, 104, 102, 100, 98],
        'Country': ['Sri Lanka'] * 17,
        'City': ['Colombo'] * 17
    }
    df = pd.DataFrame(data)
    st.sidebar.info("Using sample data. Upload your file for real insights!")

# Filters
st.sidebar.subheader("Filters")
min_date = df['Date'].min()
max_date = df['Date'].max()
date_range = st.sidebar.date_input("Date Range", (min_date, max_date))
post_types = st.sidebar.multiselect("Post Types", options=df['Post Type'].unique(), default=df['Post Type'].unique())

# Apply filters
df_filtered = df[(df['Date'] >= pd.to_datetime(date_range[0])) & (df['Date'] <= pd.to_datetime(date_range[1]))]
df_filtered = df_filtered[df_filtered['Post Type'].isin(post_types)]

# ───────────────────────────────────────────────
# Main Content: Multipage-like Tabs
# ───────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Overview", "📊 Performance Charts", "🖼️ Top Content", "👥 Audience Insights"])

with tab1:
    st.header("Key Metrics Overview")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    total_views = df_filtered['Views'].sum() if 'Views' in df_filtered else df_filtered['Reach'].sum()  # Fallback to Reach if no Views
    avg_engagement = df_filtered['Engagement'].mean()
    total_reach = df_filtered['Reach'].sum()
    follower_growth = df_filtered['Followers'].max() - df_filtered['Followers'].min()
    top_city = df_filtered['City'].mode()[0] if not df_filtered.empty else "N/A"
    
    col1.metric("Total Views/Reach", f"{total_views:,}")
    col2.metric("Avg Engagement", f"{avg_engagement:.1f}")
    col3.metric("Total Reach", f"{total_reach:,}")
    col4.metric("Follower Growth", f"+{follower_growth}")
    col5.metric("Top City", top_city)

    st.subheader("Quick Summary")
    st.markdown("Your luxury jewellery posts with giveaways drive high shares. Non-followers contribute 61%, indicating strong organic discovery.")

with tab2:
    st.header("Advanced Performance Visuals")
    
    # 1. Follower Growth Line + Area
    fig_followers = go.Figure()
    fig_followers.add_trace(go.Scatter(x=df_filtered['Date'], y=df_filtered['Followers'], mode='lines+markers', name='Followers', line=dict(color='#D4AF37')))
    fig_followers.add_trace(go.Scatter(x=df_filtered['Date'], y=df_filtered['Followers'], fill='tozeroy', name='Growth Area', fillcolor='rgba(212, 175, 55, 0.3)'))
    fig_followers.update_layout(title="Follower Growth Trend", xaxis_title="Date", yaxis_title="Followers", template="plotly_dark")
    st.plotly_chart(fig_followers, use_container_width=True)
    
    # 2. Engagement Heatmap (by Date & Post Type)
    heatmap_data = df_filtered.pivot_table(index='Date', columns='Post Type', values='Engagement', aggfunc='sum').fillna(0)
    fig_heatmap = px.imshow(heatmap_data, title="Engagement Heatmap (Darker = Higher)", color_continuous_scale="YlOrRd")
    fig_heatmap.update_layout(template="plotly_dark")
    st.plotly_chart(fig_heatmap, use_container_width=True)
    
    # 3. Scatter: Views vs Engagement
    fig_scatter = px.scatter(df_filtered, x='Views', y='Engagement', color='Post Type', size='Likes', hover_data=['Date', 'Post Type'],
                             title="Views vs Engagement (Bubble Size = Likes)", template="plotly_dark")
    st.plotly_chart(fig_scatter, use_container_width=True)

with tab3:
    st.header("Top Performing Content")
    top_posts = df_filtered.sort_values('Views', ascending=False).head(10)
    st.dataframe(top_posts[['Date', 'Post Type', 'Views', 'Engagement', 'Likes', 'Comments', 'Shares']])
    
    # Interactive expander for details
    for i, row in top_posts.iterrows():
        with st.expander(f"{row['Post Type']} on {row['Date'].date()} – {row['Views']} Views"):
            st.write(f"Engagement: {row['Engagement']}")
            # If you have images: st.image("images/post_" + str(i) + ".jpg")
    
    st.download_button("Export Top Posts CSV", top_posts.to_csv(), file_name="top_posts.csv")

with tab4:
    st.header("Audience Breakdown")
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.subheader("Gender Distribution")
        gender_data = {'Gender': ['Men', 'Women'], 'Percentage': [61.1, 38.9]}  # Update with real if available
        fig_gender = px.pie(pd.DataFrame(gender_data), values='Percentage', names='Gender', hole=0.3, template="plotly_dark")
        st.plotly_chart(fig_gender)
    
    with col_b:
        st.subheader("Age Ranges")
        age_data = {'Age': ['18-24', '25-34', '35+'], 'Percentage': [74, 16, 10]}
        fig_age = px.bar(pd.DataFrame(age_data), x='Age', y='Percentage', template="plotly_dark", color_discrete_sequence=['#D4AF37'])
        st.plotly_chart(fig_age)
    
    st.subheader("Top Locations")
    location_data = df_filtered.groupby('City').size().reset_index(name='Count').sort_values('Count', ascending=False)
    fig_location = px.bar(location_data, x='City', y='Count', template="plotly_dark")
    st.plotly_chart(fig_location, use_container_width=True)

# ───────────────────────────────────────────────
# Footer
# ───────────────────────────────────────────────
st.markdown("---")
st.caption("VELÊRAYF Analytics Dashboard • Built with Streamlit • Data from Instagram Insights • Alfar, March 2026")
