import base64
import streamlit as st
import time
import requests
import json
import requests
from streamlit_lottie import st_lottie_spinner

from nltk.tokenize import sent_tokenize


# API request.
def fetch(url, obj):
    try:
        result = requests.post(url, json=obj)
        return result.json()
    except Exception:
        return {}


# Background Gif of the application


# background audio for the home page.



def sentence_break(data):
    token_text = sent_tokenize(data)
    for s in token_text:
        url = 'https://z0ml9n8tn8.execute-api.us-east-1.amazonaws.com/cyberbullyingpredict'
        myobj = {'text': s}
        x = fetch(url, myobj)
        st.text(s)
        st.text(x)


def main():
    st.set_page_config(
        page_title="Cyber-safety",
        page_icon="🤖",
        # layout="wide"
    )

    tab1, tab2, tab3 = st.tabs(["Home", "Single-text", "Multi-text"])

    
    # st.sidebar.success("Select a page above")
    with tab1:
        st.title("Welcome to Cyber-safety")
        with st.expander("What is cyberbullying?"):
            st.text("""
            Cyberbullying is using computers, smartphones or other connected devices to embarrass, hurt, 
            mock, threaten or be mean to someone online. It is a serious issue that we can stop. """)
        with st.expander("What are some common myths about bullying?"):
            st.text("""
            Myth #1 – “Children have got to learn to stand up for themselves.” Reality – Children who get 
            up the courage to complain about being bullied are saying they’ve tried and can’t cope with the situation 
            on their own. Treat their complaints as a call for help. In addition to offering support, 
            it can be helpful to provide children with problem solving and assertiveness training to assist them in 
            dealing with difficult situations. 
            
            Myth #2 – “Children should hit back – only harder.” Reality – This 
            could cause serious harm. People who bully are often bigger and more powerful than their victims. This 
            also gives children the idea that violence is a legitimate way to solve problems. Children learn how to 
            bully by watching adults use their power for aggression. Adults have the opportunity to set a good 
            example by teaching children how to solve problems by using their power in appropriate ways. 
            
            Myth #3 – 
            “It builds character.” Reality – Children who are bullied repeatedly, have low self-esteem and do not 
            trust others. Bullying damages a person’s self-concept. 
            
            Myth #4 – “Sticks and stones can break your bones 
            but words can never hurt you.” Reality – Scars left by name-calling can last a lifetime. 
            
            Myth #5 – 
            “That’s not bullying. They’re just teasing.”Reality – Vicious taunting hurts and should be stopped. 
            
            Myth #6 – 
            “There have always been bullies and there always will be.” Reality – By working together as parents, 
            teachers and students we have the power to change things and create a better future for our children. As 
            a leading expert, Shelley Hymel, says, “It takes a whole nation to change a culture”. Let’s work together 
            to change attitudes about bullying. After all, bullying is not a discipline issue – it is a teaching 
            moment. 
            
            Myth #7 – “Kids will be kids.”Reality – Bullying is a learned behaviour. Children may be 
            imitating aggressive behaviour they have seen on television, in movies or at home. Research shows that 
            93% of video games reward violent behaviour. Additional findings show that 25% of boys aged 12 to 17 
            regularly visit gore and hate internet sites, but that media literacy classes decreased the boys’ viewing 
            of violence, as well as their acts of violence in the playground. It is important for adults to discuss 
            violence in the media with youth, so they can learn how to keep it in context. There is a need to focus 
            on changing attitudes toward violence. 
            Source: Government of Alberta""")
    with tab2:
        # st.session_state.sidebar_state = 'expanded'
        session = requests.Session()
        with st.form("my_form"):
            # index = st.number_input("ID", min_value=0, max_value=100, key="index")
            index = st.text_input("Input a text")

            submitted = st.form_submit_button("Submit")

            if submitted:
                my_bar = st.progress(0)
                for percent_complete in range(10):
                    time.sleep(0.1)
                    my_bar.progress(percent_complete + 1)
                # st.write("Result")
                url = 'https://z0ml9n8tn8.execute-api.us-east-1.amazonaws.com/cyberbullyingpredict'
                myobj = {'text': index}
                x = fetch(url, myobj)
                if x:
                    st.text(x)
                else:
                    st.error("Error")

    with tab3:
        # text
        with st.expander("Insert text file"):
            index1 = st.write("insert txt files.")
            # submitted1 = st.form_submit_button("Upload")
            file_uploader = st.file_uploader(label="Upload a file")
            hide_label = """
            <style>
                .css-9ycgxx {
                    display: none;
                }
            </style>
            """
            st.markdown(hide_label, unsafe_allow_html=True)
            if file_uploader:
                st.write("filename", file_uploader.name)
                byte_data = file_uploader.read().decode('utf-8')
                for percent_complete in range(10):
                    time.sleep(0.1)
                    my_bar.progress(percent_complete + 1)
                sentence_break(byte_data)

            else:
                st.text("Upload the file please")
            st.write("""
                Insert the files to analyze multiple text each sentences is breakdown and analyzed if the 
                content has a cyber-bullying text or not.
            """)


if __name__ == '__main__':
    main()
