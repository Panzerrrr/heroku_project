import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.title('Open Food Facto')

@st.cache
def load_data(nrows):
    data = pd.read_csv('data/data_cleaned.csv')
    return data

    # Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")

st.subheader('Raw data')
st.write(data)

hist_values = px.histogram(data, x="pnns_groups_2", color="saturated_fat_in_g").update_xaxes(categoryorder="category ascending")
st.plotly_chart(hist_values)

hist_values2 = px.histogram(data, x="pnns_groups_1", color="saturated_fat_in_g").update_xaxes(categoryorder="category ascending")
st.plotly_chart(hist_values2)

hist_values3 = px.histogram(data, x="fat_100g", color="saturated_fat_in_g").update_xaxes(categoryorder="category ascending")
st.plotly_chart(hist_values3)

hist_values4 = px.histogram(data, x="saturated-fat_100g", color="nutriscore_grade").update_xaxes(categoryorder="category ascending")
st.plotly_chart(hist_values4)

hist_values5 = px.histogram(data, x="nova_group", color="saturated_fat_in_g").update_xaxes(categoryorder="category ascending")
st.plotly_chart(hist_values5)

hist_values6 = px.histogram(data, x="ingredients_from_palm_oil_n", color="saturated_fat_in_g").update_xaxes(categoryorder="category ascending")
st.plotly_chart(hist_values6)