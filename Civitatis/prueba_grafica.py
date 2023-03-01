
#%%
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Actividades_reales.csv')

# x = [1,2,3]
# y=[4,6,12]
# print(plt.plot(x,y))
#%%
import seaborn as sns
df.columns
# df['date'][0]
# sns.lineplot(x='date', y='value', data=df)