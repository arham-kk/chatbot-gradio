import gradio as gr
import openai

# Set up your OpenAI API credentials
openai.api_key = "ENTER OPENAI API"

# Define the OpenAI engine
ENGINE_NAME = "text-davinci-003"

# Define the function for generating a response
def generate_response(text):
    response = openai.Completion.create(engine=ENGINE_NAME, prompt=text, max_tokens=50, temperature=0.6, top_p=1.0, n=1, stop=None, timeout=10)
    return response.choices[0].text.strip()

# Create a Gradio interface
def chatbot(input_text):
    response = generate_response(input_text)
    return response

inputs = gr.inputs.Textbox(lines=2, placeholder="Enter your message here...")
outputs = gr.outputs.Textbox()

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Chatbot", height=400, width=800).launch()
