import streamlit as st
from datetime import datetime, timedelta
import pytz
import time  # Ensure time is imported
from colorama import Fore
import pyfiglet
from calendar import*

# Set your local timezone (e.g., 'Africa/Nairobi' for East Africa Time)
local_tz = pytz.timezone("Africa/Nairobi")

# Define the target New Year date in your local timezone
current_year = datetime.now(pytz.utc).astimezone(local_tz).year
new_year = local_tz.localize(datetime(current_year + 1, 1, 1, 0, 0, 0))  # January 1st, Midnight, Local Time

# Streamlit app
st.title("Happy New Year Countdown Timer")
st.write("The countdown to New Year begins!")

# Placeholders for countdown timer and current time
time_placeholder = st.empty()
countdown_placeholder = st.empty()


# Countdown loop
while datetime.now(pytz.utc).astimezone(local_tz) < new_year:
    # Get the current time in local timezone
    current_time = datetime.now(pytz.utc).astimezone(local_tz)
    
    # Calculate remaining time
    remaining = new_year - current_time
    
    # Update placeholders
    countdown_placeholder.markdown(f"### Time left: {str(remaining).split('.')[0]}")  # Remove microseconds
    time_placeholder.markdown(f"**Current Time:** {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Sleep for a second
    time.sleep(1)

# Display Happy New Year message
st.success("🎉 Happy New Year!")
font = pyfiglet.figlet_format('Happy New Year')
st.markdown(f"<pre style='color: yellow;'>{font}</pre>", unsafe_allow_html=True)

 #Print celebratory messages in the terminal
print("Happy New Year 2025! Wishing you a fantastic year ahead!")

# Generate ASCII art heart
print('\n'.join(
    [''.join(
        [('Happy New Year'[(x-y) % 11]
          if ((x * 0.05)**2 + (y * 0.1)**2 - 1)**3 - (x * 0.05)**2 * (y * 0.1)**3 <= 0 else ' ')
         for x in range(-30, 30)])
     for y in range(15, -15, -1)]
))
print("Aviti Tech Solutions!!")

year = 2025
print(calendar(year, 2, 1, 8, 4))
