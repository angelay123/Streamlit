import streamlit as st

st.sidebar.title("Hello! I'm Angela Madaya,")
st.sidebar.markdown("""
    Explore my journey through the options below.
""")

menu = st.sidebar.radio("Menu", ["Home","Autobiography", "Portfolio"])
if menu == "Home":
    st.markdown("""
        <h2 style="text-align: center; font-size: 32px;font-family: 'Georgia', sans-serif; font-weight: bold;   color: #555;   ">
          Hello! I'm Angela Madaya
        </h2>
        """, unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center;">
            <img src="https://raw.githubusercontent.com/angelay123/picture/main/angela_picture.png" alt="Angela Madaya" style="width: 150px; border-radius: 50%; margin-bottom: 15px;">
            <p style="font-size: 18px; font-family: 'Georgia', sans-serif; color: #555;">
                A passionate Information Technology student at Cebu Institute of Technology - University. 
                Welcome to my personal portfolio where you can explore my projects, skills, and achievements. 
                Use the menu on the left to navigate through my Autobiography and Portfolio sections.
            </p>
        </div>
    """, unsafe_allow_html=True)
elif menu == "Autobiography":
    st.markdown("""
        <h2 style="text-align: center; font-size: 38px;font-family: 'Georgia', sans-serif; font-weight: bold; color: #333;  background-color: #dbf3fa; border-radius: 8px 8px 0 0">
           My Autobiography
        </h2>
        """, unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: justify; font-family: 'Georgia', sans-serif; background-color: #b7e9f7; padding: 15px; border-radius: 0 0 8px 8px;">
        <p style="font-size: 16px; color: #333;">
            I am Angela Madaya, born on September 19, 2000, in the small yet vibrant community of Lutopan, Toledo City. I am the youngest among the four siblings. Growing up in Lutopan, I was surrounded by the simplicity and warmth of provincial life, where everyone knew each other, and the sense of community was strong. My childhood was filled with the joy of playing outside with friends, exploring nature, and the comforting familiarity of a close-knit neighborhood.
            <br><br>
                From an early age, I had a natural curiosity and a strong desire to learn. My parents always encouraged me to pursue my dreams, no matter how big or small they seemed. This support played a crucial role in shaping my academic journey. 
            <br><br>
            I began my formal education at General P. Del Rosario Elementary School, where my foundational years were marked by a love for learning and discovery. My high school years were spent at De La Salle Andres Soriano Memorial College, a period where I developed a keen interest in various subjects and began to explore my academic strengths. In Senior High, I attended Cebu Institute of Technology - University, where I chose the STEM strand, further igniting my passion for technology and science. This experience solidified my decision to pursue a career in Information Technology.
            <br><br>
            I am currently continuing my education at Cebu Institute of Technology - University, where I am working towards my Bachelor of Science in Information Technology. My time at university has been both challenging and rewarding, allowing me to delve deeper into the world of technology and develop skills that will be invaluable in my future career.            
            <br><br>
            In addition to my academic pursuits, I have a variety of interests and hobbies that I enjoy in my free time. I have a deep appreciation for music and enjoy listening to a wide range of genres, which often serves as a source of inspiration and relaxation. Additionally, I am an avid reader of comics, finding pleasure in the rich storytelling and diverse art styles they offer. 
            <br><br>
            I also have a keen interest in Korean dramas and anime. Both of these forms of entertainment provide me with a delightful escape and a way to explore different cultures and storytelling techniques. Whether it’s the intricate plots of Korean dramas or the imaginative worlds of anime, these hobbies bring a lot of enjoyment and excitement to my life.
            <br><br>
            As I look back on my journey so far, I am grateful for the experiences that have shaped who I am today. My early life in Lutopan, my educational path, and my diverse interests have all contributed to my growth and development. With each step I take, I am more excited about the future and the opportunities it holds.
            <br><br>
            I am determined to continue pursuing my passions and making the most of every opportunity that comes my way. The knowledge and skills I have gained will guide me as I navigate my career in Information Technology and beyond. I look forward to contributing to the field and making a positive impact on the world. Thank you for taking the time to learn about my story.
        </p>
    </div>
    <br>
    """, unsafe_allow_html=True)


