import streamlit as st
import plotly.graph_objs as go

# Title of the app
st.title("Wealth Dynamics Personality Quiz")

# Instructions
st.write("Answer the following questions to find out your Wealth Dynamics personality type!")

# Initialize scores
scores = {
    "A": 0,  # The Reformer
    "B": 0,  # The Helper
    "C": 0,  # The Achiever
    "D": 0   # The Individualist
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
    # Additional questions can be added here
]

# Function to update scores based on the user's answers
def update_scores(answer):
    if answer == "A":
        scores["A"] += 1
    elif answer == "B":
        scores["B"] += 1
    elif answer == "C":
        scores["C"] += 1
    elif answer == "D":
        scores["D"] += 1

# Collecting answers from the user
for question, options in questions:
    answer = st.radio(question, options, key=question)
    update_scores(answer)

# Sidebar for traits and key information
st.sidebar.title("Key Traits of Each Type")
traits = {
    "A": {"Integrity": 8, "Analysis": 9, "Self-control": 7},
    "B": {"Empathy": 9, "Generosity": 8, "Connection": 8},
    "C": {"Achievement": 9, "Adaptability": 7, "Drive": 8},
    "D": {"Creativity": 9, "Introspection": 8, "Authenticity": 7},
}

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
        st.write("You are principled and purposeful, always striving for integrity and improvement.")
    elif personality_type == "B":
        st.write("**Type B: The Helper**")
        st.write("You are caring and generous, often prioritizing the needs of others over your own.")
    elif personality_type == "C":
        st.write("**Type C: The Achiever**")
        st.write("You are success-oriented and adaptable, constantly seeking recognition and accomplishments.")
    elif personality_type == "D":
        st.write("**Type D: The Individualist**")
        st.write("You are introspective and unique, often seeking deeper meanings in life.")

    # Plotly line chart for top traits
    trait_names = list(traits[personality_type].keys())
    trait_values = list(traits[personality_type].values())

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=trait_names, y=trait_values, mode='lines+markers', name=personality_type))
    fig.update_layout(title=f"Top Traits for Type {personality_type}",
                      yaxis_title="Trait Score",
                      yaxis=dict(range=[0, 10]),
                      xaxis_title="Traits",
                      template='plotly_white')
    
    st.plotly_chart(fig)

# To run the app: 
# Save the script as app.py and run `streamlit run app.py` in the terminal
