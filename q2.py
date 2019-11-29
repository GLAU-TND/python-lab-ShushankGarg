try:
    print(2+'33')
except TypeError as e:
    print('Error Handled',e)
try:
    h = "garg1"
    h=float(h)
except ValueError as e:
    print("Error handled ",e)
class Attributes():
    pass
try:
    print (object.attribute)
except AttributeError as e:
    print ('erroe handled',e)
    