elif menu == "Portfolio":
        # Title of the Portfolio
    # Display the image from Google Drive
    st.markdown("""
        <h2 style="text-align: center; font-size: 38px;font-family: 'Georgia', sans-serif; font-weight: bold; color: #333;background-color: #dbf3fa;border-radius: 8px; ">
           My Portfolio
        </h2>
        <br>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style="display: flex; align-items: center; background-color: #b7e9f7; padding: 15px; border-radius: 8px;">
            <div style="flex: 0 0 auto; margin-right: 15px;">
                <img src="https://raw.githubusercontent.com/angelay123/picture/main/angela_picture.png" alt="Angela Madaya" style="width: 120px; border-radius: 50%;">
            </div>
            <div style="flex: 1; text-align: justify; font-family: 'Georgia', sans-serif;">
                <p style="font-size: 16px; color: #333; marginTop:12px">
                    Hello! I am Angela Madaya, currently pursuing a Bachelor of Science in Information Technology at Cebu Institute of Technology - University. This portfolio showcases my work, skills, and projects. Feel free to explore and learn more about what I have been working on.
                </p>
            </div>
        </div>
            <br>
        """, unsafe_allow_html=True)
    st.markdown("""
    <h2 style="text-align: left; font-size: 28px;font-family: 'Georgia', sans-serif;background-color: #dbf3fa; font-weight: bold; color: #333;padding:5px;border-radius:8px 8px 0 0">
        Skills
    </h2>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: justify; font-family: 'Georgia', sans-serif; background-color: #b7e9f7; padding: 15px;border-radius:0 0 8px 8px">
            <p style="font-size: 16px; color: #333;">
            I possess a range of skills related to Information Technology and beyond. Some of my key skills include:
            <ul style="font-size: 16px; color: #333; ">
                <li>Programming Languages: Python, JavaScript, Java, C++</li>
                <li>Web Development: HTML, CSS, JavaScript, React</li>
                <li>Data Analysis: Pandas, NumPy, Matplotlib</li>
                <li>Database Management: MySQL, MariaDB</li>
                <li>API Development: Postman</li>
                <li>Software Development: Agile methodologies, Version Control (Git), Spring Boot</li>
                <li>Problem Solving: Analytical and logical thinking, debugging</li>
            </ul>
            </p>
        </div>
            <br>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <h2 style="text-align: left; font-size: 28px;font-family: 'Georgia', sans-serif; background-color: #dbf3fa; font-weight: bold; color: #333;padding:5px; border-radius:8px 8px 0 0">
        Certifications
    </h2>
    """, unsafe_allow_html=True)
    st.markdown("""
         <div style="text-align: justify; font-family: 'Georgia', sans-serif; background-color: #b7e9f7; padding: 15px; border-radius:0 0  8px 8px">
            <p style="font-size: 16px; color: #333;">
            I have completed the following certifications and training programs:
            <ul style="font-size: 16px; color: #333; ">
                <li><strong>Data Analytics - Introduction to Machine Learning Certification:</strong> Allison</li>
                <li><strong>Fundamentals Google Analytics 4 Certification:</strong> Allison</li>
            </ul>
            </p>
        </div>
                <br>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <h2 style="text-align: left; font-size: 28px;font-family: 'Georgia', sans-serif; font-weight: bold; background-color: #dbf3fa; font-weight: bold; color: #333;padding:5px;border-radius:8px 8px 0 0">
        Projects
    </h2>
    """, unsafe_allow_html=True)
    st.markdown("""
      <div style="text-align: justify;background-color: #b7e9f7; padding: 15px;color:#333;font-family: 'Georgia', sans-serif; border-radius:0 0  8px 8px">
            Here are some of the projects I have worked on:
            <ul style="font-size: 20px; color: #333; ">
                <li><strong>Capstone Project: E-AEPA System</strong>
                    <p style="font-size: 15px; color: #333; background-color:#92dff3; padding: 5px 10px 10px 10px; margin-top: 2px;border-radius:8px">
                        The E-AEPA System is a comprehensive software solution developed as part of our capstone project. Its purpose is to automate and streamline the employee performance evaluation process at CIT-U, transitioning from manual, Excel-based methods to an integrated digital platform. 
                        <br>
                        This system is designed to enhance efficiency, accuracy, and transparency in evaluating employee performance. It includes features such as secure user authentication, employee profile management, customizable evaluation workflows, a 360-degree feedback appraisal system, and detailed reporting and analytics. The system aims to empower HR personnel to make informed decisions regarding employee development, retention, and overall workforce optimization.
                        <br>
                        <strong>Technologies Used:</strong> Spring Boot, Vite, MySQL, Postman
                        <br>
                        <strong>GitHub Repository:</strong> https://github.com/surigaoadrian/E-AEPA-System
                    </p>
                </li>
                <li><strong>Project: Pawscare</strong>
                    <p style="font-size: 15px; color: #333; background-color:#92dff3; padding: 5px 10px 10px 10px; margin-top: 2px;border-radius:8px">
                        Pawscare is a comprehensive platform developed for managing pet-related services. This project, part of our Object-Oriented Programming (OOP) subject, includes features for pet adoption, online shopping for pet supplies, and scheduling appointments for grooming and veterinary care. The goal of Pawscare is to streamline pet care processes and provide a user-friendly interface for pet owners to manage their pets' needs efficiently.
                        <br>
                        <strong>Technologies Used:</strong> Java, MariaDB
                    </p>
                </li>
                <li><strong>Project: TeachManage</strong>
                    <p style="font-size: 15px; color: #333; background-color:#92dff3;  padding: 5px 10px 10px 10px; margin-top: 2px;border-radius:8px">
                        TeachManage is a comprehensive resource management and collaboration platform designed specifically for educators. This project is part of our Application Development subject and aims to streamline the way teachers manage educational resources and collaborate effectively.
                        <br>
                        With features such as subject folder management and real-time collaboration on worksheets, TeachManage simplifies the complexities of resource management in education. It empowers educators to efficiently organize their materials, collaborate seamlessly with colleagues, and innovate in their teaching methods.
                        <br>
                        <strong>Technologies Used:</strong> React, Spring Boot, MySQL, Postman
                        <br>
                        <strong>GitHub Repository:</strong> https://github.com/annejenel/TeachManage
                    </p>
                </li>
            </ul>
          
        </div>
                <br>
        
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <h2 style="text-align: left; font-size: 28px; font-family: 'Georgia', sans-serif; font-weight: bold;  background-color: #dbf3fa; font-weight: bold; color: #333;padding:5px;border-radius:8px 8px 0 0">
        Education
    </h2>
    """, unsafe_allow_html=True)
    st.markdown("""
       <div style="text-align: justify; font-family: 'Georgia', sans-serif; background-color: #b7e9f7; padding: 15px; border-radius:0 0  8px 8px ">
            <p style="font-size: 16px; color: #333;">
            I am currently pursuing a Bachelor of Science in Information Technology at Cebu Institute of Technology - University. My academic background includes:
            <ul style="font-size: 16px; color: #333;">
                <li><strong>Elementary:</strong> General P. Del Rosario Elementary School</li>
                <li><strong>High School:</strong> De La Salle Andres Soriano Memorial College</li>
                <li><strong>Senior High School:</strong> Cebu Institute of Technology - University </li>
                <li><strong>College:</strong> Cebu Institute of Technology - University</li>
            </ul>
        </div>
            <br>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <h2 style="text-align: left; font-size: 28px;font-family: 'Georgia', sans-serif; font-weight: bold;  background-color: #dbf3fa; font-weight: bold; color: #333;padding:5px;border-radius:8px 8px 0 0">
        Contact
    </h2>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: justify; font-family: 'Georgia', sans-serif; background-color: #b7e9f7; padding: 15px; border-radius: 0 0 8px 8px;">
            <p style="font-size: 16px; color: #333;">
            Feel free to reach out to me through the following channels:
            <ul style="font-size: 16px; color: #333;">
                <li><strong>Email:</strong> angelamadaya919@gmail.com</li>
                <li><strong>GitHub:</strong> https://github.com/angelay123</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

