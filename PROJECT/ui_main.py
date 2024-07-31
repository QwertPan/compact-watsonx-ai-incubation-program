import streamlit as st
from datetime import date

st.set_page_config(layout="centered")
st.title("Dashboard")

# init variables
if "score" not in st.session_state:
    st.session_state["score"] = 0
    st.session_state["uname"] = "Shion"
score = st.session_state["score"]
uname = st.session_state["uname"]


# New task
task_container = st.form("ntask_form", border=True)
task_container.header("New task")
task_input_cols = task_container.columns(4)
with task_input_cols[0]:
    st.text_input(label="Name", placeholder="Name", key="wntask_name",)
with task_input_cols[1]:
    st.date_input(label="Due", format="YYYY-MM-DD", min_value=date.today(),key="wntask_due")
with task_input_cols[2]:
    st.number_input(label="Duration (minutes)", min_value=10, max_value=240, step=10, key="wntask_time")
with task_input_cols[3]:
    st.write("") # spacer
    st.write("") # spacer
    if st.form_submit_button("Add", type="primary"):
        st.session_state["ntask_name"] = st.session_state["wntask_name"]
        st.session_state["ntask_due"] = st.session_state["wntask_due"]
        st.session_state["ntask_time"] = st.session_state["wntask_time"]
        st.switch_page("pages/tasks.py")

# Bottom row
misc_cols = st.columns(3)
with misc_cols[0]:
    with st.container(border=True, height=300): # sched box
        st.header("Today")
        st.page_link("pages/tasks.py", label="View all")
        st.image("res/upcoming.png")
with misc_cols[1]:
    with st.container(border=True, height=300): # streak box
        st.header("Rewards")
        st.page_link("pages/rewards.py", label="View all")
        with st.container():
            st.image("res/streak.png")
with misc_cols[2]:
    with st.container(border=True, height=300): # account box
        st.header("Profile")
        st.page_link("pages/profile.py", label="View all")
        st.markdown(f"#### **{score}💰**")
        with st.container(border=True, height=100): # account info box
            acc_cols = st.columns(2)
            with acc_cols[0]:
                st.image("res/shion.png")
            with acc_cols[1]:
                st.markdown(f"#### **{uname}**")

# Sidebar
with st.sidebar:
    st.title("Nexus AI")
    st.page_link("ui_main.py", label="Dashboard", icon=":material/dashboard:")
    st.page_link("pages/tasks.py", label="Day Planner", icon=":material/calendar_month:")
    st.page_link("pages/rewards.py", label="Leaderboard", icon=":material/leaderboard:")
    st.page_link("pages/shop.py", label="Shop", icon=":material/storefront:")
    for i in range(12):
        st.write("")
    st.page_link("pages/profile.py", label="Profile", icon=":material/account_circle:")
    st.page_link("pages/dummy.py", label="Log out", icon=":material/logout:")