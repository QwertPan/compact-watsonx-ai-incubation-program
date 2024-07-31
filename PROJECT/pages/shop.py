import streamlit as st
st.title("Rewards Shop")
shoCol = st.columns(4)
for i in range(4):
    with shoCol[i]:
        st.image("res/starbucks.png")
        st.image("res/starbucks.png")
        st.image("res/starbucks.png")


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