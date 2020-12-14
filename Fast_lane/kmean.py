import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

df =  pd.read_excel('dataframe_data.xlsx')
df.info()

df.drop(["Name"], axis = 1, inplace=True)

genders = df.Gender.value_counts()
sns.set_style("darkgrid")
plt.figure(figsize=(10,4))
sns.barplot(x=genders.index, y=genders.values)
plt.show()

age18_25 = df.Age[(df.Age <= 25) & (df.Age >= 18)]
age26_35 = df.Age[(df.Age <= 35) & (df.Age >= 26)]
age36_45 = df.Age[(df.Age <= 45) & (df.Age >= 36)]
age46_55 = df.Age[(df.Age <= 55) & (df.Age >= 46)]
age55above = df.Age[df.Age >= 56]

x = ["18-25","26-35","36-45","46-55","55+"]
y = [len(age18_25.values),len(age26_35.values),len(age36_45.values),len(age46_55.values),len(age55above.values)]

plt.figure(figsize=(15,6))
sns.barplot(x=x, y=y, palette="rocket")
plt.title("Number of Customer and Ages")
plt.xlabel("Age")
plt.ylabel("Number of Customer")
plt.show()

ss1_20 = df["Interest"][(df["Interest"] >= 1) & (df["Interest"] <= 20)]
ss21_40 = df["Interest"][(df["Interest"] >= 21) & (df["Interest"] <= 40)]
ss41_60 = df["Interest"][(df["Interest"] >= 41) & (df["Interest"] <= 60)]
ss61_80 = df["Interest"][(df["Interest"] >= 61) & (df["Interest"] <= 80)]
ss81_100 = df["Interest"][(df["Interest"] >= 81) & (df["Interest"] <= 100)]

ssx = ["1-20", "21-40", "41-60", "61-80", "81-100"]
ssy = [len(ss1_20.values), len(ss21_40.values), len(ss41_60.values), len(ss61_80.values), len(ss81_100.values)]

plt.figure(figsize=(15,6))
sns.barplot(x=ssx, y=ssy, palette="nipy_spectral_r")
plt.title("Spending Scores")
plt.xlabel("Score")
plt.ylabel("Number of Customer Having the Score")
plt.show()

sns.set_style("white")
fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df.Age, df["Gender"], df["Interest"], c='blue', s=60)
ax.view_init(30, 185)
plt.xlabel("Age")
plt.ylabel("Gender")
ax.set_zlabel('Interest')
plt.show()

wcss = []
for k in range(1,11):
    kmeans = KMeans(n_clusters=k, init="k-means++")
    kmeans.fit(df.iloc[:,1:])
    wcss.append(kmeans.inertia_)
plt.figure(figsize=(12,6))
plt.grid()
plt.plot(range(1,11),wcss, linewidth=2, color="red", marker ="8")
plt.xlabel("K Value")
plt.xticks(np.arange(1,11,1))
plt.ylabel("WCSS")
plt.show()

km = KMeans(n_clusters=5)
clusters = km.fit_predict(df.iloc[:,1:])

df["label"] = clusters

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df.Age[df.label == 0], df["Gender"][df.label == 0], df["Interest"][df.label == 0], c='blue', s=60)
ax.scatter(df.Age[df.label == 1], df["Gender"][df.label == 1], df["Interest"][df.label == 1], c='red', s=60)
ax.scatter(df.Age[df.label == 2], df["Gender"][df.label == 2], df["Interest"][df.label == 2], c='green', s=60)
ax.scatter(df.Age[df.label == 3], df["Gender"][df.label == 3], df["Interest"][df.label == 3], c='orange', s=60)
ax.scatter(df.Age[df.label == 4], df["Gender"][df.label == 4], df["Interest"][df.label == 4], c='purple', s=60)
ax.view_init(30, 185)
plt.xlabel("Age")
plt.ylabel("Gender")
ax.set_zlabel('Interest')
plt.show()

