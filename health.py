###health Management APP
from dotenv import load_dotenv


load_dotenv()##load all the environment variables

import strenlit as st
import os 
import google.generativeai as genai
from PIL import image 
genai.configure(api_key=os.gentenv
("GOOGLE_API_KEY"))

##function to load Google Gemini PRO viaion API And get response

def get_gemini_response(input,image,promot)
;
model=genai.GenerativeModel('gemini-pro-vision)
response=model.genrate_content([input,image[0],,promot])
return response.text


def input_image_setup(uploaded_file):
#Check if a file has been uploaded
if uploaded_file is not none:
##Read the file into bytes
bytes_data=uploaded_file.getvalue()

image_parts=[
  {
    "mime_type": uploaded_file.type,#Get the mime type of the uploaded file 
      "data":bytes_data
  }
]
return image_parts
else:
raise FileNotFoundError("No file uploaded")
 

##initialize our streamlit app


st.set_page_config(page_title="Gemini Health App")

st.header("Gemini Health App")
input=st.text_input("Input Promopt:"Key="input")
uploaded_file=st.file_uploader("choose an image...",type=["jpg","jpeg","png"])
image=""
if uplaoded_file is niot None:
image=Image.open(uploaded_file)
st.image(image,caption="Uploaded Image.",)
ua=se_column_width=True)


submit=st.button("Tell me the total calories")

input_prompt="""
You are expert in nutrionist where you need  to see the food items from the image 
 and calculate the total calories,also provide the details of every food items with calories intake below format

     1.Item 1 - no of calories
     2.Item 2 - no of calories
     ----
     ----


"""

##If submit:
image_data=input_setup(uploaded_file)
response =get_gemini_response
(input_prompt,image_data,input)
st.subheader("The Response is")
    st.write(response)

 
