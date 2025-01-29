# Acknowledging the use of website tools for additional help

from datetime import datetime

# Current date and time in required formatS
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Writing to version.md
with open("version.md", "w") as file:
    file.write(f"Current Date and Time: {current_time}")

