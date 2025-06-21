# ui/app.py

import streamlit as st
from hat import Hat, experiment

st.set_page_config(page_title="🎩 Hat Probability Simulator")

st.title("🎩 Hat Probability Simulator")
st.markdown("Estimate the probability of drawing certain balls from a hat.")

# Input hat contents
st.sidebar.header("Hat Contents")
red = st.sidebar.number_input("🔴 Red Balls", min_value=0, value=5)
blue = st.sidebar.number_input("🔵 Blue Balls", min_value=0, value=3)
green = st.sidebar.number_input("🟢 Green Balls", min_value=0, value=2)

# Input draw and experiment settings
draw_count = st.sidebar.number_input("🎯 Balls to Draw", min_value=1, value=5)
experiments = st.sidebar.number_input("🔁 Number of Experiments", min_value=100, value=2000)

# Input expected results
st.sidebar.header("Expected Draw Outcome")
expected_red = st.sidebar.number_input("Expected Red Balls", min_value=0, value=2)
expected_blue = st.sidebar.number_input("Expected Blue Balls", min_value=0, value=1)
expected_green = st.sidebar.number_input("Expected Green Balls", min_value=0, value=1)

if st.button("Run Simulation"):
    hat = Hat(red=red, blue=blue, green=green)
    expected_balls = {
        "red": expected_red,
        "blue": expected_blue,
        "green": expected_green
    }

    probability = experiment(hat, expected_balls, draw_count, experiments)
    st.success(f"🎯 Estimated Probability: `{probability:.4f}`")
