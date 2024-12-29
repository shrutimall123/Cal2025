import streamlit as st

# Set the title of the app
st.title('Simple Calculator')

# Input fields for two numbers
num1 = st.number_input("Enter the first number", step=0.1)
num2 = st.number_input("Enter the second number", step=0.1)

# Dropdown menu to select operation
operation = st.selectbox("Choose operation", ['Add', 'Subtract', 'Multiply', 'Divide'])

# Function to perform the calculation
def calculate(num1, num2, operation):
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero is not allowed."

# Button to calculate and display the result
if st.button('Calculate'):
    result = calculate(num1, num2, operation)
    st.write(f"Result: {result}")
