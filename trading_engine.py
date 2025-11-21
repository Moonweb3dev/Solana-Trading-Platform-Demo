# Demo trading engine (non-functional)

from .utils import log
from .config import DEFAULT_SYMBOL, DEFAULT_POSITION_SIZE, MAX_OPEN_POSITIONS
import time, threading

class Position:
    def __init__(self, pid, side, price, size):
        self.id = pid
        self.side = side
        self.entry = price
        self.size = size
        self.opened = time.time()

class TradingEngine:
    def __init__(self, client, symbol=DEFAULT_SYMBOL):
        self.client = client
        self.symbol = symbol
        self.open_positions = {}
        self.lock = threading.Lock()

    def compute_signals(self, tick):
        price = tick["price"]
        sma_short = 20.0
        sma_long = 20.3

        if price < sma_short * 0.995:
            return {"side": "buy", "price": price}
        if price > sma_long * 1.005:
            return {"side": "sell", "price": price}

    def execute_signal(self, signal):
        order = self.client.submit_order(self.symbol, signal["side"], signal["price"], DEFAULT_POSITION_SIZE)
        if order["status"] != "open":
            pos = Position(order["order_id"], signal["side"], order["price"], DEFAULT_POSITION_SIZE)
            with self.lock:
                self.open_positions[pos.id] = pos
        log(f"Order executed: {order}")
        return order

    def start(self, runtime=8):
        stream = self.client.simulate_stream(self.symbol)
        start = time.time()
        for tick in stream:
            s = self.compute_signals(tick)
            if s:
                self.execute_signal(s)
            if time.time() - start > runtime:
                break
        log("Demo session complete.")
