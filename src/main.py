# Acknowledging referance to/ help from some website tools for fixing codes/ errors

from datetime import datetime
import pytz

#PST timezone 
timezone = pytz.timezone("US/Pacific")

# Current date and time in required format PST
current_time = datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
print(f"Current date and time: {current_time}")

# Write the current date and time to version.md
with open("../version.md", "w") as file:
    file.write(f"Current date and time (PST): {current_time}")

