import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("tripdata.csv")

st.set_page_config(page_title="Divvy Cycle Trip Data",page_icon='cycling.png' , layout= 'wide')
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.title('Divvy Cycle Trip')
st.markdown("---")

total_users = len(df['rideable_type'])
average_time = round(df['trip_duration_min'].mean(),2)
users=df['member_casual'].value_counts()

left_column , left_middle_column, right_middle_column, right_column = st.columns(4)

with left_column:
    st.subheader('Total Users:')
    st.subheader(f'{total_users:}')

with left_middle_column:
    st.subheader('Membership Users:')
    st.subheader(f'{users[0]}')

with right_middle_column:
    st.subheader('Casual Users:')
    st.subheader(f'{users[1]}')

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
st.markdown("---")

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
    fig = px.pie(df,names="member_casual")
    st.plotly_chart(fig)
with right_column:
    fig=px.sunburst(data_frame=df,path=["member_casual","rideable_type","day_of_week"],color=df["rideable_type"])
    st.plotly_chart(fig)

st.markdown("---")

option = st.selectbox(
    'Average trip duration',
    ('','Per Day', 'Per Month'))

st.write('You selected:', option)

if option == "Per Day":
    summary=df.groupby(['member_casual','day_of_week'])['trip_duration_min'].agg(['mean'])
    summary=summary.reset_index()
    fig=sns.catplot(data=summary, kind='bar', x='day_of_week', y='mean', hue='member_casual', height=4, aspect=1.5)
    plt.title('Average length of trip per day and per member type')
    st.pyplot(fig)

if option == "Per Month":
    summary2=df.groupby(['member_casual','month'])['trip_duration_min'].agg(['mean'])
    summary2=summary2.reset_index()
    fig=sns.catplot(data=summary2, x='month', y='mean', hue='member_casual', kind='bar', height=4)
    plt.title('Average trip duration by customer type and month')
    st.pyplot(fig)
st.markdown("")

option = st.selectbox(
    'Total Number of Trips',
    ('','Per Day of Week', 'Per Month'))

st.write('You selected:', option)

if option == "Per Day of Week":
    summary3=df.groupby(['member_casual','day_of_week'])['trip_duration_min'].agg(['count'])
    summary3=summary3.reset_index()
    fig=sns.catplot(data=summary3, x="day_of_week",y='count', hue="member_casual", kind="bar", height=7, aspect=1.2)
    plt.title("Total number of trips by day of week and member type")
    st.pyplot(fig)

if option == "Per Month":
    summary4=df.groupby(['member_casual','month'])['trip_duration_min'].agg(['count'])
    summary4=summary4.reset_index()
    fig=sns.catplot(data=summary4, x='month', y='count', hue='member_casual', kind='bar', height=7)
    plt.title("Total number of trips by month and member type")
    st.pyplot(fig)
