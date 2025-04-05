import streamlit as st
import pickle
import pythoncom
from sklearn.metrics import accuracy_score, precision_score


def about_section():
    st.subheader("About Email Spam Classification App")
    st.write("Welcome to the Email Spam Classification App!")
    st.write("This application uses machine learning to classify emails as spam or not spam.")
    st.write("Feel free to explore the classification feature and provide feedback to help us improve.")
    st.write("Your input is valuable!")

def footer():
    st.write("\n\n\n\n")
    st.write("\n\n © 2024 by Tejkumar Nelluri. All rights reserved.")

def main():
    pythoncom.CoInitialize()
    try:
        st.title("Email Spam Classification Application")

        # Sidebar navigation
        st.sidebar.subheader("Navigation")
        classification_clicked = st.sidebar.button("Classification")
        st.sidebar.write("")
        about_clicked = st.sidebar.button("About")

        if classification_clicked or not about_clicked:
            st.subheader("Classification")
            msg = st.text_input("Enter the text that you received/ the text that you want to check")

            if st.button("Process") and msg:
                data = [msg]
                vect = cv.transform(data).toarray()
                result = model.predict(vect)
                if result[0] == 0:
                    st.success("This is Not A Spam Email")
                else:
                    st.success("This is A spam Email)

            # Accuracy check using pre-saved test data
            if st.button("Accuracy"):
                X_test_vect = pickle.load(open('X_test_vect.pkl', 'rb'))
                y_test = pickle.load(open('y_test.pkl', 'rb'))
                y_pred = model.predict(X_test_vect)
                accuracy = accuracy_score(y_test, y_pred)
                st.write(f"Model Accuracy: {accuracy:.4f}")

            # Precision check using pre-saved test data
            if st.button("Precision"):
                X_test_vect = pickle.load(open('X_test_vect.pkl', 'rb'))
                y_test = pickle.load(open('y_test.pkl', 'rb'))
                y_pred = model.predict(X_test_vect)
                precision = precision_score(y_test, y_pred)
                st.write(f"Model Precision: {precision:.4f}")

            # Feedback link
            st.markdown("""
                <div style="text-align: center; margin-top: 40px; font-size: 18px;">
                    Click 👉 <a href="https://forms.gle/BEDVaaXSxzHgDz3t6" style="color: #3366ff; text-decoration: underline;">here</a> to give feedback if we mistakenly gave a wrong classification.
                </div>
            """, unsafe_allow_html=True)

        elif about_clicked:
            about_section()

        footer()

    finally:
        pythoncom.CoUninitialize()

# Load model and vectorizer once at startup
model = pickle.load(open('spam.pkl', 'rb'))
cv = pickle.load(open('vectorizer.pkl', 'rb'))

if __name__ == "__main__":
    main()
