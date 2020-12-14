import pandas as pd
import xlrd
from sklearn.cluster import KMeans

from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt

main_frame = pd.read_excel('dataframe_data.xlsx')

#plt.scatter(main_frame.Age,main_frame.Interest)
#plt.xlabel('Age')
#plt.ylabel('Gender')
#plt.show()

km = KMeans(n_clusters=2)
predict = km.fit_predict(main_frame[['Age','Interest']])

main_frame["cluster"] = predict

"""
df1 = main_frame[main_frame.cluster == 0]
df2 = main_frame[main_frame.cluster == 1]
plt.scatter(df1.Age,df1.Interest,color = 'green')
plt.scatter(df2.Age,df2.Interest,color = 'red')
print(km.cluster_centers_)
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')   #Centoids of clusterz
plt.xlabel('Age')
plt.ylabel('Interest')
#plt.show()"""

#scaler = MinMaxScaler()

#scaler.fit(main_frame[['Interest']])
#main_frame['Interest'] = scaler.transform(main_frame[['Interest']])

#scaler.fit(main_frame[['Age']])
#main_frame['Age'] = scaler.transform(main_frame[['Age']])
#df1 = main_frame[main_frame.cluster == 0]
#df2 = main_frame[main_frame.cluster == 1]
#plt.scatter(df1.Age,df1.Interest,color = 'green')
#plt.scatter(df2.Age,df2.Interest,color = 'red')
#print(km.cluster_centers_)
#plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')   #Centoids of clusterz
#plt.xlabel('Age')
#plt.ylabel('Interest')
#plt.show()

#Elbow Plot
sse = []
k_rng = range(1,10)
for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(main_frame[['Age','Interest']])
    sse.append(km.inertia_)

plt.xlabel('K')
plt.ylabel('Euclidean distance')
plt.plot(k_rng,sse)
plt.show()