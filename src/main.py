# Acknowledging the help of some  website tools for fixing code errors

from datetime import datetime
from zoneinfo import ZoneInfo #to adjust the VSCode timezone to PST

# Current date and time in required formatS
current_time = datetime.now(ZoneInfo("US/Pacific")).strftime("%Y-%m-%d %H:%M:%S")
print(f"Current date and time: {current_time}")

# Writing to version.md
with open("../version.md", "w") as file:
    file.write(f"Current date and time (PST): {current_time}")
