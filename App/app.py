import streamlit as st
import pandas as pd
import numpy as np
import joblib


pipe_lr = joblib.load(open('models/emotion_classifier_pipe_lr_03_june_2021.pkl', 'rb'))

def main():
    st.title("Emotion Text Classifier App")
    menu = ["Home", 'Monitor', 'About']

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home": 
        st.subheader(" ")
    
        with st.form(key ='emotion_clf_form'):
            raw_text = st.text_area("Type Here")
            submit_text = st.form_submit_button(label = "Submit ")
        
        if submit_text:
            col1, col2 = st.beta_columns(2)

            with col1:
                st.success("Original Text")
                st.write(raw_text)

                st.success("Prediction")
            
            with col2:
                st.success("Prediction Probability")
    
    elif choice == "Monitor":
        st.subheader("Monitor App")
    
    else:
        st.subheader("About")



if __name__ == '__main__':
    main()