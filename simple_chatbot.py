# Import necessary packages
import gradio as gr
from ibm_watsonx_ai import APIClient, Credentials
from ibm_watsonx_ai.foundation_models import Model, ModelInference
from ibm_watsonx_ai.foundation_models.schema import TextChatParameters
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames

# Model and project settings
# Directly specifying the LLAMA3 model
model_id = "meta-llama/llama-3-2-11b-vision-instruct"

# Set credentials to use the model
credentials = Credentials(
    url="https://us-south.ml.cloud.ibm.com",
)

# Set necessary parameters
params = TextChatParameters(temperature=0.1, max_tokens=512)


# Specifying project_id as provided
project_id = "skills-network"


# Initialize the model
model = ModelInference(
    model_id=model_id, credentials=credentials, project_id=project_id, params=params
)
# Your question


def generate_response(prompt_txt):
    messages = [{"role": "user", "content": [{"type": "text", "text": prompt_txt}]}]

    generated_response = model.chat(messages=messages)
    generated_text = generated_response["choices"][0]["message"]["content"]
    return generated_text


chat_app = gr.Interface(
    fn=generate_response,
    flagging_mode="never",
    inputs=gr.Textbox(label="Prompt", lines=2, placeholder="Enter your prompt"),
    outputs=gr.Textbox(label="AI reply"),
    title="Ai Chatbot",
    description="Ask any question and the chatbot will try to answer.",
)

chat_app.launch()
