import os
from turtle import up
import streamlit as st
from PIL import Image

st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
st.title("Image Enhancer")

def delete_imgs(dirname):
    for files in os.listdir(dirname):
        os.remove(os.path.join(dirname, files))

try:
    dirname = os.path.join('results', 'cmp')
    delete_imgs(dirname)

    dirname = os.path.join('results', 'cropped_faces')
    delete_imgs(dirname)

    dirname = os.path.join('results', 'restored_faces')
    delete_imgs(dirname)

    dirname = os.path.join('results', 'restored_imgs')
    delete_imgs(dirname)
        
    dirname = os.path.join('tempDir')
    delete_imgs(dirname)

except FileNotFoundError:
    pass

def save_uploadedfile(uploadedfile):
    with open(os.path.join("tempDir", uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
        # return st.success(f"Saved File:{uploadedfile.name} to tempDir")
        
options = ["Enhance Images", "About"]
# st.write(os.getcwd())
menu = st.sidebar.selectbox("Select an Option", options)
if menu == "Enhance Images":
    col1, col2 = st.columns([1, 0.3])
    with col1:
        uploaded_file = st.file_uploader("Upload Image", type = ["jpg", "jpeg", "png"])
    with col2:
        st.markdown('###')
        st.markdown('###')
        sample = st.button('Use Sample Image')
    if sample:
        path = os.path.join('10045.png')
        # st.write(path)
        # st.write(f"{uploaded_file.name()}")
        with st.spinner("Please wait while we process your image.."):
            os.system(f"python inference_gfpgan.py -i {path} -o results -v 1.3 -s 2")
            # comp_results = f'results/restored_imgs/{uploaded_file.name}'
            with st.expander("Results", expanded=True):
                col11, col22 = st.columns(2)
                with col11:
                    st.write("Uploaded Image")
                    # st.image(Image.open(f'{os.getcwd()}\\tempDir\{uploaded_file.name}'))
                    st.image(Image.open(os.path.join('10045.png')))
                with col22:
                    st.write("Enhanced Image")
                    st.image(Image.open(path))
            with st.expander("Comparative Results", expanded=True):
            # comp_results = "\\results\\cmp"
            # comp_path = os.path.join('results', 'cmp')
                files = os.listdir(os.path.join('results', 'cmp'))
                for f in files:
                    st.write(f)
                    st.image(Image.open(os.path.join('results', 'cmp', f'{f}')))
                
        
    if uploaded_file is not None:
        save_uploadedfile(uploaded_file)
        enhance = st.button("Enhance the Image")
        if enhance:
            path = os.path.join('results', 'restored_imgs', f'{uploaded_file.name}')
            with st.spinner("Please wait while we process your image.."):
                os.system(f"python inference_gfpgan.py -i {os.path.join('tempDir', f'{uploaded_file.name}')} -o results -v 1.3 -s 2")
                with st.expander("Results", expanded=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("Uploaded Image")
                        st.image(Image.open(os.path.join('tempDir', f'{uploaded_file.name}')))
                    with col2:
                        st.write("Enhanced Image")
                        st.image(Image.open(path))

        with st.expander("Comparative Results"):
            files = os.listdir(os.path.join('results', 'cmp'))
            for f in files:
                st.write(f)
                st.image(Image.open(os.path.join('results', 'cmp', f'{f}')))

    if uploaded_file is None:     
        st.write("Sample Results")
        res_path = os.path.join('Demo', 'restored_imgs')
        
        with st.expander("View Sample Results:", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
            # st.write(res_path)
                # st.image(Image.open(f'{res_path}\Blake_Lively.jpg'))
                st.image(Image.open(os.path.join('demo', 'restored_imgs', 'Blake_Lively.jpg')))
            with col2:
                st.image(Image.open(os.path.join('demo', 'restored_imgs', 'Blake_Lively_restored.jpg')))


if menu == "About":
    st.sidebar.image('assets/gfpgan_logo.png')
    st.write("Test App")