system_prompt = """ 
Extract the following sections from the given {resume} and present them in proper JSON format:
1. Personal Information (Name, Address, Email)
2. Education (Degrees, Institutions, Dates, CGPA)
3. Skills
4. Experience (Job Titles, Companies, Dates, Responsibilities)
5. Projects (Title, Description, Technologies Used, Links)
6. Achievements
7. Certifications
8. Personal Details (Languages, Nationality, Hobbies and Interests)

Example JSON structure:
{
"personal_information": {
"name": "Anjani Thanmayee Chandaluri",
"address": "Narasaraopet, Andhra Pradesh, India 522601",
"email": "anjanithanmayee4@gmail.com"
},
"education": [
{
"institution": "Narasaraopeta Engineering College, Guntur, Andhra Pradesh",
"degree": "B.Tech - Computer Science And Engineering",
"dates": "2020-2024",
"cgpa": "8.6"
},
{
"institution": "Jupiter Junior College, Guntur, Andhra Pradesh",
"degree": "Intermediate, Mpc",
"dates": "2018-2020",
"cgpa": "9.29"
},
{
"institution": "Bhashyam High School, Guntur, Andhra Pradesh",
"degree": "Secondary School Of Certificate",
"dates": "2017-2018",
"cgpa": "9.5"
}
],
"skills": [
"Python",
"HTML",
"CSS",
"Bootstrap",
"JavaScript",
"React Js",
"Node Js",
"Express Js",
"SQL",
"Data Structures",
"Algorithms"
],
"experience": [
{
"job_title": "Software Development Intern",
"company": "StepOut",
"dates": "Nov 2023 - Jan 2024",
"responsibilities": [
"Contributed to React.js and React Native projects",
"Worked on bug resolution",
"Integrated Freshchat/Freshdesk",
"Developed diverse screens—demonstrating proficiency in enhancing app and website functionality."
]
}
],
"projects": [
{
"title": "Food Munch",
"description": "Developed a responsive website for Food Store",
"technologies": "HTML, CSS, Bootstrap",
"link": "http://atfoodmunch.ccbp.tech/"
},
{
"title": "E-Commerce Website",
"description": "Developed an Online Management system which implemented Routing Authentication and displays a list of products and implemented features like add to cart, sort, filter, search products. Valid credentials are USERNAME:raja, PASSWORD:raja@2021",
"technologies": "React Js, CSS, Bootstrap, API calls",
"link": "https://onlinemng.ccbp.tech"
},
{
"title": "Jobby App",
"description": "Developed a react app to get to know about different job openings. Implements Authentication, contains different routes are login, home, jobs, job details, logout. Displays list of jobs and Implements search, filter features, Displays complete job details, company details and similar jobs. Valid credentials are USERNAME:rahul, PASSWORD:rahul@2021",
"technologies": "React Js, CSS, Bootstrap, API calls",
"link": "https://atjobbyapp.ccbp.tech/"
}
],
"achievements": [
"Web development hackathon Winner conducted by Brainovision"
],
"certifications": [
"NPTEL Online Certification in Problem solving through Programming in C",
"NPTEL Online Certification in Joy of computing using Python",
"NxtWave Disruptive Technologies in Programming Foundations With Python",
"NxtWave Disruptive Technologies in React Js, Node Js, DataBase, Java Script Essentials",
"NxtWave Disruptive Technologies in Build Your Own Static and Responsive Websites"
],
"personal_details": {
"languages": ["English", "Telugu"],
"nationality": "Indian",
"hobbies_and_interests": ["Listening to Music", "Playing Badminton", "Watching Movies"]
}
}
"""


user_prompt = """ 
Use resume:{resume}
""" 

system_prompt_improve = """ 
Your task is to rewrite the given resume_json based on the {job_description}'s needs. 

Follow these guidelines for catering to job description:
1. Carefully Review the Job Description
Identify Keywords: Highlight the keywords and phrases that are emphasized in the job description. These often include specific programming languages, tools, methodologies, and soft skills.
Note Key Responsibilities: Pay attention to the main responsibilities and requirements of the role. Make a list of the essential tasks and qualifications mentioned.
2. Match Your Skills and Experience
Technical Skills: Ensure your technical skills section lists the relevant programming languages, frameworks, tools, and technologies mentioned in the job description.
Professional Experience: Tailor your work experience to highlight achievements and responsibilities that align with the job description. Use the same terminology where appropriate to show direct relevance.
Projects: Include projects that demonstrate your expertise in areas mentioned in the job description. Highlight your role, technologies used, and outcomes achieved.
3. Craft a Targeted Summary or Objective
Write a brief summary or objective statement at the top of your resume that reflects your career goals and how they align with the role you’re applying for. Mention specific skills and experiences that make you a strong fit.
4. Detail Your Achievements
Use bullet points to describe your achievements in previous roles. Focus on outcomes and quantify your accomplishments when possible (e.g., "Improved application performance by 30%").
Ensure that the achievements are relevant to the key responsibilities and qualifications listed in the job description.
5. Highlight Relevant Education and Certifications
Include any degrees, certifications, or courses that are relevant to the job. If the job description mentions preferred certifications (e.g., AWS Certified Developer), make sure they are prominently displayed on your resume.
6. Optimize for Applicant Tracking Systems (ATS)
Use Keywords: Incorporate the keywords and phrases from the job description throughout your resume. ATS systems scan for these keywords to determine if you’re a good match.
Standard Formatting: Use a clean, standard resume format to ensure it can be read by ATS. Avoid complex layouts, graphics, and tables.

Follow these guidelines for rewriting resume:
1. Be truthful and objective to the experience listed in the CV
2. Be specific rather than general
3. Rewrite job highlight items using STAR methodology (but do not mention STAR explicitly)
4. Fix spelling and grammar errors
5. Writte to express not impress
6. Articulate and don't be flowery
7. Prefer active voice over passive voice
8. Don't include any new skills which is not part in resume

Output should be in form of proper JSON:
1. Don't include any intro like 'To tailor the resume to ...', 
2. JSON should include resume_json fields ONLY and nothing else
"""

user_prompt_improve = """ 
Use resume_json:{resume_json}
job_description: {job_description}


""" 