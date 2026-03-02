import gradio as gr
import requests
# This file defines the Gradio-based user interface for the Smart Contract Assistant.
#  It allows users to upload documents and interact with the assistant through a chat interface.
#  The UI communicates with the backend API to handle document processing and question-answering.

API_URL = "http://localhost:8000"

def upload_contract(file):
    with open(file.name, "rb") as f:
        response = requests.post(f"{API_URL}/upload", files={"file": f})
    return response.json().get("message", "Upload Failed")

def chat_with_assistant(message, history):
    response = requests.post(f"{API_URL}/ask", params={"question": message})
    return response.json().get("answer", "Error connecting to backend.")
# Gradio UI setup
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Your Smart  Q&A Assistant")
    
    with gr.Row():
        file_input = gr.File(label="Upload (PDF/DOCX)")
        upload_btn = gr.Button("Index content")
    
    status = gr.Textbox(label="Status", interactive=False)
    upload_btn.click(upload_contract, inputs=file_input, outputs=status)
    
    gr.ChatInterface(fn=chat_with_assistant, title="Ask about the content of your uploaded documentsf").style(height=400)

if __name__ == "__main__":
    demo.launch(server_port=7860)
