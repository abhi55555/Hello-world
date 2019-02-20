'''cars = ['BMW','Porshe','Audi']
for c in cars:
    print(c)
print(len(cars))
print(cars[1])

cars.append('Toyota')
print(cars)
cars.pop(1)
print(cars)
cars.remove('BMW')
print(cars)
cars.reverse()
print(cars)


class newclass:
    te = 'teachers'
q1 = newclass()
print(q1.te)
'''
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print('Hello my name is ' + self.name)

p1 = person("Ram",34)
p1.myfunc()
#print(p1.name)
#print(p1.age)
p1.age = 100
del p1
print(p1.age)
print('-----------')

import numpy as np

a = np.array([12, 23], [45, 56])
print(a)


