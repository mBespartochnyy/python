import pandas as pd

squirrel_data = pd.read_csv('./data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250925.csv')

print(squirrel_data.groupby(['Primary Fur Color']).size())