import gradio as gr
import google.generativeai as genai
import os
from dotenv import load_dotenv
import PIL.Image

load_dotenv()

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-pro-vision")

    

def process_image(img_path, prompt):
    print("Image Path:", img_path)
    print("Prompt:", prompt)
    
    img = PIL.Image.open(img_path)
    response = model.generate_content([prompt, img], stream=True)
    response.resolve()
    return response.text

iface = gr.Interface(
    fn=process_image,
    inputs=[gr.Image(type="filepath"), gr.Textbox()],
    outputs="text",
    live=False,
)


iface.launch(share=True)
