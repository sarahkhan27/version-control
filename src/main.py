# Acknowledging the use of websites/ AI tools for additional help with date and time code
import datetime

# Ccurrent date and time in correct format YYYY-MM-DD HH:MM:SS
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Writing  date/time to version.md
with open("../../version.md", "w") as file:
    file.write(f"Current Date and Time: {current_time}")

