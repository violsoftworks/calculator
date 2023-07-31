import tkinter as tk
import math
import re

#-----------------------------------CALCULATE FUNCTIONS-------------------------------------------

calculation = ""

symbols = "/*-+%"
count = 0

def add_to_calculation(symbol):
    global calculation, count
    try:
        # Check if the input symbol is valid
        if isinstance(symbol, (int, float, complex, str)):
            # Check if there are at least two characters in the calculation string
            if len(calculation) >= 2:
                last_two_chars = calculation[-2:]
                if last_two_chars in symbols:
                    count += 1
                else:
                    count = 0

                if count > 1:
                    # Remove the second character to prevent consecutive symbols
                    calculation = calculation[:-1]

            calculation += str(symbol)
            text_result.delete(1.0, "end")
            text_result.insert(1.0, calculation)
        else:
            raise ValueError("Invalid input")
    except Exception as e:
        clear_field()
        text_result.insert(1.0, "Error: " + str(e))



def evaluate_calculation():
    global calculation
    try:
        calculation = calculation.replace('^', '**')

        # Handle factorial operations
        while '!' in calculation:
            factorial_index = calculation.index('!')
            start_index = factorial_index - 1
            while start_index >= 0 and (calculation[start_index].isdigit() or calculation[start_index] == '.'):
                start_index -= 1
            start_index += 1  # Adjust for the last digit of the number

            # Handle the case when the factorial is in parentheses
            if calculation[start_index] == '(':
                count_open_parentheses = 1
                count_close_parentheses = 0
                end_index = start_index + 1
                while count_open_parentheses != count_close_parentheses:
                    if calculation[end_index] == '(':
                        count_open_parentheses += 1
                    elif calculation[end_index] == ')':
                        count_close_parentheses += 1
                    end_index += 1

                expression_inside_parentheses = calculation[start_index + 1:end_index - 1]
                number = evaluate_expression(expression_inside_parentheses)
                factorial_result = math.factorial(int(number))
                calculation = calculation[:start_index] + str(factorial_result) + calculation[end_index:]

            else:
                number = calculation[start_index:factorial_index]
                factorial_result = math.factorial(int(number))
                calculation = calculation[:start_index] + str(factorial_result) + calculation[factorial_index+1:]

        # Evaluate the remaining expression
        calculation = str(evaluate_expression(calculation))

        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except Exception as e:
        clear_field()
        text_result.insert(1.0, "Error: " + str(e))

def evaluate_expression(expression):
    return eval(expression, {'sin': math.sin, 'cos': math.cos, 'tan': math.tan})

def calculate_square_root():
    global calculation
    try:
        result = math.sqrt(float(calculation))
        calculation = str(result)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

#----------------------------------CREATING INTERFACE-----------------------------------------------

root = tk.Tk()
root.geometry("1000x600")
root.configure(bg="#FFC1CC")

# Frame to simulate background color for text_result
frame_result = tk.Frame(root, bg="#FFC1CC", padx=5, pady=5)
frame_result.grid(row=0, column=0, columnspan=6)

text_result = tk.Text(frame_result, height=2, width=27, font=('Arial', 24), bg="#FFD1DC")
text_result.grid(columnspan=6)


#---------------------------------CREATING BUTTONS------------------------------------------------

btn_style = {
    'height': 2, 
    'width': 5, 
    'font': ('Arial', 24),
    'borderwidth': 0,
    'relief': tk.FLAT,
    'activebackground': "#FF9999",
    'activeforeground': "white"
}

operation_btn_style = {
    'height': 2, 
    'width': 5, 
    'font': ('Arial', 24),
    'borderwidth': 0,
    'relief': tk.FLAT,
    'activebackground': "#F88379",
    'activeforeground': "white"
}

# Number buttons
number_color = "#FC6C85"
btn_1 = tk.Button(root, text="1", fg="white", bg=number_color, command=lambda: add_to_calculation(1), **btn_style)
btn_1.grid(row=3, column=1)
btn_2 = tk.Button(root, text="2", fg="white", bg=number_color, command=lambda: add_to_calculation(2), **btn_style)
btn_2.grid(row=3, column=2)
btn_3 = tk.Button(root, text="3", fg="white", bg=number_color, command=lambda: add_to_calculation(3), **btn_style)
btn_3.grid(row=3, column=3)

btn_4 = tk.Button(root, text="4", fg="white", bg=number_color, command=lambda: add_to_calculation(4), **btn_style)
btn_4.grid(row=4, column=1)
btn_5 = tk.Button(root, text="5", fg="white", bg=number_color, command=lambda: add_to_calculation(5), **btn_style)
btn_5.grid(row=4, column=2)
btn_6 = tk.Button(root, text="6", fg="white", bg=number_color, command=lambda: add_to_calculation(6), **btn_style)
btn_6.grid(row=4, column=3)

