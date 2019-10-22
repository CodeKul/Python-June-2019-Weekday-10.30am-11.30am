# 1) Series
# 2) DataFrame
# 3) Panel

import pandas as pd

ser1 = pd.Series(['Red', 'Green', 'Blue', 'Yellow', 'Magenta', 'Cyan', 'Black', 'White', 'Gray'])

ser2 = pd.Series([1,2,3,4,5,6,7,8,9])
# print(ser2.Two)


df = pd.DataFrame([ser1, ser2])

dict1 = {'Python': [20, 40, 25, 63, 54, 34, 34, 67, 89, 23, 45, 78], 'Java': [45, 42, 64, 72, 57, 35, 78, 34, 78, 56, 45, 73],'C': [34, 54, 23, 67, 23, 34, 56, 53, 36, 89, 45, 34], 'C++': [53, 64, 74, 34, 86, 36, 45, 34, 65, 73, 67, 45], 'Data structures': [45, 45, 56, 56, None, 45, 56, 23, 78, 78, 67, 23], 'Android': [45, 54, 87, 23, 97, 56, 34, 68, 46, 23, 67, 67], 'iOS': [54, 56, 47, 84, 46, 56, 67, 34, 56, 34, 56, 67]}

df = pd.DataFrame(dict1, index=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'])
# print(df)

# print(df.head(3))
# print(df.tail(10))

# print(df.shape)

# df.info(null_counts=True)

# print(df.mean())

# print(df.max())
# print(df.min())

# print(df.std())

# print(df.median())
# print(df.count())

# print(df.describe())

df.rename(columns={'Data structures':'Data_structures'}, inplace=True)
df.Data_structures = df.Data_structures.fillna(int(df.Data_structures.mean()))

df.drop(columns=['C++'], inplace=True)

# df = df[['Python', 'Java', 'C']].corr()

df.Data_structures = df.Data_structures.astype(int) 

print(df)

df = pd.read_csv('mycsv.csv')

print(df)

df.info()

print(df.describe())


df = pd.read_csv('dataset1.csv')
print(df)

df.drop(columns=['Index'], inplace=True)
print(df)

df.info()

df.Cost = df.Cost.fillna(df.Total - df.Tax)

print(df)

df.rename(columns={'Tax':'GST'}, inplace=True)

print(df)

# df.Cost = df.Cost.astype(str)

print(df[['Cost', 'GST', 'Total']].corr())

print(df.iloc[3:7,1:4])

print(df.loc[:, 'Item':'GST'])

# df.GST = df.GST + 100
# print(df.loc[:, 'Item':'GST'])

f = lambda x: x * 2
df.Cost = df.Cost.apply(f)
print(df)


sorted_df = df.sort_values(by='Cost', ascending=True)
print(sorted_df)

filter1 = df['Cost'] > 15
filtered_df = df[filter1]

filter2 = (df.Cost > 10) & (df.Cost < 15)
filtered_df = df[filter2]
print(filtered_df)