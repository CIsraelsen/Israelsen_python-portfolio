import pandas as pd
import plotly.express as px

# read in csv file
df = pd.read_csv("/Users/Colin/Library/Mobile Documents/com~apple~CloudDocs/Python Files/Data Science Programming/Project1/names_year.csv")

#%%
# filter "Luke"
colin_df = df.query('name == "Felisha"')

oliver_count_in_utah = df[df['name'] == 'Oliver']['UT'].sum()
oliver_count_in_utah

colin_df
#%%
# plot the filtered dataframe
px.line(colin_df, x='year', y='Total')
# %%
tempsF = [-40, 0, 32, 98.6, 212]

def f_to_c(degree):
    return (degree - 32) * 5/9

# version 1
tempsC = []
for f in tempsF:
    tempsC.append(f_to_c(f))
print(tempsC)

# version 2
tempsC = [f_to_c(f) for f in tempsF]
print(tempsC)

# version 3
tempsC = []
for f in tempsF:
    tempsC.append((lambda degree: (degree - 32) * 5/9)(f))
print(tempsC)

df = pd.DataFrame(tempsF)
print(df)