import numpy as np

def cumulative_mean(X):
    X = np.cumsum(X, axis = 1)
    Y = np.arange(1, len(X) + 1)
    for i in range(1, len(X) + 1):
        X /= Y
    return X


a = np.array[4, 5]
print(a)
# a = np.cumsum(a)
# b = np.arange(1, len(a) + 1)
# print(a)
# print(b)
# print(a / b)
#print(cumulative_mean(a))