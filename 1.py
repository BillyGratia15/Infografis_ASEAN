import mysql.connector
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Ganteng12345',
    database = 'world'
)

df = pd.read_sql('select Name, Population from country where Region = "Southeast Asia" order by Name asc', con = mydb)
print(df)

plt.style.use('seaborn')

x = df.Name
y = df.Population
warna = ['r', 'orange', 'y', 'g', 'b', 'k', 'purple', 'pink', 'r', 'y', 'b']
plt.title('Populasi Negara ASEAN',fontsize=15)

for titik in range(len(x)):
    plt.text(x[titik],y[titik],y[titik], ha='center', va='bottom')

plt.bar(x,y, color=warna)
plt.xlabel('Negara',fontsize=10)
plt.ylabel('Populasi (x100jt jiwa)',fontsize=10)

plt.xticks(rotation = 45, fontsize=7) 
plt.yticks(fontsize=7) 
plt.grid(True)
plt.show()