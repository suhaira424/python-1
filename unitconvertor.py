import streamlit as st  # Import Streamlit for UI
from pint import UnitRegistry  # Import Pint for unit conversions

# Initialize the unit registry
ureg = UnitRegistry()

# Streamlit App Title
st.title("🔢 Google-Style Unit Converter")

# Define unit categories and their possible conversions
unit_categories = {
    "Length": ["meter", "kilometer", "mile", "yard", "foot", "inch"],
    "Weight": ["gram", "kilogram", "pound", "ounce"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Speed": ["meter/second", "kilometer/hour", "mile/hour"],
    "Time": ["second", "minute", "hour", "day"]
}

# Select a category
category = st.selectbox("Select a category", list(unit_categories.keys()))

# Select units for conversion
from_unit = st.selectbox("Convert from", unit_categories[category])
to_unit = st.selectbox("Convert to", unit_categories[category])

# User input for value to convert
value = st.number_input("Enter value", min_value=0.0, format="%.2f")

# Convert Button
if st.button("Convert"):
    try:
        # Convert the value using Pint
        result = (value * ureg(from_unit)).to(to_unit)
        st.success(f"{value} {from_unit} = {result.magnitude:.4f} {to_unit}")
    except Exception as e:
        st.error(f"Error: {e}")
