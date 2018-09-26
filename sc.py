# sprogram for simple calculator

i=int(input("enter the value of i:"))
j=int(input("enter the value of j:"))
o=input("what do you want to do?,+,-,/,*: ")

def add():
    return i+j
 def sub(a,b):
    return a-b
  def mult(a,b):     
    return a*b
  def div(a,b):
    return a/b
  if (o=='+'):
  	    print("addition=", add())
  elif (o=='-'):
   		print("subtraction=", sub(50,90))
   elif (o=='*'):
        print("multipication=", mult())
   elif (o=='/'): 
         print("divison=", div())     
            	
