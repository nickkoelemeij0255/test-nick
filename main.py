
import pandas as pd
import streamlit as st

# Configure the page
st.set_page_config(
    page_title="Map Visualization App",
    page_icon="🗺️",
)

st.title("Map Visualization")
st.sidebar.success("Select a page above.")

# Path to your Excel file
excel_file_path = "C:/Users/nikoe/Desktop/MyAssets (1).xlsx"


# Read the Excel file
try:
    df = pd.read_excel(excel_file_path)
    
    #st.dataframe(df.head())  # Display first few rows
    if 'asset_longitude' in df.columns and 'asset_latitude' in df.columns:
        df = df.rename(columns={
            'asset_longitude': 'lon',
            'asset_latitude': 'lat'
        })
        
    else:
        st.error("The columns 'asset_longitude' or 'asset_latitude' are not found in the Excel file.")

    # Check if latitude and longitude columns exist
    if 'lat' in df.columns and 'lon' in df.columns:
        # Display the map with markers
        st.write("Map with markers:")
        st.map(df[['lat', 'lon']])
    else:
        st.error("The Excel file must contain 'latitude' and 'longitude' columns.")
except Exception as e:
    st.error(f"Error reading the file: {e}")
'''
import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth

# Configure the page
st.set_page_config(
    page_title="Map Visualization App",
    page_icon="🗺️",
    layout="wide"
)

# Define user credentials with hashed passwords
users = {
    "usernames": {
        "clientA": {
            "name": "Client A",
            "password": "$2b$12$12345..."  # Replace with actual hash
        },
        "clientB": {
            "name": "Client B",
            "password": "$2b$12$67890..."  # Replace with actual hash
        }
    }
}

# Initialize the authenticator
authenticator = stauth.Authenticate(
    users,
    "map_vis_app_cookie",  # Cookie name
    "4f2b3d9a8f29e6b7c4d9f2c8a1e6a3b4",  # Signature key
    cookie_expiry_days=1
)

# Login mechanism
name, authentication_status, username = authenticator.login("Login", location="sidebar")

if authentication_status:
    st.sidebar.success(f"Welcome, {name}!")

    # Path to your Excel file
    excel_file_path = "C:/Users/nikoe/Desktop/MyAssets (1).xlsx"

    # Read the Excel file
    try:
        df = pd.read_excel(excel_file_path)

        if 'asset_longitude' in df.columns and 'asset_latitude' in df.columns:
            df = df.rename(columns={
                'asset_longitude': 'lon',
                'asset_latitude': 'lat'
            })
            st.title("Map Visualization")
            st.write("Map with markers:")
            st.map(df[['lat', 'lon']])
        else:
            st.error("The Excel file must contain 'latitude' and 'longitude' columns.")
    except Exception as e:
        st.error(f"Error reading the file: {e}")

    # Logout button
    authenticator.logout("Logout", location="sidebar")

elif authentication_status is False:
    st.error("Username or password is incorrect")

elif authentication_status is None:
    st.warning("Please enter your username and password")


'''