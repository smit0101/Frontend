import base64
import streamlit as st
from PIL import Image
import numpy as np


def bg():
    # side_bg_ext = 'gif'
    file_ = open(r"FrontEnd/gif/Final_hompage2.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(
        f"""
      <style>
      [class="stApp css-ffhzg2 eczokvf1"] {{
            background: url(data:image/gif;base64,{data_url});
            background-size: cover;
      }}
      [data-testid="stHeader"]{{
        background-color: rgba(0,0,0,0);
      
      }}
      </style>
      """,
        unsafe_allow_html=True,
    )


# background audio for the home page.
def autoplay_audio():
    with open(r"FrontEnd/Sound/motivational-day-112790.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay class="stAudio" loop="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )


def main():
    bg()
    autoplay_audio()
    st.title("About US")
    st.text("Cyber-safety project")
    st.text(""" 
Readable text is an important type of internet content, such as web pages, job posts, tweets, 
Facebook posts, and product details. Text-based content can be collected from many sources and used to extract 
insight for many purposes. Recommended jobs based on a saved search, scam detection from online product posts, 
and email filtering are some examples of Natural Language Processing (NLP) and Machine Learning (ML) 
applications. This project will use Cyberbullying Tweets Dataset from Kaggle.com to build machine-learning models 
for cyberbullying classification. Selecting a machine-learning model will be stored on the public cloud and used 
by serverless technology once the provided API has been called. The result will return to the requester in JSON 
format, providing the classification result based on providing text. A front-end application will be created for 
API calls, and Postman will be used for testing purposes. """)

    st.header("Group Members")

    praba = Image.open(r'FrontEnd/Images/Pirabanjan.jpg')
    api = Image.open(r'FrontEnd/Images/api.jpeg')
    dhar = Image.open(r'FrontEnd/Images/Dhar.jpeg')
    sarah = Image.open(r'FrontEnd/Images/Sarah.jpeg')
    kiranvir = Image.open(r'FrontEnd/Images/kiranvir.jpeg')

    with st.expander("Apinya T"):
        st.image(api)
        st.write('Apinya: [LinkedIn](https://www.linkedin.com/in/apinya-t/)')
        st.text(""" 
Through 17 years of experience in various industries, I have been serving company and customer 
businesses with maximized IT values through people, processes, operations, and technology improvement. 
With a growth mindset, willingness to collaborate, and keeping continuous improvement in mind, 
I believe I will deliver the best products and services to your clients and company.My 5-year plan is to move 
into a higher position, taking more responsibilities, or even move to other areas such as SRE or Solution 
Architect. However, I will not just wait for 5 years. Instead, I will continue improving myself, so I am ready 
to take it once the opportunities come to me.
        
Latest Position Senior: 
        Service Delivery Manager 
        Latest Job Function: DevOps
        Experienced Industries: Banking, Consulting, Digital/Tech Companies, Software Development, 
        IT Professional Services, Telecommunication, and Mobile Content Provider 
        """)

    with st.expander("Pirabanjan K"):
        st.image(praba)
        st.write('Pirabanjan: [LinkedIn](https://www.linkedin.com/in/pirabanjan-kirupaharan/)')
        st.text(""" 
I am a focused, self-motivated, adaptable, and hardworking graduate student who has the passion and 
dedication to seek a challenging position, where I could utilize my skills and knowledge to serve the 
organization while grooming as a successful IT professional. And I’m a fluent communicator with strong 
investigation, problem-solving, and decision-making skills, combined with a pragmatic approach. 
I have worked at Pearson for 3 years as a Site Reliability Engineer. I always like to learn new technologies 
and experience new challenging environments so decided to move to Canada for postgraduate studies 
I am currently following DevOps for Cloud Computing PGDip at Lambton College and 
I am working as an infrastructure engineer in 4S Consulting Services Inc. 
I have completed certifications like RHCSA and RHCE and currently looking forward to completing certification 
in AWS, Kubernetes, and Terraform. 
        """)

    with st.expander("Sarah "):
        st.image(sarah)
        st.write('Sarah: [LinkedIn](https://www.linkedin.com/in/sarahlebautista/?originalSubdomain=ca)')
        st.text("""
I am currently a student at Lambton College taking up a post-graduate course to upgrade my skillsets and to equip myself 
for a more challenging role that I may be in the future. I am an IT professional with experience in Project and Delivery 
support in the IT industry focusing on Enterprise Resource Planning (ERP) application services and deployment running 
on cloud platforms. 

While incident management and service requests are challenging yet enjoyable tasks as they developed my profound 
skills in troubleshooting, however, going beyond what my role entails gave me an opportunity to explore and learn the 
application installations and upgrades. It led me to a new role where I manage thorough application deployment and 
attend to urgent release updates required by the client that supports their business to operate efficiently and meet 
their goals. I strongly believe that understanding and aligning the client’s needs and expectations could lead to a 
healthy customer relationship. 

In my 8 years of experience in the IT industry, I have administered ERP systems in the AWS cloud platform, 
running on Windows 2012 Server R2 and using Microsoft SQL and Oracle databases for 5 years. I have Implemented 127 
release upgrades for different accounts and types of environments for the past two years of employment, provisioned 
Level 3/Level 4 support to troubleshoot complex problems, and provide diagnosis and resolution to operational issues. 
I have created ten technical documentation guides for process improvement and held new hire onboarding technical 
training from basic to core processes. I also provided on-call support during off-hours work and deployed emergency 
releases. Lastly, I got certified by ITIL Foundation in IT Service Management.
        """)

    with st.expander("Dharsana B"):
        st.image(dhar)
        st.write('Dharsana: [LinkedIn](https://www.linkedin.com/in/dharsana-bala-72b827224/)')
        st.text(""" 
Dharsana is a computer science graduate. Have worked extensively on "Secure file transfer over the 
cloud" and published across different forums. Currently pursuing Post graduate diploma at Lambton College, Toronto. 
I’m now thriving in the cloud and containers, discovering features and technologies to reach high availability, 
scalability and security of systems in an automated way. 
        """)

    with st.expander("Kiranvir "):
        st.image(kiranvir)
        st.write('KIRANVEER KAUR: [LinkedIn](https://www.linkedin.com/in/kiranveer-kaur-1a08a1249/)')
        st.text("""
2 Years of IT experience as a software analyst encompassing a wide range of skill sets, roles, 
and industry verticals. Firm knowledge of different phases of software testing and software development life 
cycle (SDLC) Including Agile Methodology and waterfall. I am a motivated software analyst to contribute my 
knowledge and skills to the organization and enhances my experience through continuous learning and teamwork. 
I am seeking to obtain a part-time position as a software analyst, where I can apply technical and analytical 
skills to challenging problems and assist your company to meet its goals. 
        """)


if __name__ == '__main__':
    main()
