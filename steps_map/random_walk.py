from random import choice


class RandomWalk:
    """a class create random walking"""

    def __init__(self, footsteps):
        self.footsteps = footsteps
        self.x_values = [0]
        self.y_values = [0]

    def walk_random(self):
        x_next = y_next = 0
        while len(self.x_values) < self.footsteps:
            x_direction = choice([1, 0, -1])
            y_direction = choice([1, 0, -1])

            x_gap = choice([0, 1, 2, 3])
            y_gap = choice([0, 1, 2, 3])

            x_next = x_next + (x_direction * x_gap)
            y_next = y_next + (y_direction * y_gap)

            self.x_values.append(x_next)
            self.y_values.append(y_next)
