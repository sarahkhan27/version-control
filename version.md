# Acknowledging the use of websites/ AI tools for additional help with date and time codey

from datetime import datetime

# Get the current date and time in the required format
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write to version.md in the repository
with open('../version.md', 'w') as file:
    file.write(f"Current Date and Time: {current_time}")

