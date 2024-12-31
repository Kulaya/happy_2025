import streamlit as st
from datetime import datetime
import time
import pytz
from colorama import Fore
import pyfiglet

# Set your local timezone (e.g., 'Africa/Nairobi' for East Africa Time)
local_tz = pytz.timezone("Africa/Nairobi")

# Define the target New Year date in your local timezone
new_year = datetime(datetime.now().year + 1, 1, 1, tzinfo=pytz.utc).astimezone(local_tz)

# Streamlit app
st.title("New Year Countdown")
st.write("The countdown to New Year begins!")

# Placeholders for countdown timer and current time
countdown_placeholder = st.empty()
time_placeholder = st.empty()

# Countdown loop
while datetime.now(pytz.utc).astimezone(local_tz) < new_year:
    current_time = datetime.now(pytz.utc).astimezone(local_tz)  # Get the current time in local timezone
    remaining = new_year - current_time  # Calculate remaining time
    
    # Update placeholders
    countdown_placeholder.markdown(f"### Time left: {remaining}")
    time_placeholder.markdown(f"**Current Time:** {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    time.sleep(1)  # Sleep for a second

# Display Happy New Year message
st.success("🎉 Happy New Year!")
font = pyfiglet.figlet_format('Happy New Year')
st.markdown(f"<pre style='color: yellow;'>{font}</pre>", unsafe_allow_html=True)
