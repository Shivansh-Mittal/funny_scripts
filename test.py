from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path

IST = ZoneInfo("Asia/Kolkata")

log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

log_file = log_dir / "timestamps.log"

now = datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S %Z")

with open(log_file, "a") as f:
    f.write(f"{now}\n")

print(f"Logged timestamp: {now}")
