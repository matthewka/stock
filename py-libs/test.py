import talib as ta
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    #a = np.array([1, 2, 3])  # Create a rank 1 array
    #a = np.random.random((100,))
    l = []
    for i in range(0, 100):
        l.append(i)

    a = np.array(l, dtype=np.float64)
    print(type(a))  # Prints "<class 'numpy.ndarray'>"
    print(a.shape)  # Prints "(3,)"
    print(a[0], a[1], a[2])  # Prints "1 2 3"
    a[0] = 5  # Change an element of the array
    print(a)  # Prints "[5, 2, 3]"

    b = np.array([[1, 2, 3], [4, 5, 6]])  # Create a rank 2 array
    print(b.shape)  # Prints "(2, 3)"
    print(b[0, 0], b[0, 1], b[1, 0])  # Prints "1 2 4"

    rsi55 = ta.RSI(a, 5)
    sma5 = ta.SMA(a, timeperiod=30)
    print(sma5)
    print(rsi55)
    plt.plot(rsi55)
    plt.show()


if __name__ == '__main__':
	main()