from pyscript import display, document

# String
firstname = "Parminder Singh Bhullar"
display("name:",firstname)

#- Integer
Age = 15
display("age:", Age)

#- Float
Height1 = 182.22
display("Height:", Height1)

#- List
Countries_visited = ["Japan", "Russia", "Singapore"]
display("Countries Visited:", Countries_visited)

#- Boolean
New_student = False
display("New student?", New_student)

#- Dictionary
Dictionary1 = {"Red": "Toyota", "9.5": "Raphael"}
display("color, shoe size, and best friend",Dictionary1)


#- Set
favorite_fruits = {"Mango", "Apple", "Banana", "Grapes", "Orange"}
display("Favorite fruits:",favorite_fruits)


#- Tuple
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
display("Days of the week", days)

#- addition 
def adding_numbers(e):
    document.getElementById('result').innerHTML = " "  # clear the previous result

    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)

    # Adds the two numbers
    sum = first_number + second_number

    display(f'The sum of {first_number} and {second_number} is {sum}', target='result')

#- substraction
def subtracting_numbers(e):
    document.getElementById('result').innerHTML = " "  # clear the previous result

    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)

    # Subtracts the second number from the first number
    difference = first_number - second_number

    display(f'The difference of {first_number} and {second_number} is {difference}', target='result')

#- Multiplication
def multiplying_numbers(e):
    document.getElementById('result').innerHTML = " "  # clear the previous result

    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)

    # Multiplies the two numbers
    product = first_number * second_number

    display(f'The product of {first_number} and {second_number} is {product}', target='result')

#- Division
def dividing_numbers(e):
    document.getElementById('result').innerHTML = " "  # clear the previous result

    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)

    # Divides the first number by the second number
    quotient = first_number / second_number

    display(f'The quotient of {first_number} and {second_number} is {quotient}', target='result')


def floor_dividing_numbers(e):
    document.getElementById('result').innerHTML = " "  # clear the previous result

    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)

    # Performs floor division and returns the whole-number result
    result = first_number // second_number

    display(f'{first_number} // {second_number} = {result}', target='result')


def modulus_numbers(e):
    document.getElementById('result').innerHTML = " "  # clear the previous result

    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)

    # Finds the remainder after division
    result = first_number % second_number

    display(f'{first_number} % {second_number} = {result}', target='result')