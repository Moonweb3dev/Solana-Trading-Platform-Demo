# Demo CLI entrypoint

from .solana_client import MockSolanaClient
from .trading_engine import TradingEngine
from .bot_api import MockBotAPI
from .config import SOLANA_RPC
from .utils import log

def main():
    log("Starting demo...")
    client = MockSolanaClient(SOLANA_RPC)
    engine = TradingEngine(client)
    engine.start(runtime=6)
    bot = MockBotAPI()
    bot.send("Demo finished.")

if __name__ == "__main__":
    main()
