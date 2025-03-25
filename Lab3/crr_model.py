from typing import Union, Optional
from __future__ import annotations
import numpy as np
import numpy.typing as npt

class TwoStateInstrument():
    Numeric = Union[int, float]
    def __init__(self, u: Numeric, d: Numeric):
        if d>u:
            raise ValueError("d musn't be greater than u")
        self.u = u
        self.d = d

class Node():
    Numeric = Union[int, float]
    def __init__(self, val: Numeric, right: Optional["Node"] = None, left: Optional["Node"] = None):
        self.val = val
        self.right = right
        self.left = left

class CRRModel():
    Numeric = Union[int, float]
    NumericList = list[int | float]
    NumericArray = npt.NDArray[np.int64 | np.float64]
    class TwoStateSinglePeriodMarket():
        Numeric = Union[int, float]
        def __init__(self, u: Numeric, d: Numeric, r: Numeric):
            if u<r or d>r:
                raise ValueError("Provided values of u, d and r induce an arbitrage")
            self.u = u
            self.d = d
            self.r = r
            #risk-neutral measure
            self.pstar = (1 + r - d) / (u - d)
        def price_instrument(self, instrument: TwoStateInstrument):
            xu = instrument.u
            xd = instrument.d
            return self.pstar * xu + (1 - self.pstar) * xd





    def __init__(self, endvalues: Union[NumericList, NumericArray], r: Numeric):
        ## form rational prices tree
        curr_formation_layer = [Node(endvalues[i]) for i in range(len(endvalues))]

        for i in range(len(endvalues), 0, -1):


        self.endvalues = endvalues
        ## form simple markets tree
        if r <= 0:
            raise ValueError("Interest must be greater than 0")
        self.r = r

    
    


