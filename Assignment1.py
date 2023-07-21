import pandas as pd


df = pd.read_csv('bank_txns.csv')

print(df)

print(df.describe())


#Converting the transaction_date column to a pandas datetime object with a format
df['transaction_date'] = pd.to_datetime(df['transaction_date'],format='%d-%m-%Y')


#Sorting the transaction_date column in ascending order
df = df.sort_values(['transaction_date'],ascending=True)

print(df)

#Calculating cumulative sum of balance column to get closing balance of each day
df['closing_balance'] = df.groupby('transaction_date')['balance'].cumsum()

print(df.head(5))


#Grouping transaction by month and calculating total balance for each month
monthly_balance = df.groupby(df['transaction_date'].dt.to_period('M'))['closing_balance'].max()

print(monthly_balance)

#Calculating the number of days in each month
days_in_month = df.groupby(df['transaction_date'].dt.to_period('M')).size()

print(days_in_month)

#Calculating the monthly average balance by dividing total balance by the number of days in each month
average_monthly_balance = monthly_balance/days_in_month


print(average_monthly_balance)





