import streamlit as st

# Set the title of the web app
st.title("Waste Watch")

# Add a button to the web app
if st.button("Click me"):
    st.write("You clicked the button!")

# Display text
st.write("This is a simple Streamlit web app.")

def overview_page():
    st.title("Project Overview")
    st.write("This is the overview page for your project.")
    # Add your project overview content here

# Create a function for another page
def other_page():
    st.title("Another Page")
    st.write("This is another page of your Streamlit app.")
    # Add content for this page here

# Create a navigation menu
page = st.sidebar.selectbox(
    "Select a page",
    ("Overview", "Another Page")
)

# Display the selected page
if page == "Overview":
    overview_page()
elif page == "Another Page":
    other_page()