btn_7 = tk.Button(root, text="7", fg="white", bg=number_color, command=lambda: add_to_calculation(7), **btn_style)
btn_7.grid(row=5, column=1)
btn_8 = tk.Button(root, text="8", fg="white", bg=number_color, command=lambda: add_to_calculation(8), **btn_style)
btn_8.grid(row=5, column=2)
btn_9 = tk.Button(root, text="9", fg="white", bg=number_color, command=lambda: add_to_calculation(9), **btn_style)
btn_9.grid(row=5, column=3)

# Number zero
btn_0 = tk.Button(root, text="0", fg="white", bg=number_color, command=lambda: add_to_calculation(0), **btn_style)
btn_0.grid(row=6, column=2)

# Operation buttons
operation_color = "#FC8EAC"
btn_plus = tk.Button(root, text="+", fg="white", bg=operation_color, command=lambda: add_to_calculation('+'), **operation_btn_style)
btn_plus.grid(row=6, column=4)
btn_minus = tk.Button(root, text="-", fg="white", bg=operation_color, command=lambda: add_to_calculation('-'), **operation_btn_style)
btn_minus.grid(row=5, column=4)
btn_multiplication = tk.Button(root, text="x", fg="white", bg=operation_color, command=lambda: add_to_calculation('*'), **operation_btn_style)
btn_multiplication.grid(row=4, column=4)
btn_division = tk.Button(root, text="÷", fg="white", bg=operation_color, command=lambda: add_to_calculation('/'), **operation_btn_style)
btn_division.grid(row=3, column=4)
btn_degree = tk.Button(root, text="^", fg="white", bg=operation_color, command=lambda: add_to_calculation('^'), **operation_btn_style)
btn_degree.grid(row=2, column=1)
# Additional buttons
btn_point = tk.Button(root, text=".", fg="white", bg="#FC8EAC", command=lambda: add_to_calculation('.'), **btn_style)
btn_point.grid(row=3, column=5)

btn_remainder = tk.Button(root, text="%", fg="white", bg="#FC8EAC", command=lambda: add_to_calculation('%'), **btn_style)
btn_remainder.grid(row=4, column=5)

btn_root = tk.Button(root, text="√", fg="white", bg="#FC8EAC", command=lambda: calculate_square_root(), **btn_style)
btn_root.grid(row=5, column=5)

btn_par_open = tk.Button(root, text="(", fg="white", bg="#FC8EAC", command=lambda: add_to_calculation('('), **btn_style)
btn_par_open.grid(row=6, column=1)

btn_par_close = tk.Button(root, text=")", fg="white", bg="#FC8EAC", command=lambda: add_to_calculation(')'), **btn_style)
btn_par_close.grid(row=6, column=3)

# Equal button
btn_equal = tk.Button(root, text="=", fg="white", bg="#E75480", command=evaluate_calculation, **btn_style)
btn_equal.grid(row=6, column=5)

# Additional buttons
#btn_arrow = tk.Button(root, text="⟽", fg="white", bg="#FC8EAC", **btn_style)
#btn_arrow.grid(row=2, column=1)

btn_e = tk.Button(root, text="e", fg="white", bg="#FC8EAC", command=lambda: add_to_calculation('2.71828'), **btn_style)
btn_e.grid(row=2, column=2)

btn_pi = tk.Button(root, text="𝛑", fg="white", bg="#FC8EAC", command=lambda: add_to_calculation('3.14159'), **btn_style)
btn_pi.grid(row=2, column=3)

# Clear button
btn_clear = tk.Button(root, text="C", fg="white", bg="#FC8EAC", command=clear_field, **btn_style)
btn_clear.grid(row=2, column=4, columnspan=2)

# btn_arrow = tk.Button(root, text="⟽", fg="white", bg="#FC8EAC", **btn_style)
# btn_arrow.grid(row=2, column=1)








#--------------------------------TRIGONOMETRIC FUNCTIONS_------------------------------------------
def convert_input_to_radians(input_str):
    # Function to handle trigonometric expressions with "pi"
    def replace_pi(match):
        return str(eval(match.group(0).replace('pi', 'math.pi')))

    # Replacing 'pi' with 'math.pi' and evaluating the input to handle expressions like pi/2
    input_str = re.sub(r'\bpi\b|pi[/*^+()]', replace_pi, input_str)

    # Converting degrees to radians
    radians_value = math.radians(eval(input_str))
    return radians_value

def sine():
    global calculation
    try:
        radians_value = convert_input_to_radians(calculation)
        result = math.sin(radians_value)
        calculation = str(result)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def cosine():
    global calculation
    try:
        radians_value = convert_input_to_radians(calculation)
        result = math.cos(radians_value)
        calculation = str(result)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def tangent():
    global calculation
    try:
        radians_value = convert_input_to_radians(calculation)
        result = math.tan(radians_value)
        calculation = str(result)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def cotangent():
    global calculation
    try:
        radians_value = convert_input_to_radians(calculation)
        result = 1 / math.tan(radians_value)
        calculation = str(result)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")


