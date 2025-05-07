import streamlit as st
import time
import random

class TypingSpeedTracker:
    def __init__(self):
        self.sentence = self.generate_sentence()
        self.start_time = None
        self.typed = ""
        self.submitted = False

    # To generate a random sentence from a predefined list of sentences
    def generate_sentence(self):
        sentences = [
            "Python is a powerful programming language.",
            "Streamlit makes building apps very simple.",
            "Typing fast improves your coding ability.",
            "Machine learning is a part of AI.",
            "Web development is fun and creative.",
            "Consistent practice improves typing speed.",
            "Debugging is a key part of programming.",
            "Always write clean and readable code."
        ]
        return random.choice(sentences)

    # Calculate accuracy
    def calculate_accuracy(self, original, typed):
        correct_chars = sum(1 for o, t in zip(original, typed) if o == t)
        return (correct_chars / len(original)) * 100

    # Calculate word per minute (WPM)
    def calculate_wpm(self, typed_text, time_seconds):
        words = typed_text.split()
        return (len(words) / time_seconds) * 60

    # Streamlit UI
    def run(self):
        st.set_page_config(page_title="Typing Speed Tracker", layout="centered")
        st.title("💬 Typing Speed Tracker")

        # Session state initialization
        if 'tracker' not in st.session_state:
            st.session_state.tracker = TypingSpeedTracker()

        tracker = st.session_state.tracker

        # User input for name and print the message
        name = st.text_input("👤 Enter your name:")

        if name:
            st.write(f"👋 Hello, **{name}**! Type the following sentence:")
            st.info(tracker.sentence)

            # Start typing timer
            if tracker.start_time is None:
                if st.button("🟢 Start Typing"):
                    tracker.start_time = time.time()
                    tracker.submitted = False
                    tracker.typed = ""
            else:
                typed = st.text_area("✍️ Type here:", height=150)
                tracker.typed = typed

                # Submit button to check the typing speed and accuracy
                if st.button("📤 Submit"):
                    if typed.strip() == "":
                        st.warning("Please type something before submitting.")
                    else:
                        end_time = time.time()
                        total_time = max(end_time - tracker.start_time, 1)

                        accuracy = tracker.calculate_accuracy(tracker.sentence, typed)
                        wpm = tracker.calculate_wpm(typed, total_time)

                        tracker.submitted = True

                        st.session_state.tracker = tracker

                        st.success(f"⏱️ Time Taken: {total_time:.2f} seconds")
                        st.success(f"✅ Accuracy: {accuracy:.2f}%")
                        st.success(f"⚡ Speed: {wpm:.2f} WPM")

                        if accuracy == 100:
                            st.balloons()
                            st.info("🎯 Perfect typing! Well done!")
                        elif accuracy >= 80:
                            st.info("💪 Great job! You're almost perfect.")
                        else:
                            st.warning("🧑‍💻 Keep practicing. You'll get better!")

            # Try again button
            if tracker.submitted:
                if st.button("🔁 Try Again", key="try_again"):
                    st.session_state.tracker = TypingSpeedTracker()
                    st.rerun()


# Run the app
TypingSpeedTracker().run()
