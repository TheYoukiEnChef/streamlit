import streamlit as st
import pandas as pd
import seaborn as sns
import plotly as plt
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px


# j'importe une image

st.image("https://www.albilegeant.com/articles/wp-content/uploads/2020/11/couleur-auto-low-624x365.jpg")


df= pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')


st.title('Production automobile')

st.write("Les données")

df.columns= ["conso", "vol_cylindre", "vol_moteur","chevaux","poids","acceleration","annee","continent"]
df['slice_conso']=pd.qcut(df['conso'], 5, labels=["very low", "low", "medium", "hight", "very hight"])
#df['slice_acceleration']=pd.cut(df['acceleration'], 5)


st.dataframe(df.head())



#ma matrice de corrélation
st.title("Matrice de corrélation")
col1, col2 = st.columns([2,1])

with col1:
   
    st.subheader("Matrice de corrélation")
    sns.set_style(style = 'darkgrid')

    corr = df.corr()
    mask = np.triu(np.ones_like(corr, dtype=np.bool))
    f, ax = plt.subplots(figsize=(11, 9))
    cmap = sns.diverging_palette(220, 10, as_cmap=True)

    viz_correlation= sns.heatmap(corr, mask=mask, cmap=cmap, annot = True, vmax=1, vmin=-1, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})
    
    st.pyplot(viz_correlation.figure)
   

with col2:
    st.subheader("description ")
    st.write("Les corrélations positives fortes- les variables évoluent étroitement de la même façon- sont en rouge (ex: volume moteur et volume cylindrée, volume moteur et poids etc.\nLes corrélations négatives sont en bleu- quand une valeur augmente l'autre diminue (ex: le volume du moteur et la consommation de carburant")



# poids / continent
st.subheader("poids des véhicules selon le continent")

fig4 = px.bar(df, x='continent', y='poids')
st.plotly_chart(fig4)

st.subheader("consommation des véhicules selon le continent")
fig5 = px.bar(df, x='continent', y='conso')
st.plotly_chart(fig5)


#graphiques en fonction du pays d'origine
pays = st.radio(
     "choisir le pays d'origine des véhicules",
     ('US', 'Japon', 'Europe'))
if pays == 'US':
    st.write('Evolution de la consommation et du poids des véhicules Américains')
    df_us = df[df['continent']== ' US.']
    fig6 = px.scatter(df_us, y='poids', x='annee',
            size='poids', color="slice_conso",
                log_x=True,size_max=40)
    st.plotly_chart(fig6)
    
elif pays=='Japon':
    st.write('Evolution de la consommation et du poids des véhicules Japonnais')
    df_jap = df[df['continent']== ' Japan.']
    fig7 = px.scatter(df_jap, y='poids', x='annee',
            size='poids', color="slice_conso",
                log_x=True,size_max=40)
    st.plotly_chart(fig7)
else:
    st.write('Evolution de la consommation et du poids des véhicules Européens')
    df_ue = df[df['continent']== ' Europe.']
    fig8 = px.scatter(df_ue, y='poids', x='annee',
            size='poids', color="slice_conso",
                log_x=True,size_max=40)
    st.plotly_chart(fig8)