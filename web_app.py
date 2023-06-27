import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Set page title
st.title("Simple Streamlit App")

# Add input fields
x_min = st.number_input("Enter the minimum value of x:", value=0.0)
x_max = st.number_input("Enter the maximum value of x:", value=10.0)
num_points = st.number_input("Enter the number of points:", value=100)
function_type = st.selectbox("Select a function:", ["Sin", "Cos", "Tan"])

# Generate data based on user input
x = np.linspace(x_min, x_max, num_points)
if function_type == "Sin":
    y = np.sin(x)
elif function_type == "Cos":
    y = np.cos(x)
else:
    y = np.tan(x)

# Plot the data
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(f'{function_type} function')
st.pyplot(fig)
