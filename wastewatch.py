import streamlit as st

# Set the title and description of the web app
st.title("Waste Watch - AI for Waste Classification")
st.markdown("Welcome to Waste Watch, an AI model for waste sorting and management.")

# Create a navigation menu
page = st.sidebar.selectbox(
    "Select a page",
    ("Overview", "Interactive Demo", "Waste Management", "About Us")
)

# Define the function for the "Overview" page
def overview_page():
    st.header("Project Overview")
    st.write("Waste Watch is an innovative AI model that helps automate the process of waste classification and sorting. It is designed to assist waste management and recycling facilities in identifying and segregating various types of waste materials efficiently. Our goal is to contribute to environmental sustainability and make waste management more efficient.")
    # Add more project overview details here

# Define the function for the "Interactive Demo" page
def interactive_demo():
    st.header("Interactive Demo")
    st.write("Try out our interactive demo to see how the AI model can classify waste materials. Upload an image, and the AI will provide you with the classification results.")
    # Add the interactive demo code here

# Define the function for the "Waste Management" page
def waste_management():
    st.header("Waste Management")
    st.write("Efficient waste management is crucial for a sustainable future. Waste Watch helps waste management facilities automate the sorting process, reducing errors and improving recycling rates.")
    # Add more information about waste management here

# Define the function for the "About Us" page
def about_us():
    st.header("About Us")
    st.write("Waste Watch is a project developed for the NYAS Challenge. Our team is passionate about environmental sustainability and using AI for positive change. We are excited to contribute to the waste management and recycling industry.")
    # Add team member details and contact information here

# Display the selected page
if page == "Overview":
    overview_page()
elif page == "Interactive Demo":
    interactive_demo()
elif page == "Waste Management":
    waste_management()
elif page == "About Us":
    about_us()
