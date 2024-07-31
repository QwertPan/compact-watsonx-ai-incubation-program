import streamlit as st
ConHEIGHT=60
st.title("Rankings")

# init variables
uname = st.session_state["uname"]
score = st.session_state["score"]

data = [["1","2","3","4","5", "6", "7", "8", "9", "10"], ["Alice Johnson", "Bob Smith", "Charlie Brown", "David Wilson", "Emma Davis",
    "Frank Miller", "Grace Lee", "Hannah Taylor", "Ian Martinez", "Jessica Garcia"], ["7020", "6980", "6930", "6900", "6850", "6800", "6740", "6700", "6650", "6600"]]
prof = [["Ranking", "This Week's Minutes", "Total Minutes", "Total Tasks Completed", "Current Streak", "Highest Streak"], ["#153", "10", "1430", "23", "2 days", "32 days"]]
bigCol = st.columns([2, 1])
with bigCol[0]:
    entcol= st.columns(3)
    with entcol[0]:
        st.write("Rank")
    with entcol[1]:
        st.write("Name")
    with entcol[2]:
        st.write("Total Minutes")

    entcol= st.columns(3)
    for i in range(10):
        with st.container(height=ConHEIGHT):
            entcol= st.columns(3)
            with entcol[0]:
                st.write(data[0][i])
                #st.write("wshj")
            with entcol[1]:
                st.write(data[1][i])
            with entcol[2]:
                st.write(data[2][i])
    with st.container(height=ConHEIGHT):
            entcol= st.columns(3)
            with entcol[0]:
                st.write("153")
                #st.write("wshj")
            with entcol[1]:
                st.write(f"{uname} (You)")
            with entcol[2]:
                st.write("10")
with bigCol[1]:
    with st.container(border=True):
        with st.columns(3)[1]:
            st.image("res/shion.png")
            st.write("Shion")
        st.divider()
        for j in range(len(prof[0])):
            st.write(prof[0][j])
            with st.container(border = True):
                st.write(prof[1][j])

with st.container(border=True):
    shopCol = st.columns([4, 1])
    with shopCol[0]:
        st.subheader("Shop")
        st.page_link("pages/shop.py", label="View shop")
        progText = f"{score}/25000 Points - {25000-score} away from goal"
    with shopCol[1]:
        st.image("res/starbucks.png", width = 125)
    bar = st.progress(0, text=progText)
    bar.progress(score/25000, text = progText)

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