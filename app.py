import streamlit as st
import base64

# Encode the image in base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Load the logo image
logo_base64 = get_base64_image("logo.png")

# CSS styling
st.markdown(f"""
    <style>
        .container {{
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: flex-start;
            padding: 20px;
        }}
        .column-left {{
            flex: 1;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .column-right {{
            flex: 3;
            display: flex;
            justify-content: flex-start;
            align-items: center;
        }}
        .logo {{
            width: 150px;
        }}
        h1 {{
            font-family: 'Arial', sans-serif;
            font-size: 48px;
            margin: 0;
            padding-left: 20px;
        }}
        h1 .cloud {{
            color: black;
        }}
        h1 .solutions {{
            color: #EF4444;
        }}
    </style>
    <div class="container">
        <div class="column-left">
            <img src="data:image/png;base64,{logo_base64}" alt="Cloud Solutions Logo" class="logo">
        </div>
        <div class="column-right">
            <h1>
                <span class="cloud">CLOUD</span> <span class="solutions">SOLUTIONS</span>
            </h1>
        </div>
    </div>
""", unsafe_allow_html=True)
