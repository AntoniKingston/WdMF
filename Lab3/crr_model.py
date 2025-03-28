import numpy as np
from abc import ABC, abstractmethod
from pyqtgraph.flowchart.library.functions import modeFilter

class Instrument(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def price(self, trajectory):
        pass
class American_call(Instrument):
    def __init__(self, K):
        super().__init__()
        self.K = K
    def price(self, trajectory):
        call_trajectory = trajectory - self.K
        call_trajectory[call_trajectory < 0] = 0
        return np.max(call_trajectory)


class CRRModel():
    def __init__(self, u, d, r, T, S0):
        self.u = u
        self.d = d
        self.r = r
        self.pstar = (1 + r - d) / (u - d)
        self.T = T
        self.S0 = S0
        stock_price = [[S0*(u**(j))*(d**(i-j)) for j in range(i+1)] for i in range(0, T+2)]
        self.stock_price = stock_price
    #instrument is a function that takes in T+1 arguments and returns single value
    def price_instrument(self, instrument):
        #generating binary sequence
        rational_prices = [[None for j in range(i + 1)] for i in range(0, self.T + 2)]





def main():
    model = CRRModel(1.1, 0.9, 1.05, 5, 100)
    print(model.stock_price)
if __name__ == '__main__':
    main()

    
    


