# AI libs
import os
from dotenv import load_dotenv
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.foundation_models.extensions.langchain import WatsonxLLM
from datetime import date

load_dotenv()

timewk = "17:00-21:00"
timewknd = "12:00-16:00"

api_key = os.getenv("WATSONX_APIKEY", None)
ibm_cloud_url = os.getenv("IBM_CLOUD_URL", None)
project_id = os.getenv("PROJECT_ID", None)
model = "meta-llama/llama-3-70b-instruct"

if api_key is None or ibm_cloud_url is None or project_id is None:
    print("where env")
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
    'stop_sequences': ["|"],
    'random_seed': 42,
    # 'temperature': 0.2,
    # GenParams.TOP_K: 100,
    # GenParams.TOP_P: 1,
    #'repetition_penalty': 1.05
    #'input_text':False
}

def make_prompt(tasks): # TODO: add timewk and timewknd params
    text = f"""You are a schedule organiser. Time to be scheduled for on weekdays is {timewk}, and {timewknd} on weekends. Students need time to take breaks. Tasks can only be scheduled on days after today's date specified. You will receive the list of tasks that your user has to complete with their completion times in minutes and due dates in YYYY-MM-DD format, as well as an example. Order the tasks based on their importance and length. Output the new list, including the timestamps for each task. Output in CSV format where each task is a new record, and the date, time and name of a task are separate fields. Times are in 24 hour format. Breaks should be formatted as a task with the name "Break". Do not output days with no tasks scheduled. Terminate the list with a | character. Output nothing but the list.

Input: Today: 2024-07-27, Saturday
Study group, 90, 2024-08-03
History project, 50, 2024-07-30
Research paper, 120, 2024-08-03
Coding assignment, 50, 2024-08-03
Quiz preparation, 90, 2024-08-03
Output:  2024-07-27,12:00-12:50,History project
2024-07-27,12:50-13:40,Coding assignment
2024-07-27,13:40-14:00,Break
2024-07-27,14:00-16:00,Research paper
2024-07-28,12:00-13:30,Study group
2024-07-28,13:30-15:00,Quiz preparation|

Input: {tasks}
Output: """
    #print("Prompt: ", text) # debug
    return text
# Create model instance
modelsetup = Model(
    model_id=model,
    params=params,
    credentials=creds,
    project_id=project_id,
    space_id=None)
llm = WatsonxLLM(modelsetup)

def make_schedule(tasks):
    today = date.today().strftime("%Y-%m-%d, %A")

    ftasks = f"Today: {today}\n{tasks}"

    prompt = make_prompt(ftasks)
    sched_raw = llm(prompt)

    schedule = sched_raw[:-1] # cut last character (pipe) out
    return schedule