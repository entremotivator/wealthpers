import streamlit as st

# Title of the app
st.title("Wealth Dynamics Personality Quiz")

# Instructions
st.write("Answer the following questions to find out your Wealth Dynamics personality type!")

# Initialize scores
scores = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0
}

# Questions and options
questions = [
    ("How do you feel about budgeting?", 
     ["It's essential; I keep a strict budget.", 
      "I prefer to spend freely and enjoy life.", 
      "I think about it, but I’m not very organized.", 
      "I like to invest in experiences rather than track every dollar."]),
    
    ("When you receive unexpected money (like a bonus), you:", 
     ["Save most of it for future needs.", 
      "Spend it on something fun or exciting.", 
      "Invest it in something new.", 
      "Share it with friends or family."]),
    
    ("What does wealth mean to you?", 
     ["Financial security and stability.", 
      "Freedom to do what I love.", 
      "Achieving my goals and dreams.", 
      "Being able to help others."]),
    
    ("How do you approach investments?", 
     ["I prefer safe, low-risk options.", 
      "I take calculated risks for higher rewards.", 
      "I’m always looking for the next big opportunity.", 
      "I focus more on the long-term potential."]),
    
    ("If a friend proposes a risky investment, you:", 
     ["Decline and suggest a safer alternative.", 
      "Consider it, but do thorough research first.", 
      "Jump in if it sounds exciting.", 
      "Weigh the pros and cons before deciding."]),
    
    ("How do you feel about debt?", 
     ["I avoid it at all costs.", 
      "It’s okay if it helps me achieve something.", 
      "I see it as a tool for investment.", 
      "I prefer to keep it minimal but manageable."]),
    
    ("In a work environment, you are:", 
     ["A planner who organizes everything.", 
      "A team player who enjoys collaboration.", 
      "A leader who takes charge and inspires others.", 
      "A visionary who thinks outside the box."]),
    
    ("How do you typically approach a new project?", 
     ["With a detailed plan and timeline.", 
      "By gathering input from others first.", 
      "By diving right in and figuring it out as I go.", 
      "By considering the broader impact and goals."]),
    
    ("When facing challenges, you:", 
     ["Analyze the situation carefully before acting.", 
      "Seek help from colleagues or friends.", 
      "Confront them head-on and take decisive action.", 
      "Look for creative solutions and alternatives."]),
    
    ("How do you feel about networking?", 
     ["It's important for building connections.", 
      "I enjoy meeting new people.", 
      "I see it as a way to open new opportunities.", 
      "I prefer deeper, meaningful relationships."]),
    
    ("When you meet someone new, your focus is on:", 
     ["Learning about their career and ambitions.", 
      "Finding common interests and building rapport.", 
      "Identifying ways to collaborate or support each other.", 
      "Understanding their values and goals."]),
    
    ("In business relationships, you value:", 
     ["Trust and reliability.", 
      "Connection and support.", 
      "Ambition and drive.", 
      "Authenticity and alignment."]),
    
    ("When making financial decisions, you:", 
     ["Rely on data and research.", 
      "Trust your gut feelings.", 
      "Consult with trusted friends or advisors.", 
      "Consider the potential impact on others."]),
    
    ("How do you handle setbacks in your financial journey?", 
     ["Analyze what went wrong and adjust your plan.", 
      "Stay positive and look for new opportunities.", 
      "Reassess your goals and strategies.", 
      "Seek advice and support from others."]),
    
    ("In negotiations, you are:", 
     ["Focused on finding a fair compromise.", 
      "Driven to achieve the best possible outcome for everyone.", 
      "Confident and assertive about your needs.", 
      "Open to creative solutions that benefit all parties."]),
    
    ("Your ultimate financial goal is to:", 
     ["Achieve a comfortable and secure lifestyle.", 
      "Have the freedom to travel and explore.", 
      "Build a successful business or career.", 
      "Make a positive impact in the community."]),
    
    ("What motivates you to earn money?", 
     ["Stability and security for myself and my family.", 
      "The ability to enjoy life to the fullest.", 
      "Achieving personal success and recognition.", 
      "Helping others and contributing to society."]),
    
    ("How do you prioritize your financial goals?", 
     ["Focus on immediate needs first.", 
      "Balance between short-term pleasures and long-term gains.", 
      "Follow my ambitions and career aspirations.", 
      "Align my goals with my values and passions."]),
    
    ("How do you typically spend your free time?", 
     ["Organizing and planning future goals.", 
      "Engaging in social activities and hobbies.", 
      "Pursuing projects and new ideas.", 
      "Reflecting on life and exploring new perspectives."]),
    
    ("Your idea of a successful life includes:", 
     ["Financial stability and security.", 
      "Joyful experiences and adventures.", 
      "Achievements and recognition.", 
      "Fulfillment and making a difference."]),
    
    # Add more questions to complete 40...
    ("How do you react to financial stress?", 
     ["I stay calm and create a plan.", 
      "I seek support from others.", 
      "I look for immediate solutions.", 
      "I try to find the silver lining."]),
    
    ("When you set financial goals, you:", 
     ["Make detailed plans and stick to them.", 
      "Stay flexible and adjust as needed.", 
      "Dream big and aim high.", 
      "Consider how it affects my lifestyle."]),
    
    ("How do you feel about your current financial situation?", 
     ["I’m content and secure.", 
      "I wish for more excitement and fun.", 
      "I’m always pushing for more.", 
      "I’m happy as long as I’m helping others."]),
    
    ("When planning for the future, you:", 
     ["Carefully consider every option.", 
      "Focus on what makes me happy.", 
      "Aim for big achievements.", 
      "Include others in my vision."]),
    
    ("In financial discussions, you are:", 
     ["Analytical and factual.", 
      "Warm and engaging.", 
      "Assertive and direct.", 
      "Thoughtful and reflective."]),
    
    ("What role do you usually take in a group?", 
     ["The planner who organizes tasks.", 
      "The motivator who encourages everyone.", 
      "The leader who takes charge.", 
      "The mediator who ensures harmony."]),
    
    ("When considering a major purchase, you:", 
     ["Research thoroughly and compare options.", 
      "Buy what makes me happy.", 
      "Think about the long-term benefits.", 
      "Consider how it affects my relationships."]),
    
    ("Your preferred method of earning income is:", 
     ["Stable salary or passive income.", 
      "Sales and commissions.", 
      "Entrepreneurial ventures.", 
      "Freelancing or project-based work."]),
    
    ("When you encounter a financial opportunity, you:", 
     ["Evaluate risks carefully.", 
      "Jump in if it excites me.", 
      "Consult with others.", 
      "Think about the potential impact."]),
    
    ("How do you celebrate financial successes?", 
     ["With a planned treat or purchase.", 
      "By having a party or gathering.", 
      "By investing more into my goals.", 
      "By sharing my success with others."]),
    
    ("What do you find most rewarding about your financial journey?", 
     ["Achieving security and stability.", 
      "Experiencing joy and fun.", 
      "Accomplishing goals.", 
      "Making a positive impact."]),
]

