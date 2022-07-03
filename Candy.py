from operator import index
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv



CandyReader=pd.read_csv("2017 Candy Data Cleaned.csv")
DataSummary = pd.read_csv("Candy Data Summary.csv")
Satisfaction = pd.read_csv("Satisfaction Summary.csv")
Top5 = pd.read_csv("Top 5.csv")
Candiespcountry = pd.read_csv("Top5CandiesCountry.csv")

positive=Satisfaction.iloc[1: , 1:2]
negative=Satisfaction.iloc[1: , 2:3]
neutral=Satisfaction.iloc[1: , 3:4]
index=Satisfaction.iloc[1: , :1]
Satgraph=pd.DataFrame({'positive':positive,'negative':negative, 'neutral':neutral}, index=index)
color = {
  "positive":"Green",
  "negative":"Red",
  "neutral":"Orange",
}
Satgraph.plot(color=color, kind='bar', stacked=True)
print(Satgraph)

Top5Data=Top5.iloc[: , :4]
Top5Pos=Top5.iloc[: , 1:2]
Top5Neg=Top5.iloc[: , 2:3]
Top5Neu=Top5.iloc[: , 3:4]
Top5Index=Top5.iloc[: , :1]
Top5graph=pd.DataFrame({'positive':Top5Pos,'negative':Top5Neg, 'neutral':Top5Neu}, Top5Index=index)
print(Top5graph)

fiveeach = Candiespcountry.iloc[: , :4]
print(fiveeach)

x = []
y = []
  
with open('Top5CandiesCountry.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        x.append(row[1])
        y.append(int(row[2]))
  
plt.bar(x, y, color = 'g', width = 1, label = "Age")
plt.xlabel('Candy')
plt.ylabel('Votes')
ax.set_title('Top 5 Candies \n United States - Canada - Other')
plt.legend()
plt.show()

Agesrt=pd.read_csv("AgeSort.csv")
Agesrt35=Agesrt.iloc[:750 , :79]
Agesrt50=Agesrt.iloc[750:1902 , :79]
Agesrt100=Agesrt.iloc[1902:2461 , :79]
numpy_array1 = Agesrt35.to_numpy()
numpy_array2 = Agesrt35.to_numpy()
numpy_array3 = Agesrt35.to_numpy()
print(np.char.count(numpy_array1, '0-35'))
print(np.char.count(numpy_array2, '35-50'))
print(np.char.count(numpy_array3, '50-100'))


