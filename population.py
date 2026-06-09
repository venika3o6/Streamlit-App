import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(page_title="Population Analysis", layout="wide")
st.title("Population Analysis Dashboard")
file=st.file_uploader("opulation.txt", type=["txt"])
if file:
    df=pd.read_csv(file)
    st.subheader("Population Data Overview")
    st.dataframe(df.head())
    #Country filter
    country=st.selectbox("Select Country", df['Country'].unique())
    country_df=df[df['Country']==country]
    #Population trend line chart
    fig=px.line(country_df,x='Year',y='Population',title=f'Population Growth -{country}')
    st.plotly_chart(fig,use_container_width=True)
    #GDP trend
    fig2=px.line(country_df,x='Year',y='GDP',title=f'GDP Growth - {country}')
    st.plotly_chart(fig2,use_container_width=True)
    # latest population and GDP
    latest_year=df["Year"].max()
    latest_df=df[df['Year']==latest_year]
    fig3=px.bar(latest_df.sort_values(by='Population', ascending=False).head(10),x='Country',y='Population',title=f'Population in {latest_year}')
    st.plotly_chart(fig3,use_container_width=True)

