import numpy as np

a, b = np.linalg.solve([
        [2,1],
        [1,-2]
    ],
    [4, -3]
)

c, d = np.linalg.solve([
        [5,-1],
        [4,3]
    ],
    [11, 24]
)

print(a, b, c, d)
