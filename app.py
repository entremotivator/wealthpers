import streamlit as st

# Title of the app
st.title("Wealth Dynamics Personality Quiz")

# Instructions
st.write(
    "Welcome to the Wealth Dynamics Personality Quiz! This quiz will help you discover which of the 4 Wealth Dynamics personality types best represents you."
)
st.write(
    "Answer the following questions honestly to get the most accurate result. At the end of the quiz, you'll receive a detailed description of your personality and what that means for your wealth journey."
)

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
        st.write(
            "As a Type A, you are known for your strong sense of integrity and a deep desire to improve both yourself and the world around you. "
            "You are highly analytical, often thinking about long-term stability and security. You may find yourself drawn to roles where you can create structure, systems, and sustainable growth. "
            "Your wealth strategy likely focuses on minimizing risk and maximizing stability, whether through investments, career choices, or lifestyle decisions."
        )
        st.write("**Strengths**: Analytical thinking, integrity, discipline")
        st.write("**Challenges**: Can be overly cautious or resistant to change")

    elif personality_type == "B":
        st.write("**Type B: The Helper**")
        st.write(
            "As a Type B, you are deeply empathetic and driven by a desire to help others. You naturally put others’ needs before your own, whether it's in your career, friendships, or family relationships. "
            "You tend to attract opportunities for collaboration and teamwork, thriving in environments where you can build connections and support others. "
            "Your wealth dynamics revolve around leveraging relationships and community-oriented investments, and you may find fulfillment in using wealth to improve the lives of others."
        )
        st.write("**Strengths**: Empathy, generosity, collaboration")
        st.write("**Challenges**: Can neglect your own needs or overextend yourself")

    elif personality_type == "C":
        st.write("**Type C: The Achiever**")
        st.write(
            "As a Type C, you are goal-oriented and driven by a desire to achieve success. You are adaptable, constantly seeking new opportunities to grow and improve. "
            "You tend to be ambitious and may prioritize career or financial success as part of your wealth-building strategy. You are always looking for ways to optimize your performance and achieve measurable results. "
            "Your wealth strategy revolves around high-energy, high-reward endeavors, and you thrive in competitive or fast-paced environments."
        )
        st.write("**Strengths**: Achievement-focused, adaptable, driven")
        st.write("**Challenges**: Can be too focused on success and lose sight of personal well-being")

    elif personality_type == "D":
        st.write("**Type D: The Individualist**")
        st.write(
            "As a Type D, you are introspective and value authenticity. You are naturally creative and often think outside the box. "
            "You might feel more comfortable in unconventional career paths or investment strategies that allow you to express your unique talents and ideas. "
            "Your wealth strategy focuses on long-term vision and creative pursuits, and you often seek meaningful projects that resonate with your deeper values."
        )
        st.write("**Strengths**: Creativity, independence, authenticity")
        st.write("**Challenges**: Can struggle with structure and routine")

    # Detailed Key Traits for Each Type
    st.write("### Key Traits of Your Personality:")
    st.write(f"**Type {personality_type} - Key Traits**")
    for trait, value in traits[personality_type].items():
        st.write(f"- {trait}: {value}")

    st.write(
        "These traits define how you approach wealth-building and decision-making. Understanding these traits can help you align your financial goals with your natural strengths, making your wealth-building journey more effective and fulfilling."
    )

    # Encourage User to Reflect
    st.write(
        "Now that you've learned about your Wealth Dynamics personality type, reflect on how these traits show up in your life. "
        "How can you use your strengths to build a more prosperous future? Consider how you can leverage your unique traits to maximize your potential."
    )

    st.write(
        "Thank you for taking the quiz! Feel free to share your results with friends or come back for further insights on how to apply your Wealth Dynamics personality to your financial strategies."
    )

# To run the app:
# Save the script as app.py and run `streamlit run app.py` in the terminal
