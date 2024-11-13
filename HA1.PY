import streamlit as st
import ollama

# Initialize session state for storing conversation history
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Add resources and severity keywords for enhanced features
resources = {
    "heart health": "https://www.heart.org",
    "mental health": "https://www.nimh.nih.gov",
    "nutrition": "https://www.eatright.org"
}
severe_keywords = ["chest pain", "difficulty breathing", "severe bleeding", "unconscious", "heart attack", "stroke"]

def check_severity(query):
    """Checks for high-risk symptoms in the query and returns a warning if found."""
    if any(keyword in query.lower() for keyword in severe_keywords):
        return "⚠️ This symptom may require urgent medical attention. Please contact emergency services."
    return None

def get_resource_link(query):
    """Provides a helpful resource link if a relevant keyword is detected in the query."""
    for key in resources:
        if key in query.lower():
            return resources[key]
    return None

def healthcare_chatbot(query):
    # Define the prompt for the healthcare-related query response
    prompt = f"Respond concisely to the following healthcare query:\n\n{query}\n\nProvide a clear and accurate response without any introductory phrases."

    # Use Ollama's gemma:2b model to generate a response
    response = ollama.generate(
        model="gemma:2b",
        prompt=prompt
    )
    
    # Extract the answer from the response key
    answer = response.get('response', "No response available.").strip()
    return answer

# Streamlit frontend design
st.title("Healthcare Chatbot")
st.write("Ask any healthcare-related questions below, and the chatbot will provide concise answers.")
st.markdown("**Privacy Notice:** This chatbot does not store or share any personal health data beyond this session. Please avoid sharing sensitive information.")

# Input for healthcare question
query = st.text_input("Your question:")

# Button to submit the question
if st.button("Ask"):
    if query:
        # Check for severity and display warning if needed
        severity_warning = check_severity(query)
        if severity_warning:
            st.warning(severity_warning)

        # Get answer from chatbot
        answer = healthcare_chatbot(query)
        
        # Provide a relevant resource link if applicable
        resource_link = get_resource_link(query)
        if resource_link:
            answer += f"\n\nFor more information, visit [this resource]({resource_link})."
        
        # Store the query and answer in session state
        st.session_state.conversation.append({"query": query, "answer": answer})

# Display the conversation history
st.markdown("### Chat History")
for i, convo in enumerate(st.session_state.conversation):
    st.write(f"**You:** {convo['query']}")
    st.write(f"**Chatbot:** {convo['answer']}")
    st.markdown("---")

# Stop conversation button to clear history
if st.button("End Conversation"):
    st.session_state.conversation = []

# Style customization with Streamlit's styling options
st.markdown("""
    <style>
        /* Customize chat interface */
        .stButton > button {
            background-color: #0d6efd;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            padding: 8px 16px;
            margin-top: 10px;
        }
        .stTextInput > div > div > input {
            border: 2px solid #0d6efd;
            border-radius: 10px;
            padding: 10px;
        }
        .stApp {
            background-color: #f7f9fc;
            font-family: 'Arial', sans-serif;
        }
        h1 {
            color: #0d6efd;
            font-size: 32px;
            font-weight: 700;
        }
        .markdown-text-container {
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)
