import streamlit as st
from llm import *
from util import *
import csv
from io import StringIO

st.title("Tasks")

MIN_TASK_H = 70

ntask_name = st.session_state['ntask_name']
ntask_due = st.session_state['ntask_due']
ntask_time = st.session_state['ntask_time']

fntask = f"{ntask_name}, {ntask_time} min, {ntask_due}"
st.text(fntask)

testtask = """Email Campaign, 90, 2024-08-27
Team Check-In, 60, 2024-08-28
Market Research, 120, 2024-08-29
Invoice Processing, 60, 2024-08-30
System Update, 90, 2024-08-31"""
sched_raw = ""
st.text(testtask)
if st.button("Make schedule"):
    with st.spinner("Generating schedule..."):
        sched_raw = make_schedule(testtask)
st.text(sched_raw)

# fake task array to save tokens
tsched = """2024-07-30,17:00-18:30,"Email Campaign"
2024-07-30,18:30-19:00,"Break"
2024-07-30,19:00-20:00,"Team Check-In"
2024-07-31,17:00-19:00,"Market Research"
2024-07-31,19:00-19:30,"Break"
2024-07-31,19:30-21:00,"Invoice Processing"
2024-08-01,17:00-18:30,"System Update\""""

sched_f = StringIO(tsched) # fake
#sched_f = StringIO(sched_raw) # real
reader = csv.reader(sched_f)
sched_arr = []
for row in reader:
    #print(row) # debug
    sched_arr.append(row)

def task_complete(id, mins):
    st.session_state["score"] += mins
    st.toast(f"Task complete! {mins} points added")

for i in range(len(sched_arr)):
    # display date if 
    if (i > 0): # prevent indexOutOfRange
        if (sched_arr[i][0] != sched_arr[i-1][0]): # see if we need to display the date
            st.header(sched_arr[i][0])
    else: # if first element, we know the date wasn't displayed already
        st.header(sched_arr[i][0])
    
    time = rtime2len(sched_arr[i][1]) # get task length for formatting
    # set task block height from time
    item_height = MIN_TASK_H if time <= MIN_TASK_H else time # don't go less than 60 (text doesn't fit otherwise)
    with st.container(border=True, height=item_height):
        task_cols = st.columns(4)
        if sched_arr[i][2] != "Break":
            task_cols[0].write(f"**{sched_arr[i][2]}**")
            task_cols[1].write(sched_arr[i][1])
            task_cols[2].button("Complete task", on_click="task_complete", args=[i, time], key=f"btn_compltask{i}")
            task_cols[3].button("Delete task", key=f"btn_deltask{i}")
        else:
            task_cols[0].write(f"*{sched_arr[i][2]}*")
            task_cols[1].write(f"*{sched_arr[i][1]}*")