# hat.py

import copy
import random

class Hat:
    def __init__(self, **kwargs):  # fixed method name
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        balls_drawn = []
        if num_balls >= len(self.contents):
            balls_drawn = self.contents.copy()
            self.contents = []
        else:
            for _ in range(num_balls):
                ball_index = random.randint(0, len(self.contents)-1)
                balls_drawn.append(self.contents.pop(ball_index))
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_success = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        if all(balls_drawn.count(color) >= expected_balls[color] for color in expected_balls):
            num_success += 1
    return num_success / num_experiments
