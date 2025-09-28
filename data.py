import pandas as pd
data=pd.Series([10,20,30,40],index=['A','B','C','D'])
df=pd.DataFrame({
    'Name':['Alice','Bob','Charlie','Kelvin'],
    'Age':[21,22,23,34],
    'Score':[33,45,55,67]
})
df.set_index('Name', inplace=True)

print(df.head)