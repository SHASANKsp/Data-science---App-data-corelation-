#PART 3

import pandas as pd #importing pandas
import numpy as np #importing numpy


file1 = pd.read_csv("browser_rankings_data.csv",skiprows=1) #reading the csv file
#file1.head()
nfile = file1[["App ID","Keyword","Rank","Short Description","Long Description"]] #creating a subset
#nfile.head()

nfile['App ID'] = file1['App ID'].astype('category').cat.codes #converting the datatype to categorical
print("Correlation b/w Rank and App ID")
print(nfile['App ID'].corr(nfile['Rank'])) #printing correlation b/w variable

nfile['Keyword'] = file1['Keyword'].astype('category').cat.codes
print("Correlation b/w Rank and Keyword")
print(nfile['Keyword'].corr(nfile['Rank']))

nfile['Short Description'] = file1['Short Description'].astype('category').cat.codes
print("Correlation b/w Rank and Short description")
print(nfile['Short Description'].corr(nfile['Rank']))

nfile['Long Description'] = file1['Long Description'].astype('category').cat.codes
print("Correlation b/w Rank and Long description")
print(nfile['Long Description'].corr(nfile['Rank']))

corr = nfile.corr() #making a correlation matrix b/w all the variables

fig = plt.figure() #ploting the correlation matrix

#setting up colour scheme
ax = fig.add_subplot(111)
cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)

ticks = np.arange(0,len(nfile.columns),1)
ax.set_xticks(ticks)

plt.xticks(rotation=90)
ax.set_yticks(ticks)

# setting up labels for the plot
ax.set_xticklabels(nfile.columns)
ax.set_yticklabels(nfile.columns)
#displaying the plot
plt.show()
