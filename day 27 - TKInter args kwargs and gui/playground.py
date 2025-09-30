def add(*nums_arr):
	result = 0
	for n in nums_arr:
		result += n
	print(result)

add(1,3,5,7, -6)

class Car:
	def __init__(self, **kw):
		self.make = kw.get('make')
		self.model = kw.get('model')

my_car = Car(make='Nissan')
print(my_car.model)
# output: None

print(my_car.make)
# output: Nissan