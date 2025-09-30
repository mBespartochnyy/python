import pandas as pd

data = pd.read_csv('./data/weather_data.csv')

# find avg temp
print(data.temp.mean())

# find max temp
data.temp.max()

# find row of data with max temp
print(data[data.temp == data.temp.max()])

# find rows of data where condition was sunny
print(data[data.condition == 'Sunny'])

# convert monday's temperature from C to F
monday_temp = data[data.day == 'Monday'].temp
monday_temp_in_f = (monday_temp * 9/5) + 32
print(monday_temp_in_f)

#  create a data fram from scratch
data_dict = {
	"students": ['Amy', 'James', 'Angela'],
	"scores": [76, 56, 65]
}
data_dict_converted = pd.DataFrame(data_dict)
print(data_dict_converted)

# save converted data dictionary into a csv file
data_dict_converted.to_csv('./data/student_scores.csv')
