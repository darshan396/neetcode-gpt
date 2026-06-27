import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        max_z = z.max()
        ans = np.zeros(len(z))
        sum_den = 0
        for i in range(len(z)):
            ans[i] = np.exp(z[i] - max_z)
            sum_den += ans[i]
        
        for i in range(len(z)):
            ans[i] = ans[i]/sum_den
            ans[i] = round(ans[i],4)
        return ans
        pass
