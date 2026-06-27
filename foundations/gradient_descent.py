class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        f_x = init
        for i in range(iterations):
            f_x_new = f_x - (learning_rate * (2 * f_x))
            f_x = f_x_new
        return round(f_x,5)
        pass
