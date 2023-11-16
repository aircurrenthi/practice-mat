import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from tkinter import *


df = pd.read_csv('df/Yunlin.csv',encoding='UTF-8')
row = df['補助事項或用途'] == '111年銀髮健身俱樂部補助計畫'
columns = ['補助事項或用途' ,'補助對象' ,'補助經費總計']
result = df.loc[row,columns]
result.set_index('補助對象',inplace=True)

chart = result.plot(figsize=(15, 10))

font = FontProperties(fname=r"NotoSansTC-VariableFont_wght.ttf")

for label in chart.get_xticklabels():
    label.set_fontproperties(font)

plt.title('111年銀髮健身俱樂部補助計畫',fontproperties = font)
plt.xlabel("對象",fontproperties = font)
plt.ylabel("補助經費總計",fontproperties = font)
plt.legend(prop = font)
plt.show()
