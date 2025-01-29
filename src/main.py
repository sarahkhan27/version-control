# Acknowledging the help of some  website tools for fixing code errors

from datetime import datetime

# Current date and time in required format
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Current date and time: {current_time}") 

# Write the current date and time to version.md
with open("version.md", "w") as file:
    file.write(f"Current date and time: {current_time}")

