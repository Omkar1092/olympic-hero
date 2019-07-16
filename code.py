# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(index=str,columns= {'Total':'Total_Medals'},inplace = True)
print (data.head(10))


# --------------
#Code starts here

data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'],'Summer',(np.where(data['Total_Summer']<data['Total_Winter'],'Winter','Both')))

better_event = data['Better_Event'].value_counts().idxmax()
print (better_event)


# --------------
#Code starts here



top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
#print(type(top_countries))
top_countries.drop(top_countries.tail(1).index,inplace=True)

def top_ten(x):
    country_list=[]
    df = top_countries.nlargest(10,x)
    #print (df)
    country_list = list(df['Country_Name'])
    return country_list

top_10_summer = top_ten('Total_Summer')
top_10_winter = top_ten('Total_Winter')
top_10 = top_ten('Total_Medals')

#print (top_10)
#print(top_10_summer)
#print(top_10_winter)
common = list (set(top_10)&set(top_10_summer)&set(top_10_winter))
print(common)



# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
d1 = summer_df[['Total_Summer','Country_Name']]

pos=np.arange(len(summer_df['Country_Name']))
d1.plot(kind='bar')
plt.xticks(pos,d1['Country_Name'])
plt.title('Summer Medals')
plt.show()

d2 = winter_df[['Country_Name','Total_Winter']]
d2.plot(kind='bar')
plt.xticks(pos,d2['Country_Name'])
plt.title('Winter Medals')
plt.show()

d3=top_df[['Country_Name','Total_Medals']]
d3.plot(kind='bar')
plt.xticks(pos,d3['Country_Name'])
plt.title('Total Medals')
plt.show()

#fig,(ax_1,ax_2,ax_2) = plt.subplots(nrows=3,ncols=1,figsize=(20,10))
#ax_1.plot(kind='bar')


# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_df[['Country_Name','Golden_Ratio']]

index=summer_df['Golden_Ratio'].idxmax()
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df.loc[index,'Country_Name']

print ('Summer max golden ration is',summer_max_ratio)
print ('Country with summer max gold',summer_country_gold)

winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
#winter_df[['Country_Name','Golden_Ratio']]

index=winter_df['Golden_Ratio'].idxmax()
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df.loc[index,'Country_Name']

print ('Winter max golden ration is',winter_max_ratio)
print ('Country with winter max gold',winter_country_gold)

top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
#top_df[['Country_Name','Golden_Ratio']]

index=top_df['Golden_Ratio'].idxmax()
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df.loc[index,'Country_Name']

print ('Top max golden ration is',top_max_ratio)
print ('Country with top max gold',top_country_gold)



# --------------
#Code starts here
data_1=data[:-1]

data_1['Total_Points']=(data['Gold_Total']*3+data['Silver_Total']*2+data['Bronze_Total'])
index = data_1['Total_Points'].idxmax()
most_points=data_1['Total_Points'].max()
best_country=data_1.loc[index,'Country_Name']

print('Best country is',best_country)
print('most points are',most_points)


# --------------
#Code starts here
best= data.loc[data['Country_Name']==best_country,:]

best=best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar(stacked=True)
plt.xlabel('United_states')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


