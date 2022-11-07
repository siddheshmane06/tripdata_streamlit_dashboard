import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("member.csv")

st.set_page_config(page_title="member",page_icon='cycling.png' , layout= 'wide')
st.title("Membership Users")
st.markdown("---")

total_users = len(df['rideable_type'])
users = df['rideable_type'].value_counts()
average_time = round(df['trip_duration_min'].mean(),2)

left_column , left_middle_column, right_middle_column, right_column = st.columns(4)

with left_column:
    st.subheader("Membership Users:")
    st.subheader(f'{total_users}')

with left_middle_column:
    st.subheader('Classic Bike Users:')
    st.subheader(f'{users[0]:}')

with right_middle_column:
    st.subheader('Electric Bike Users:')
    st.subheader(f'{users[1]:}') 

with right_column:
    st.subheader('Average Time:')
    st.subheader(f'{average_time} minutes')
    
st.markdown('---')

if st.checkbox("Show Dataset"):
    number=st.number_input("Number of rows to view",5,15)
    st.dataframe(df.head(number))
    st.success("Data Loaded Successfully")
else:
    data=None

left_column, right_column = st.columns(2)
with left_column:
    st.subheader("Start Position")
    fig=px.scatter_mapbox(df,
                      lon=df["start_lng"],
                      lat=df["start_lat"],
                      zoom=10,
                      color=df["member_casual"],
                      width=500,
                      height=700)
    fig.update_layout(mapbox_style="open-street-map")
    # fig.update_layout(margin={"r":0,"t":50,"l":0,"b":1})
    st.plotly_chart(fig)#, use_container_width=True)
with right_column:
    st.subheader("End Position")
    fig=px.scatter_mapbox(df,
                      lon=df["end_lng"],
                      lat=df["end_lat"],
                      zoom=10,
                      color=df["member_casual"],
                      width=500,
                      height=700)
    fig.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig)
st.markdown("")

left_column, right_column = st.columns(2)
with left_column:
    fig = px.pie(df,names="rideable_type")
    st.plotly_chart(fig)
with right_column:
    fig=px.sunburst(data_frame=df,path=["member_casual","rideable_type","day"],color=df["rideable_type"])
    st.plotly_chart(fig)
