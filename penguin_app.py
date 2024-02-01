import streamlit as st 
import pandas as pd 
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt


st.title('Penguin Party')
penguins = 'penguins.csv'


@st.cache_data
def load_data(nrows):
    data = pd.read_csv(penguins, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")
st.write(data)

# create scatterplot
fig = plt.scatter(penguins, 
           x = 'flipper_length_mm', y = 'body_mass_g', 
           color = 'sex', 
           color_discrete_map={'FEMALE':'rgb(251,117,4)', 'MALE':'rgb(167,98,188)', 'Gentoo':'rgb(4,115,116)'},
           symbol='sex',
           symbol_map = {'FEMALE':'circle', 'MALE':'triangle-up'},
           height= 760
           )
fig.update_traces(marker=dict(size=9))
fig.update_layout(title='flipper length (mm) vs body mass (g)',
                  titlefont = dict( color='black', family='Open Sans',),) 
                  
fig.show()
