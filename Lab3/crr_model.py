import numpy as np
from abc import ABC, abstractmethod
import math
from pyqtgraph.flowchart.library.functions import modeFilter

class Instrument(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def price(self, trajectory):
        pass
class AmericanCall(Instrument):
    def __init__(self, K):
        super().__init__()
        self.K = K
    def price(self, trajectory):
        call_trajectory = np.array(trajectory) - self.K
        call_trajectory[call_trajectory < 0] = 0
        return np.max(call_trajectory)

class EuropeanCall(Instrument):
    def __init__(self, K):
        super().__init__()
        self.K = K
    def price(self, trajectory):
        return max(trajectory[-1]-self.K, 0)

class EuropeanPut(Instrument):
    def __init__(self, K):
        super().__init__()
        self.K = K
    def price(self, trajectory):
        return max(self.K - trajectory[-1], 0)

class MaximumInstrument(Instrument):
    def __init__(self):
        super().__init__()
    def price(self, trajectory):
        return max(trajectory)


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
    def price_instrument(self, instrument: Instrument, trajectory=None):
        if trajectory is None:
            trajectory = [self.S0]
        if len(trajectory) == self.T + 1:
            return instrument.price(trajectory)
        return (1/(1+self.r))*(self.pstar*self.price_instrument(instrument, trajectory+[trajectory[-1]*self.u]) + (1-self.pstar) * self.price_instrument(instrument, trajectory+[trajectory[-1]*self.d]))









def main():
    u = 1.1
    d = 0.9
    r = 0.05
    T = 5
    S0 = 100
    pstar = (1 + r - d) / (u - d)
    model = CRRModel(u, d, r, T, S0)
    strike = 150
    instrument = AmericanCall(strike)
    print(model.price_instrument(instrument))
    print((1+r)**(-T) * sum([math.comb(T,i) * (pstar**i) * ((1-pstar)**(T-i)) * max((S0 * (u**i) * (d**(T-i))) - strike,0) for i in range(T+1)]))
if __name__ == '__main__':
    main()

    
    


