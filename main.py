# main.py

from hat import Hat, experiment

# Create a hat with ball counts
hat = Hat(red=5, blue=3, green=2)

# Set your expected result
expected_balls = {"red": 2, "green": 1}

# Run the experiment
probability = experiment(hat, expected_balls, num_balls_drawn=5, num_experiments=2000)

print("Estimated Probability:", probability)
