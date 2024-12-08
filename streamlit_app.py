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
