import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO

# Configure the Streamlit app layout and title
st.set_page_config(layout='wide', page_title="Background Removal")

# Main title for the app
st.write("Remove background from your image")

# Sidebar header
st.sidebar.write("## Upload and Download")

# Function to convert the processed image to bytes for downloading
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format='PNG')
    bytes_im = buf.getvalue()
    return bytes_im

def hide_streamlit_style():
    hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

hide_streamlit_style()
# Function to process the uploaded image and remove the background
def fix_image(upload):
    st.write('Original Image')
    image = Image.open(upload)
    st.image(image, caption="Original Image", use_container_width=True)

    with st.spinner("Removing background..."):
        fixed = remove(image)

    st.write("Fixed Image")
    st.image(fixed, caption="Fixed Image", use_container_width=True)

    # Add download button for the fixed image
    st.sidebar.markdown('\n')
    st.sidebar.download_button("Download Fixed Image", convert_image(fixed), 'fixed.png', 'image/png')

# Sidebar file uploader for the image
my_upload = st.sidebar.file_uploader("Upload the image", type=['png', 'jpg', 'jpeg'])

# Call the function to process the image if an image is uploaded
if my_upload is not None:
    fix_image(upload=my_upload)

