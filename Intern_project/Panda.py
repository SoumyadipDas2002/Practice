import pandas as pd

#Series 1D

# s= pd.Series([10,20,30,40,50], index=['a','b','c','d','e']) 
# print(s)

# print(s['c'])

# print(s.mean())
# print(s.sum())
# print(s + 55)


#DataFrames

# data={
#     'Name':["John","Harry","Peter"],
#     'Age':[19,20,30],
#     'Marks':[85,92,78]
# }


# df=pd.DataFrame(data)
# print(df)
# print(df.head()) First 5 rows default
# print(df.head(2)) First two rows
# print(df.tail(2)) Last two rows

# print(df.shape)

# print(df.columns)

# print(df['Name'])

# print(df.iloc[2]) Index number wise show data

# print(df.loc[0,'Marks']) it prints mark column 0 row it only prints one value



# db={
#     'Name':['Praloy','Sayan','Sahil'],
#     'Age':[18,19,25],
#     'Marks':[34,56,12]
# }

# dm=pd.DataFrame(db)
# print(dm)
# print(dm.iloc[2])

# Load csv
df=pd.read_csv('dataset.csv')
# print(df.head())
# print(df.info())

# Statistical column
# print(df.describe()) 

# Filter Data
# fil=df[df['Age']>30]
# print(fil)

# fil=df[(df['Age']>30)&(df['Salary']>90000)]
# print(fil)


# Add a new column
df['Status']="Old"
df.loc[df['Age']<30,'Status'] ='Young'
print(df)
df.to_csv("dataset.csv",index=False)

# sort data
# sort= df.sort_values(by='Salary',ascending=True)
# print(sort)