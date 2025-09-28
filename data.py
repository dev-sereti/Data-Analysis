#Creating Series and Data Frames
import pandas as pd
data=pd.Series([10,20,30,40],index=['A','B','C','D'])
df=pd.DataFrame({
    'Name':['Alice','Bob','Charlie','Kelvin'],
    'Age':[21,22,23,34],
    'Score':[33,45,55,67]
})
df.set_index('Name', inplace=True)

# Reading files
dfcsv=pd.read_csv("Data Cleaning.csv")
#print(dfcsv.head)


dfexcel=pd.read_excel("Data Cleaning Start.xlsx", sheet_name="Data")
#print(dfexcel.shape)
#print(dfexcel.info)
#print(dfexcel.head)
#print(dfexcel.tail)
#print(df.describe)
print(df.columns)


