import pandas as pd

# Sample student data
std_data = [
    (1, 'sahil', 31, 'male', 'delhi'),
    (2, 'veer', 32, 'male', 'bihar'),
    (3, 'panda', 33, 'female', 'puri'),
    (4, 'suman', 34, 'female', 'mumbai')
]

# Create DataFrame
df = pd.DataFrame(std_data, columns=['std_id', 'name', 'age', 'gender', 'city'])

#_Display the DataFrame
#print(df.head(2))
#print(df.tail(2))
#print(df.shape)
#print(df.info())
#print(df.describe())
#print(df.columns)
#print(df[['age', 'gender']])
#print(df.values)
#print(df.index)
#print(df.dtypes)
#print(df.size)

#_OPERATIONS ON PANDAS DATA FRAME
#print(df['age'])
#print(df[['name', 'gender']])
#print(df.Loc[0])
#print(df[df['age'] > 34])

#_ adding a new column
df['phone_no'] = ['7654', '7890', '7639', '1234']

# delete a column
#df = df.drop(columns=['age'])

# rename operator
#df = df.rename(columns={'age': 'student_age'})

# deleting a row from dataframe
#df = df.drop(4)

# update a row in dataframe
#df.loc[3] = [3, 'pinki', 28, 'female', 'pauri' '7890]

# update the value
df.loc[2, 'gender'] = female
#display updated frame
print(df)