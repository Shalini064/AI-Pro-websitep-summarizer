import gradio as gr
from summarizer import summarize_website    
gr.Interface(
    fn=summarize_website,
    inputs=gr.Textbox(label="Enter Website URL"),
    outputs=gr.Markdown(label="Summary"),
    title="Website Summarizer").launch(share=True)