import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Waste Watch - AI for Waste Classification",
    page_icon="🗑️",
    layout="wide"
)

<<<<<<< HEAD
=======
# Create a custom CSS style for the sidebar
sidebar_style = """
    background-color: ##0000FF;
    color: ##0000FF;
    padding: 20px;
    """
st.markdown(
    f'<style>{sidebar_style}</style>',
    unsafe_allow_html=True
)
>>>>>>> 966bf559937f7a1d62b11877e506d8601e5f8d82

<<<<<<< HEAD
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
=======
# Set the title and description of the web app
st.title("Waste Watch - AI for Waste Classification")
st.markdown("Welcome to Waste Watch, an AI model for waste sorting and management.")

# Create a navigation menu with custom styling
>>>>>>> 966bf559937f7a1d62b11877e506d8601e5f8d82
page = st.sidebar.selectbox(
    "Select a page",
    ("Overview", "Interactive Demo", "Waste Management", "About Us")
)

# Define the function for the "Overview" page with custom styling
def overview_page():
    st.header("Project Overview")
    st.write("Waste Watch is an innovative AI model that helps automate the process of waste classification and sorting. It is designed to assist waste management and recycling facilities in identifying and segregating various types of waste materials efficiently. Our goal is to contribute to environmental sustainability and make waste management more efficient.")
    # Add more project overview details here

# Define the function for the "Interactive Demo" page with custom styling
def interactive_demo():
    st.header("Interactive Demo")
    st.write("Try out our interactive demo to see how the AI model can classify waste materials. Upload an image, and the AI will provide you with the classification results.")
    # Add the interactive demo code here

# Define the function for the "Waste Management" page with custom styling
def waste_management():
    st.header("Waste Management")
    st.write("Efficient waste management is crucial for a sustainable future. Waste Watch helps waste management facilities automate the sorting process, reducing errors and improving recycling rates.")
    # Add more information about waste management here

# Define the function for the "About Us" page with custom styling
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
