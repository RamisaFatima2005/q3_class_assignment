import streamlit as st

# User Class
class User:
    def __init__(self, username, password, is_tutor=False):
        self.username = username
        self.password = password
        self.is_tutor = is_tutor
        self.wallet = 10.0

# Session Class
class Session:
    def __init__(self, student, tutor, topic):
        self.student = student
        self.tutor = tutor
        self.topic = topic
        self.price = 2.0

# Payment Class
class Payment:
    @staticmethod
    def process(user, amount):
        if user.wallet >= amount:
            user.wallet -= amount
            return True, "✅ Payment successful"
        else:
            return False, "❌ Insufficient balance"

# In-memory database (dictionary)
if "users" not in st.session_state:
    st.session_state.users = {}

if "current_user" not in st.session_state:
    st.session_state.current_user = None

if "login_success" not in st.session_state:
    st.session_state.login_success = False

# Signup Function
def signup():
    st.subheader("🔐 Sign Up")
    username = st.text_input("Choose a username", key="signup_user")
    password = st.text_input("Choose a password", type="password", key="signup_pass")
    is_tutor = st.checkbox("Are you a tutor?", key="signup_check")
    if st.button("Sign Up"):
        if username in st.session_state.users:
            st.error("Username already exists!")
        else:
            st.session_state.users[username] = User(username, password, is_tutor)
            st.success("Account created! Now login.")

# Login Function
def login():
    st.subheader("🔓 Log In")
    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")
    if st.button("Login"):
        user = st.session_state.users.get(username)
        if user and user.password == password:
            st.session_state.current_user = user
            st.session_state.login_success = True
        else:
            st.error("Invalid credentials")

# Dashboard Function
def dashboard():
    user = st.session_state.current_user
    st.subheader(f"📋 Dashboard for {user.username}")
    st.info(f"💰 Wallet Balance: ${user.wallet}")

    if user.is_tutor:
        st.success("You are registered as a Tutor.")
    else:
        st.subheader("📚 Book a Tutoring Session")
        tutor_list = [u.username for u in st.session_state.users.values() if u.is_tutor]
        if not tutor_list:
            st.warning("No tutors available.")
            return
        selected_tutor = st.selectbox("Choose a Tutor", tutor_list)
        topic = st.text_input("Topic you need help with")

        if st.button("Book Session"):
            tutor = st.session_state.users[selected_tutor]
            session = Session(user, tutor, topic)
            paid, message = Payment.process(user, session.price)
            if paid:
                st.success(f"Session booked with {tutor.username} on '{topic}'")
                st.info(message)
            else:
                st.error(message)

    # Logout button
    if st.button("🚪 Logout"):
        st.session_state.current_user = None
        st.session_state.login_success = False

# Main App Logic

st.title("🎓 EduBridge App")

# Handle login success and rerun manually
if st.session_state.login_success:
    st.session_state.login_success = False

if st.session_state.current_user is None:
    menu = ["Login", "Sign Up"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Login":
        login()
    else:
        signup()
else:
    dashboard()
