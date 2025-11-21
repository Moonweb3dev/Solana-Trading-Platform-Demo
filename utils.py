import datetime, sys

def log(msg):
    ts = datetime.datetime.utcnow().isoformat()
    print(f"[{ts}] {msg}", file=sys.stdout)
