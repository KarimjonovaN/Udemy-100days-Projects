# class Calculator:

#   def add(self, num_1, num_2):
#     return num_1 + num_2
  

#   def subtract(self, num_1, num_2):
#     return num_1 - num_2
    
    
# calculate = Calculator()

# add_result = calculate.add(11, 22)
# print(add_result)

# sub_result = calculate.subtract(22, 11)
# print(sub_result)

import math

class Circle(): 
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return math.pi *self.radius ** 2

    
  
  def perimetr(self):
   return math.pi *self.radius * 2


circle = Circle(5)
print(f"{circle.area()},\n{circle.perimetr()}")



    