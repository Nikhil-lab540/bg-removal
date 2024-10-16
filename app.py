import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO

def hide_streamlit_style():
    hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """
    st.markdown(hide_st_style, unsafe_allow_html=True)



st.set_page_config(layout='wide', page_title="Background Removal")

st.write("Remove background from your image")

st.sidebar.write("## Upload and Download")
hide_streamlit_style()

def convert_image(img):
    bug = BytesIO()
    img.save(bug, format='PNG')  # Change Save to save
    bytes_im = bug.getvalue()
    return bytes_im

def fix_image(upload):
    st.write('Original Image')
    image = Image.open(upload)
    st.image(image)

    fixed = remove(image)
    st.write("Fixed Image")
    st.image(fixed)

    # Add download button for the fixed image
    st.sidebar.markdown('\n')
    st.sidebar.download_button("Download Fixed Image", convert_image(fixed), 'fixed.png', 'image/png')

# Sidebar file uploader
my_upload = st.sidebar.file_uploader("Upload the image", type=['png', 'jpg', 'jpeg'])

if my_upload is not None:
    fix_image(upload=my_upload)


