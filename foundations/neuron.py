import numpy as np
from numpy.typing import NDArray


class Solution:
    def forward(self, x: NDArray[np.float64], w: NDArray[np.float64], b: float, activation: str) -> float:
        # x: 1D input array
        # w: 1D weight array (same length as x)
        # b: scalar bias
        # activation: "sigmoid" or "relu"
        #
        # Pre-activation: z = dot(x, w) + b
        # Sigmoid: σ(z) = 1 / (1 + exp(-z))
        # ReLU: max(0, z)
        # return round(your_answer, 5)
        z = (w@x.T) + b
        if activation == "sigmoid":
            y = 1/(1 + np.exp(-z)).astype(float)
            return round(y,5)
        else:
            y = max(0,z)
            y =  float(y)
            return round(y,5)

        pass
