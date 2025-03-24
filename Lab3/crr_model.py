from typing import Union
import numpy as np
import numpy.typing as npt

class CRRModel():
    Numeric = Union[int, float]
    NumericList = list[int | float]
    NumericArray = npt.NDArray[np.int64 | np.float64]
    def __init__(self, endvalues: Union[NumericList, NumericArray], interest: Numeric):
        self.endvalues = endvalues
        if interest <= 0:
            raise ValueError("Interest must be greater than 0")
        self.interest = interest
    ## Static function c
    def price_on_2_state_1_period_market(u: Numeric, d: Numeric, r: Numeric, piu: Numeric, pid: Numeric):
        pstar = (1 + r - d) / (u - d)
        return (pstar * piu + (1 - pstar) * pid) / (1 + r)


