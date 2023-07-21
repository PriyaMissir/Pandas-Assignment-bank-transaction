# Average Monthly Balance analysis using Pandas

This repository contains a Python script for analyzing bank transactions using the Pandas library. The script reads transaction data from a CSV file, performs various data manipulations, and calculates monthly average balances. 

# Steps

1.) Install Python in your system.
2.) Install Pandas.
3.) Read the CSV file. 
4.) Convert the Date format the 'transaction_date' column is converted to a Pandas DATETIME object with the format '%d-%m-%Y'.
5.) Sort the 'transaction_date' column in ascending order.
6.) Calculate the Cumulative sum of the balance to get the closing balance of each day and add it to a new column 'closing_balance' in the dataset.
7.) For calculating the monthly balance group the data by month and calculate the maximum closing balance for each month.
8.) Now calculate the number of transactions in each month to determine the number of days in each month.
9.) Final step calculate the 'Average monthly balance' by dividing the total balance by the number of days in each month.
10.) Display the result.