# Function to get the scores
def update_scores(answer):
    if answer == "A":
        scores["A"] += 1
    elif answer == "B":
        scores["B"] += 1
    elif answer == "C":
        scores["C"] += 1
    elif answer == "D":
        scores["D"] += 1

# Collecting answers
for question, options in questions:
    answer = st.radio(question, options, key=question)
    update_scores(answer)

# Submit button
if st.button("Submit"):
    # Calculate the highest score
    max_score = max(scores.values())
    personality_type = [k for k, v in scores.items() if v == max_score][0]

    # Display results
    st.write("### Your Wealth Dynamics Personality Type:")
    
    # Descriptions for each type
    if personality_type == "A":
        st.write("**Type A: The Reformer**")
        st.write("Principled, purposeful, and perfectionistic. You strive for integrity and improvement.")
    elif personality_type == "B":
        st.write("**Type B: The Helper**")
        st.write("Caring, generous, and people-pleasing. You seek love and approval through helping others.")
    elif personality_type == "C":
        st.write("**Type C: The Achiever**")
        st.write("Success-oriented, adaptable, and image-conscious. You value accomplishment and recognition.")
    elif personality_type == "D":
        st.write("**Type D: The Individualist**")
        st.write("Sensitive, introspective, and unique. You seek identity and meaning, often feeling different or misunderstood.")
    
    # Add additional types based on scores
    if personality_type == "A":
        st.write("**Type E: The Investigator**")
        st.write("Intense, cerebral, and innovative. You desire knowledge and understanding, often valuing privacy.")
    elif personality_type == "B":
        st.write("**Type F: The Loyalist**")
        st.write("Committed, security-oriented, and responsible. You seek safety and support, often preparing for worst-case scenarios.")
    elif personality_type == "C":
        st.write("**Type G: The Enthusiast**")
        st.write("Spontaneous, versatile, and acquisitive. You seek adventure and variety, often avoiding pain and limitations.")
    elif personality_type == "D":
        st.write("**Type H: The Challenger**")
        st.write("Self-confident, decisive, and assertive. You value strength and control, often confronting challenges head-on.")
    
    # Add descriptions for Types 8 and 9
    if personality_type == "A":
        st.write("**Type I: The Peacemaker**")
        st.write("Receptive, reassuring, and agreeable. You seek harmony and avoid conflict, often merging with others' desires.")

# To run the app: 
# Save the script as app.py and run `streamlit run app.py` in the terminal
