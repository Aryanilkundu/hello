import numpy as np
import pandas as pd
#creating a dictionary
dict1={
       'name' :['h','r','s','sh'],
       'marks':[12,34,56,28],
       'city':['howrah','kolkata','delhi','mumbai']
       
       }
df=pd.DataFrame(dict1)
df
#exporting the dataframe into a csv file 
df.to_csv('friends.csv')
#creating a excel file without indexing 
df.to_csv('friends_index_false.csv',index=False)
#if u want some front or back rows
df.head()
df.tail()

#this command gives some statistical result of all numerical columns
df.describe()
#accesing to already created csv file
harry=pd.read_csv('train.csv')
print(harry)
print(harry['speed'])
#changing a entry
harry['speed'][0]=50
harry['speed'][0]
harry.to_csv('train.csv')
harry.index=('a','b','c','d')
print(harry)
harry.to_csv('train.csv')

##-------------------------------------------------------------------------
newdf=pd.DataFrame(np.random.rand(334,15),index=np.arange(334 )) 
#arange is a programe under numpy which acts just like range in normal...
newdf.head()
newdf.index
newdf.columns
newdf.to_numpy()   #converts into numpy array
newdf.T    ##takes the transpose
newdf.head()
newdf.sort_index(axis=0,ascending=False)
type(newdf[0])

#x is a view of our dataframe newdf, any changes made to newdf 
#after assigning the varibale name will also be reflected in x
x=newdf
newdf[0][0]=234
x
#but when use copy command then x1 will not be a view
x1=newdf.copy()
newdf[0][0]=2345
x1

#while changing a particular entry of dataframe use loc[] command instead of 
#newdf[0,0]=234
newdf.head(2)
newdf.loc[0][0]=345 
newdf.head(2)

#deleting a particular row of column,for row axis=0(default),for column,axis=1
newdf.drop(333)
newdf= newdf.drop(14,axis=1)
newdf

#obtaining a particular set of rows or columns
newdf.loc[[0,1],[12,13]]
newdf.loc[[0,1],:]
newdf.loc[:,[0,1]]

#giving some conditions by loc
newdf.loc[(newdf[0]<0.4) & (newdf[5]>0.1)]

#till now whenever we use newdf.(some command) the actual 'newdf' don't 
#change untill we use newdf=newdf.(some command)...soin case u use 
#newdf.(some commnad)(...,..,inplace=True )






















