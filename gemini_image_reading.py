import os
import google.generativeai as genai
import streamlit as st
from PIL import Image
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
gemini_api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=gemini_api_key)

st.title("Image Reading App")
a = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if a is not None:
    image = Image.open(a)
    st.image(image, caption="Uploaded Image", use_column_width=True)

prompt = st.text_input("Enter your prompt for the image :")

if st.button("Generate Response"):
    if a is not None and prompt:
        with st.spinner("Generating response..."):
            img = Image.open(a)
            model = genai.GenerativeModel('gemini-2.5-flash')
            response = model.generate_content([prompt,img])
        st.success("Response generated!")
        st.write("Response :")
        st.write(response.text)
    else:
        st.error("Please upload an image and enter a prompt.")

        