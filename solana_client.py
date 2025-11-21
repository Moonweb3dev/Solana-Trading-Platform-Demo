# Mocked Solana client for demo use only

import time, random

class MockSolanaClient:
    def __init__(self, rpc_url):
        self.rpc_url = rpc_url

    def get_recent_blockhash(self):
        return f"BlockHash-{int(time.time())}"

    def get_account_balance(self, pubkey):
        return round(1000 + random.random() * 500, 6)

    def fetch_orderbook(self, market):
        bids = [(20 - i * 0.01, 1 + i * 0.1) for i in range(5)]
        asks = [(20 + i * 0.01, 1 + i * 0.1) for i in range(5)]
        return {"bids": bids, "asks": asks, "market": market}

    def submit_order(self, market, side, price, size):
        status = random.choice(["filled", "partial", "open"])
        return {
            "order_id": f"ORD-{int(time.time()*1000)}",
            "market": market,
            "side": side,
            "price": price,
            "size": size,
            "status": status
        }

    def simulate_stream(self, market):
        while True:
            yield {
                "market": market,
                "price": round(20 + random.uniform(-0.5, 0.5), 3),
                "volume": round(1 + random.random() * 5, 3),
                "ts": time.time()
            }
            time.sleep(0.5)
