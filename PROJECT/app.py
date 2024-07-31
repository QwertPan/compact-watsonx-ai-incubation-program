# Import environment loading library
from dotenv import load_dotenv
from ibm_watsonx_ai.foundation_models import Model 
from ibm_watsonx_ai.foundation_models.extensions.langchain import WatsonxLLM
# Import system libraries
import os
# Import streamlit for the UI 
import streamlit as st
# CSV for extracting data from model output
import csv


# Load environment vars
load_dotenv()

model = "meta-llama/llama-3-70b-instruct"
# Models available:
#    "llama3": "meta-llama/llama-3-70b-instruct",
#    "granite_chat":"ibm/granite-13b-chat-v2",
#    "flanul": "google/flan-ul2",
#    "llama2": "meta-llama/llama-2-70b-chat",
#    "mixstral": 'mistralai/mixtral-8x7b-instruct-v01'

# Define credentials 
api_key = os.getenv("WATSONX_APIKEY", None)
ibm_cloud_url = os.getenv("IBM_CLOUD_URL", None)
project_id = os.getenv("PROJECT_ID", None)

if api_key is None or ibm_cloud_url is None or project_id is None:
    print("Ensure you copied the .env file that you created earlier into the same directory as this notebook")
else:
    creds = {
        "url": ibm_cloud_url,
        "apikey": api_key 
    }

# Define generation parameters 
params = {
    'decoding_method': "greedy",
    'min_new_tokens': 1,
    'max_new_tokens': 300,
    'random_seed': 42,
    # 'temperature': 0.2,
    # GenParams.TOP_K: 100,
    # GenParams.TOP_P: 1,
    'repetition_penalty': 1.05
}
    
# input is List of Dict from the session state
def format_chat_history(session_state):
    # made up a chat history
    chat_history=""
    for turn in session_state:
        chat_history+=f"""
        {turn['role']}: {turn['content']}
        """
    return chat_history



def prompt_template(question):
    #text = f"""[INST] <<SYS>>
    #You are a schedule organiser. You will receive the list of tasks that your user has for today and a new task. Find a place in the list for the new task based on its importance and the importance of existing tasks, and keep the rest of the list in the same order. Output the new list.
    #<</SYS>>
    #
    #QUESTION: {question} [/INST] ANSWER:
    #"""
    timewk = "17:00-21:00"
    timewknd = "12:00-16:00"
    text = f"""[INST] <<SYS>>
You are a schedule organiser. Time to be scheduled for on weekdays is {timewk}, and {timewknd} on weekends. Students need time to take breaks. You will receive the list of tasks that your user has to complete, and examples. Order the tasks based on their importance and length. Output the new list, including the timestamps for each task. Output in CSV format where each task is a new record, and the date, time and name of a task are separate fields. Times are in 24 hour format. Break should be formatted as a task with the name "Break". Terminate the list with a | character. Output nothing but the list.
Example:
Input: Today: July 27, Saturday
Study group, 1.5 hours, August 3
History project, 50 minutes, July 30
Research paper, 2 hours, August 3
Coding assignment, 50 minutes, August 3
Quiz preparation, 1.5 hours, August 3
Output:  "July 27", "12:00-12:50", "History project"
"July 27", "12:50-13:40", "Coding assignment"
"July 27", "13:40-14:00", "Break"
"July 27", "14:00-16:00", "Research paper"
"July 28", "12:00-13:30", "Study group"
"July 28", "13:30-15:00", "Quiz preparation"
"July 28", "15:00-16:00", "Break"
"July 29", "17:00-21:00", "Break"
"July 30", "17:00-21:00", "Break"
"July 31", "17:00-21:00", "Break"
"August 1", "17:00-21:00", "Break"
"August 2", "17:00-21:00", "Break"
"August 3", "12:00-16:00", "Break"|
<</SYS>>
Input: {question}
Output: [/INST]
"""
    #print("Prompt: ", text) # debug
    return text

# Title for the app
st.title('Project')

#option = st.selectbox(
#    "select model for Q&A",
#    tuple(models),
#)

modelsetup = Model(
    model_id=model,
    params=params,
    credentials=creds,
    project_id=project_id,
    space_id=None)

llm = WatsonxLLM(modelsetup)


# Initialize chat history
#if "messages" not in st.session_state:
#    st.session_state.messages = []

# Display chat messages from history on app rerun
#for message in st.session_state.messages:
#    with st.chat_message(message["role"]):
#        st.markdown(message["content"])

#chat_hist = format_chat_history(st.session_state.messages)

if prompt := st.chat_input("Enter your prompt here"):
    # Display user message in chat message container
    #st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    #st.session_state.messages.append({"role": "user", "content": prompt})

    current_prompt = prompt_template(prompt)

    # this is the generation part of the model
    #response = llm(chat_hist+current_prompt)
    response = llm(current_prompt)
    print(response)
    # Display assistant response in chat message container
    #with st.chat_message("assistant"):
    #    st.markdown(response)
    # Add assistant response to chat history
    #st.session_state.messages.append({"role": "assistant", "content": response})