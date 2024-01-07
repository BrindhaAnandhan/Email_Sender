from email.message import EmailMessage
import ssl
import smtplib
email_sender= 'brindhaorbindu@gmail.com'
email_password= 'XXXXXXXXXXXX'

email_receiver='XXXXXXXXXXXXXX'
subject= "Request for interview - Python Developer "
body= '''
Dear Manager:\n
I hope this email finds you well. My name is Brindha, and I am writing to express my interest in the Python Developer 
position at your company. With my strong background in Python programming and experience in developing efficient and 
scalable software solutions, I believe I would be a valuable asset to your team.\n

I have been following the impressive growth and innovative projects undertaken by [Company Name], and I am particularly 
drawn to the company's commitment to leveraging cutting-edge technologies. As an experienced Python Developer, I have 
successfully delivered numerous projects and developed robust applications in Python, both independently and as part of
 cross-functional teams.\n

My qualifications include:\n

Proficiency in Python programming language, along with expertise in popular frameworks such as Django and Flask.
Strong knowledge of object-oriented programming (OOP) principles and design patterns.
Experience in developing RESTful APIs and integrating third-party services.
Solid understanding of database management systems, including SQL and ORM frameworks like SQLAlchemy.
Familiarity with version control systems, particularly Git, and collaborative development using platforms like GitHub or
Bitbucket. Ability to write clean, maintainable, and testable code, adhering to coding standards and best practices.
Problem-solving mindset and the capacity to analyze complex technical challenges and propose effective solutions.
Excellent communication skills and the ability to collaborate effectively with team members and stakeholders.
I am confident that my skills and experience align well with the requirements of the Python Developer position at XXX.
I would be honored to have the opportunity to discuss further how my contributions can benefit the company and 
contribute to its ongoing success.\n
I kindly request an interview to discuss the Python Developer position in detail and provide more information about my 
background and accomplishments. I am available at your convenience and can be reached via email at 
btindhaanand1409@gmail.com or by phone at 9790156818.\n

Thank you for considering my application. I look forward to the opportunity to speak with you and showcase my 
capabilities as a Python Developer.\n

Sincerely,\n
Brindha A
'''
em= EmailMessage()
em['From']= email_sender
em["To"]= email_receiver
em["subject"]= subject
em.set_content(body)

context= ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context ) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())