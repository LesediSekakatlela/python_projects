import pandas as pd
from pandas import ExcelFile

df = pd.read_excel('Book11.xlsx', sheetname='Sheet1')
 
X = list(df['X'])
Y = list(df['Y'])
