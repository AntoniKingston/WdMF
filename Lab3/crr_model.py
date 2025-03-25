from __future__ import annotations
from typing import Union, Optional
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
    Numeric = Union[int, float, None]
    def __init__(self, val: Numeric, right: Optional[Node] = None, left: Optional[Node] = None):
        self.val = val
        self.right = right
        self.left = left

    def build_recombining_tree(depth: int) -> Optional[Node]:
        """
        Builds a full recombining binomial tree of given depth.

        :param depth: Depth of the tree.
        :param value_function: Function to generate values for nodes.
        :return: Root node of the recombining tree.
        """
        if depth < 0:
            return None

        # Dictionary to store already created nodes for recombination
        memo = {}

        def create_node(level: int, index: int) -> Node:
            """Recursively creates a recombining binomial tree."""
            if level > depth:
                return None

            if (level, index) in memo:  # Ensure recombination
                return memo[(level, index)]

            # Create children first
            left_child = create_node(level + 1, index)
            right_child = create_node(level + 1, index + 1)

            # Create node and store it for recombination
            node = Node(None, right_child, left_child)
            memo[(level, index)] = node

            return node

        return create_node(0, 0)
    def fill_tree_leafs(self, list_of_values):


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
        root = Node.build_recombining_tree()


        self.endvalues = endvalues
        ## form simple markets tree
        if r <= 0:
            raise ValueError("Interest must be greater than 0")
        self.r = r

    
    


