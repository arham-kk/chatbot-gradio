import gradio as gr
import random
import time
import openai

# Set up OpenAI GPT-3.5 credentials
openai.api_key = "YOUR_OPENAI_API_KEY"

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    def user(user_message, history):
        return "", history + [[user_message, None]]

    def bot(history):
        user_message = history[-1][0]
        prompt = "User: " + user_message + "\nBot:"
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can use other engines as well
            prompt=prompt,
            max_tokens=50
        )
        bot_message = response.choices[0].text.strip()
        history[-1][1] = ""
        for character in bot_message:
            history[-1][1] += character
            time.sleep(0.05)
            yield history

    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )
    clear.click(lambda: None, None, chatbot, queue=False)
    
demo.queue()
demo.launch()
