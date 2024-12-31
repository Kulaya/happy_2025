import streamlit as st
from datetime import datetime, timedelta
import pytz
from colorama import Fore
import pyfiglet

# Set your local timezone (e.g., 'Africa/Nairobi' for East Africa Time)
local_tz = pytz.timezone("Africa/Nairobi")

# Define the target New Year date in your local timezone
current_year = datetime.now(pytz.utc).astimezone(local_tz).year
new_year = local_tz.localize(datetime(current_year + 1, 1, 1, 0, 0, 0))  # January 1st, Midnight, Local Time

# Streamlit app
st.title("New Year Countdown")
st.write("The countdown to New Year begins!")

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