def hyperbolic_sine():
    global calculation
    try:
        result = math.sinh(float(calculation))
        calculation = str(result)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def hyperbolic_cosine():
    global calculation
    try:
        result = math.cosh(float(calculation))
        calculation = str(result)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def hyperbolic_tangent():
    global calculation
    try:
        result = math.tanh(float(calculation))
        calculation = str(result)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def hyperbolic_cotangent():
    global calculation
    try:
        result = 1 / math.tanh(float(calculation))
        calculation = str(result)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def hyperbolic_secant():
    global calculation
    try:
        result = 1 / math.cosh(float(calculation))
        calculation = str(result)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def hyperbolic_cosecant():
    global calculation
    try:
        result = 1 / math.sinh(float(calculation))
        calculation = str(result)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")



btn_sin = tk.Button(root, text="sin", fg="white", bg=operation_color, command=sine, **operation_btn_style)
btn_sin.grid(row=2, column=6)

btn_cos = tk.Button(root, text="cos", fg="white", bg=operation_color, command=cosine, **operation_btn_style)
btn_cos.grid(row=2, column=7)

btn_tan = tk.Button(root, text="tan", fg="white", bg=operation_color, command=tangent, **operation_btn_style)
btn_tan.grid(row=3, column=6)

btn_cot = tk.Button(root, text="cot", fg="white", bg=operation_color, command=cotangent, **operation_btn_style)
btn_cot.grid(row=3, column=7)

btn_sinh = tk.Button(root, text="sinh", fg="white", bg=operation_color, command=hyperbolic_sine, **operation_btn_style)
btn_sinh.grid(row=4, column=6)

btn_cosh = tk.Button(root, text="cosh", fg="white", bg=operation_color, command=hyperbolic_cosine, **operation_btn_style)
btn_cosh.grid(row=4, column=7)

btn_tanh = tk.Button(root, text="tanh", fg="white", bg=operation_color, command=hyperbolic_tangent, **operation_btn_style)
btn_tanh.grid(row=5, column=6)

btn_coth = tk.Button(root, text="coth", fg="white", bg=operation_color, command=hyperbolic_cotangent, **operation_btn_style)
btn_coth.grid(row=5, column=7)

btn_a = tk.Button(root, text="a=", fg="white", bg=operation_color,  **operation_btn_style)
btn_a.grid(row=4, column=8)

btn_b = tk.Button(root, text="b=", fg="white", bg=operation_color, **operation_btn_style)
btn_b.grid(row=5, column=8)

btn_factorial = tk.Button(root, text="!", fg="white", bg=operation_color, command=lambda:add_to_calculation('!'), **operation_btn_style)
btn_factorial.grid(row=3, column=8)


#-----------------------------------ADVANCED PART-----------------------------------------------

import tkinter as tk
import math
import re
import sympy as sp
from scipy import integrate

# ...

#--------------------------------TRIGONOMETRIC FUNCTIONS_------------------------------------------
# ... (Existing trigonometric functions)

def calculate_limit():
    global calculation
    try:
        # Replace 'x' with 'X' in the expression for limit calculation
        expression_with_x = calculation.replace('x', 'X')
        limit_value = sp.limit(expression_with_x, sp.Symbol('X'), sp.oo)
        calculation = str(limit_value)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def calculate_integral():
    global calculation
    try:
        # Replace 'x' with 'X' in the expression for integral calculation
        expression_with_x = calculation.replace('x', 'X')
        integral_value = integrate.quad(lambda X: sp.sympify(expression_with_x), -sp.oo, sp.oo)[0]
        calculation = str(integral_value)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def calculate_derivative():
    global calculation
    try:
        # Replace 'x' with 'X' in the expression for derivative calculation
        expression_with_x = calculation.replace('x', 'X')
        x = sp.Symbol('X')
        derivative_value = sp.diff(expression_with_x, x)
        calculation = str(derivative_value)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")



btn_limit = tk.Button(root, text="lim", fg="white", bg=operation_color, command=lambda: calculate_limit(), **operation_btn_style)
btn_limit.grid(row=6, column=6)

btn_integral = tk.Button(root, text="∫", fg="white", bg=operation_color, command=lambda: calculate_integral(), **operation_btn_style)
btn_integral.grid(row=6, column=7)

btn_derivative = tk.Button(root, text="d/dx", fg="white", bg=operation_color, command=lambda: calculate_derivative(), **operation_btn_style)
btn_derivative.grid(row=2, column=8)

btn_x = tk.Button(root, text="X", fg="white", bg=operation_color, command=lambda: add_to_calculation('x'), **operation_btn_style)
btn_x.grid(row=6, column=8)

root.mainloop()



















