import streamlit as st
from datetime import datetime
import time
from colorama import Fore
import pyfiglet

# Define the target New Year date
new_year = datetime(datetime.now().year + 1, 1, 1)

# Streamlit app
st.title("New Year Countdown")
st.write("The countdown to New Year begins!")

# Placeholders for countdown timer and current time
countdown_placeholder = st.empty()
time_placeholder = st.empty()

# Countdown loop
while datetime.now() < new_year:
    current_time = datetime.now()  # Get the current time
    remaining = new_year - current_time  # Calculate remaining time
    
    # Update placeholders
    countdown_placeholder.markdown(f"### Time left: {remaining}")
    time_placeholder.markdown(f"**Current Time:** {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    time.sleep(1)  # Sleep for a second

# Display Happy New Year message
st.success("🎉 Happy New Year!")
font = pyfiglet.figlet_format('Happy New Year')
st.markdown(f"<pre style='color: yellow;'>{font}</pre>", unsafe_allow_html=True)
