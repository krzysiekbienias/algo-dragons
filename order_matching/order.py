from typing import TypeVar, Iterable, Tuple, Dict, List
import os
import heapq as h
from collections import deque
from dataclasses import dataclass, field


class OrderBookInterface:
    def __init__(self):
        pass

    def validate_command(self):
        pass

    def add_new_trade(self):
        pass

    def ammend_trade(self):
        pass

    def match(self):
        pass

    def generate_random_trade(self):
        pass

    def cancel_trade(self):
        pass


class Commandhandler:
    def __init__(self, command: str) -> None:
        self._command = command

    def parse_command_2_hm(self):
        pass


@dataclass
class Order:
    """
    Single order storage.
    """
    action: str
    order_id: int
    timestamp: int
    symbol: str
    order_type: str
    side: str
    price: float
    quantity: int


@dataclass
class LimitOrder(Order):
    order_type: str = field(init=False, default="L")


@dataclass(kw_only=True)
class MarketOrder(Order):
    order_type: str = field(default="M")

    def __post_init__(self):
        self.price = 0 if self.side == "S" else float("inf")  #strange


class IOCOrder(Order):
    pass
