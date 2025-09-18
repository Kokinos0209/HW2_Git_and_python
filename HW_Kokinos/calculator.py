def main(expression):
    parts = expression.split()
    operator = parts[1]
    num1, num2 = float(parts[0]), float(parts[2])
    result = 0
    if operator == '+':
        result = addition(num1, num2)
    elif operator == '-':
        result = difference(num1, num2)
    elif operator == '*':
        result = multiple(num1, num2)
    elif operator == '/':
        if num2==0:
            return 'На ноль делить нельзя!'
        result = deviation(num1, num2)
    return result

def difference(a, b):
    return (a - b)

def multiple(a, b):
    return (a * b)

def deviation (x, y): 
	  return (x/y)
      
def addition(a, b):
    return (a + b)
  
print(main(input("Введите выражение"))
      
      

