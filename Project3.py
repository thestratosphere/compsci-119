#Project 3 - Jacqueline Cole - November 29th, 2022
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

rawdf = pd.read_csv("All_Pokemon.csv")
df = px.data

#print(rawdf)
print(f"{rawdf.isnull().values.any()}, there are null values present in the data")
#Bring back a True, due to Type 2 being empty in many rows due to being monotypes. Monotypes are needed through the data so no cleaning up of null values is done
#Legendaries are a seperate category from non-legendaries, so the data is cleaned to only focus on the legendaries
legendary = rawdf[rawdf["Legendary"]==1]
#print(legendary)

#Calculate some averages

avs = legendary['BST'].mean()
print(f"The average BST of all Legendary Pokemon is {round(avs)}")

#Average of specific types

#Normal - There are no Normal secondary typing legendary class Pokemon, thus trying to average produces NaN
legendaryNormal = legendary[legendary["Type 1"]=="Normal"]
#legendaryNormal2 = legendary[legendary["Type 2"]=="Normal"]
avsN = legendaryNormal['BST'].mean()
#avsN2 = legendaryNormal2['BST'].mean()
print(f"The average BST of all Normal type Legendary Pokemon is {round(avsN)}")

#Dragon
legendaryDragon = legendary[legendary["Type 1"]=="Dragon"]
legendaryDragon2 = legendary[legendary["Type 2"]=="Dragon"]
avsD = legendaryDragon['BST'].mean()
avsD2 = legendaryDragon2['BST'].mean()
avgDragonBST = ((avsD+avsD2)/2)
print(f"The average BST of all Dragon type Legendary Pokemon is {round(avgDragonBST)}")


#Fairy
legendaryFairy = legendary[legendary["Type 1"]=="Fairy"]
legendaryFairy2 = legendary[legendary["Type 2"]=="Fairy"]
avsF = legendaryFairy['BST'].mean()
avsF2 = legendaryFairy2['BST'].mean()
avgFairyBST = ((avsF+avsF2)/2)
print(f"The average BST of all Fairy type Legendary Pokemon is {round(avgFairyBST)}")

#Make some charts
#Bar graph of BST across entire Pokedex, aka why only Legendaries
figRaw = px.bar(rawdf, y=["BST"])
figRaw.update_layout(title="Comparison of all Base Stat Totals", xaxis_title="Pokemon Number", yaxis_title="Base Stat Total")
figRaw.show()

#Distribution of Legendary Base Stat Totals
figLegendary = px.histogram(legendary, x=["BST"], text_auto=True)
figLegendary.update_layout(title="Distribution of Legendary Base Stat Totals", xaxis_title="Base Stat Total", yaxis_title="Number of Pokemon", bargap=0.05)
figLegendary.show()


#Comparison of Dragon type Legendary Pokemon BST versus Normal type Legendary Pokemon BST

figDVN = go.Figure()
figDVN.add_trace(go.Bar(name='Dragon', x=['Dragon'], y=[avgDragonBST],))
figDVN.add_trace(go.Bar(name='Normal', x=['Normal'], y=[avsN],))
figDVN.update_layout(barmode='group', bargap=0.50, bargroupgap=0.0, title="Comparison of Dragon type Legendary Pokemon BST versus Normal type Legendary Pokemon BST")
figDVN.show()

#Comparison of Dragon type Legendary Pokemon BST versus Fairy type Legendary Pokemon BST

figDVF = go.Figure()
figDVF.add_trace(go.Bar(name='Dragon', x=['Dragon'], y=[avgDragonBST],))
figDVF.add_trace(go.Bar(name='Normal', x=['Fairy'], y=[avgFairyBST],))
figDVF.update_layout(barmode='group', bargap=0.50, bargroupgap=0.0, title="Comparison of Dragon type Legendary Pokemon BST versus Fairy type Legendary Pokemon BST")
figDVF.show()