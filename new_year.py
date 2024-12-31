import streamlit as st
from datetime import datetime, timedelta
import pytz
import time  # Ensure time is imported
from colorama import Fore
import pyfiglet
from calendar import calendar

# Set your local timezone (e.g., 'Africa/Nairobi' for East Africa Time)
local_tz = pytz.timezone("Africa/Nairobi")

# Streamlit app
st.title("New Year Countdown with Custom Time Adjustment")
st.write("Countdown to a user-defined target time or New Year begins!")

# Input for user-specified time adjustment (in seconds)
adjust_time_seconds = st.number_input(
    "Enter time adjustment in seconds (default is 0 for New Year):",
    min_value=0, value=0, step=1
)

# Define the target time based on user adjustment
current_year = datetime.now(pytz.utc).astimezone(local_tz).year
new_year = (
    datetime.now(pytz.utc).astimezone(local_tz) + timedelta(seconds=adjust_time_seconds)
    if adjust_time_seconds > 0
    else local_tz.localize(datetime(current_year + 1, 1, 1, 0, 0, 0))
)

# Placeholders for countdown timer and current time
countdown_placeholder = st.empty()
time_placeholder = st.empty()

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

# Decorative New Year ASCII art
ascii_art = '\n'.join(
    [''.join(
        [('Happy New Year'[(x-y) % 11]
          if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1)
             ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ')
         for x in range(-30, 30)]
     ) for y in range(15, -15, -1)]
)
st.markdown(f"<pre style='color: green;'>{ascii_art}</pre>", unsafe_allow_html=True)

# Final custom message
st.write("🎉 **Aviti Tech Solutions** wishes you a fantastic year ahead! 🎉")
def main():
    st.title("2025 Calendar")
    year = 2025
    cal_str = calendar(year)
    st.text(cal_str)
