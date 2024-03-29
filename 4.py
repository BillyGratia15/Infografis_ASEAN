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

df = pd.read_sql('select Name, SurfaceArea from country where Region = "Southeast Asia" order by Name asc', con = mydb)
print(df)

x = df.Name
y = df.SurfaceArea

warna = ['r', 'orange', 'y', 'g', 'b', 'k', 'purple', 'pink', 'r', 'y', 'b']
plt.title('Persentase Luas Daratan ASEAN',fontsize=15)

plt.pie(y,labels=x, colors=warna, autopct='%.1f%%')
plt.savefig('4.png')
plt.show()