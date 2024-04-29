# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import matplotlib.pyplot as plt
# import seaborn as sns

# df=pd.read_csv("casual.csv")

# st.set_page_config(page_title="casual",page_icon='cycling.png' , layout= 'wide')
# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
# st.title("Casual Users")
# st.markdown("---")

# total_users = len(df['rideable_type'])
# users = df['rideable_type'].value_counts()
# average_time = round(df['trip_duration_min'].mean(),2)

# left_column , left_middle_column, right_middle_column, right_column = st.columns(4)

# with left_column:
#     st.subheader("Casual Users:")
#     st.subheader(f'{total_users}')

# with left_middle_column:
#     st.subheader('Classic Bike Users:')
#     st.subheader(f'{users[0]:}')

# with right_middle_column:
#     st.subheader('Electric Bike Users:')
#     st.subheader(f'{users[1]:}') 

# with right_column:
#     st.subheader('Docked Bike Users:')
#     st.subheader(f'{users[2]:}') 
    
# st.markdown('---')

# df=pd.read_csv("casual.csv")
# if st.checkbox("Show Dataset"):
#     number=st.number_input("Number of rows to view",0,15)
#     st.dataframe(df.head(number))
#     st.success("Data Loaded Successfully")
# else:
#     data=None

# left_column, right_column = st.columns(2)
# with left_column:
#     st.subheader("Start Position")
#     fig=px.scatter_mapbox(df,
#                       lon=df["start_lng"],
#                       lat=df["start_lat"],
#                       zoom=10,
#                       color=df["member_casual"],
#                       width=500,
#                       height=700)
#     fig.update_layout(mapbox_style="open-street-map")
#     # fig.update_layout(margin={"r":0,"t":50,"l":0,"b":1})
#     st.plotly_chart(fig)#, use_container_width=True)
# with right_column:
#     st.subheader("End Position")
#     fig=px.scatter_mapbox(df,
#                       lon=df["end_lng"],
#                       lat=df["end_lat"],
#                       zoom=10,
#                       color=df["member_casual"],
#                       width=500,
#                       height=700)
#     fig.update_layout(mapbox_style="open-street-map")
#     st.plotly_chart(fig)
# st.markdown("")

# left_column, right_column = st.columns(2)
# with left_column:
#     fig = px.pie(df,names="rideable_type")
#     st.plotly_chart(fig)
# with right_column:
#     fig=px.sunburst(data_frame=df,path=["member_casual","rideable_type","day"],color=df["rideable_type"])
#     st.plotly_chart(fig)
# st.markdown("")

import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("casual.csv")

# Title and page configuration
st.set_page_config(page_title="Casual Users", page_icon='cycling.png', layout='wide')
st.title("Casual Users")

# Interactive filters
filter_options = st.sidebar.selectbox("Filter by:", ["Rideable Type", "Trip Duration"])
if filter_options == "Rideable Type":
    rideable_types = df['rideable_type'].unique()
    selected_type = st.sidebar.selectbox("Select Rideable Type:", rideable_types)
    filtered_df = df[df['rideable_type'] == selected_type]
else:
    min_duration = st.sidebar.slider("Minimum Trip Duration (minutes):", min_value=0, max_value=df['trip_duration_min'].max(), value=0)
    filtered_df = df[df['trip_duration_min'] >= min_duration]

# Display filtered data
st.subheader("Filtered Data:")
st.write(filtered_df)

# Interactive charts
st.subheader("Interactive Charts:")
with st.expander("Start Position"):
    fig_start = px.scatter_mapbox(filtered_df, lon=filtered_df["start_lng"], lat=filtered_df["start_lat"],
                                   zoom=10, color=filtered_df["member_casual"], width=700, height=500)
    fig_start.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig_start)

with st.expander("End Position"):
    fig_end = px.scatter_mapbox(filtered_df, lon=filtered_df["end_lng"], lat=filtered_df["end_lat"],
                                 zoom=10, color=filtered_df["member_casual"], width=700, height=500)
    fig_end.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig_end)

with st.expander("Rideable Type Distribution"):
    fig_pie = px.pie(filtered_df, names="rideable_type")
    st.plotly_chart(fig_pie)

with st.expander("Sunburst Chart"):
    fig_sunburst = px.sunburst(data_frame=filtered_df, path=["member_casual", "rideable_type", "day"],
                               color=filtered_df["rideable_type"])
    st.plotly_chart(fig_sunburst)
