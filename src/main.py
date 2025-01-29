# Acknowledging referance to/ help from some website tools for fixing codes/ errors

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# Manually apply the UTC -8:00 offset (for PST)
pst = ZoneInfo("US/Pacific")

# Get the current time in UTC
utc_now = datetime.now(pytz.utc)

# Convert to PST (UTC -8 hours)
pst_time = utc_now - timedelta(hours=8)

# Format the time in the desired format
formatted_time = pst_time.strftime("%Y-%m-%d %H:%M:%S")

# Write the current date and time to version.md
with open("../version.md", "w") as file:
    file.write(f"Current date and time (PST): {formatted_time}")

