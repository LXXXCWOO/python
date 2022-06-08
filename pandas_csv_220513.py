import pandas as pd

# df = pd.read_csv('C:\\Users\cwlee2009\Desktop\no_header.csv',
#                  header=None, names=['number', 'name', 'major'])
df = pd.read_csv('C:/Users/cwlee2009/Desktop/no_header.csv',
                 encoding='EUC-KR', header=None, names=['number', 'name', 'major'])
print(df)
