import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        ans = z - z.max()
        expon = np.exp(ans)
        final_ans = expon / np.sum(expon)
        return np.round(final_ans, 4)
        pass
