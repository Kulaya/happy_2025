import streamlit as st
from datetime import datetime
import time
from colorama import Fore
import pyfiglet

# Define the target New Year date
new_year = datetime(datetime.now().year + 1, 1, 1)

# Streamlit app
st.title("Happy New Year Countdown Timer")
st.write("The countdown to New Year begins!")

# Placeholder for countdown timer
placeholder = st.empty()

# Countdown loop
while datetime.now() < new_year:
    remaining = new_year - datetime.now()
    
    # Update the placeholder with the remaining time
    placeholder.markdown(f"### Time left: {remaining}")
    
    time.sleep(1)  # Sleep for a second

# Display Happy New Year message
st.success("🎉 Happy New Year!")
font = pyfiglet.figlet_format('Happy New Year')
st.markdown(f"<pre style='color: yellow;'>{font}</pre>", unsafe_allow_html=True)
