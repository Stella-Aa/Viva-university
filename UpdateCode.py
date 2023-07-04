#  Updated Code by HelixGen

from math import tan, pi
def Asking(info):
   return input(info)
def check(inputData, reUse):
      if inputData=="y":
         return reUse
      else:
          print("goodbye")

def CalculateArea():
 try:
  n_sides = int(input("Input number of sides: "))
  s_length = float(input("Input the length of a side: "))
  p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
 except ZeroDivisionError:
       Asking(f"you can not enter 0 wrong value please try again \n Would you wanna try it again? if yes type y")
       check(Asking,CalculateArea())
 except ValueError:
        Asking(f"you can not enter wrong type of value wrong value please try again \n Would you wanna try it again? if yes type y")
        check(Asking,CalculateArea())
 
 else:
     print(f"the area of the Polygon is {p_area}" )
        
CalculateArea()        