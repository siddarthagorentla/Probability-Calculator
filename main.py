# main.py

from hat import Hat, experiment

def main():
    print("🎩 Hat Probability Simulator (Command Line Mode)\n")

    # Get user input
    red = int(input("Enter number of red balls: "))
    blue = int(input("Enter number of blue balls: "))
    green = int(input("Enter number of green balls: "))
    draw_count = int(input("How many balls to draw? "))
    experiments = int(input("Number of experiments to simulate: "))

    # Expected balls
    expected_red = int(input("Expected red balls to draw: "))
    expected_blue = int(input("Expected blue balls to draw: "))
    expected_green = int(input("Expected green balls to draw: "))

    # Create hat and expected dict
    hat = Hat(red=red, blue=blue, green=green)
    expected_balls = {
        "red": expected_red,
        "blue": expected_blue,
        "green": expected_green
    }

    # Run experiment
    probability = experiment(hat, expected_balls, draw_count, experiments)
    print(f"\n🎯 Estimated Probability: {probability:.4f}")

if __name__ == "__main__":
    main()
