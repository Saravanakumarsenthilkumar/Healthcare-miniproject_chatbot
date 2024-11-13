Healthcare Chatbot
This is a healthcare chatbot application built using Streamlit and Ollama's gemma:2b model. The chatbot answers healthcare-related questions concisely and includes advanced features like severity detection for urgent symptoms and links to trusted resources.

Features
Real-Time Healthcare Q&A: Provides concise answers to healthcare-related queries.
Severity Detection: Detects high-risk symptoms in questions (e.g., "chest pain," "difficulty breathing") and displays an urgent medical attention warning.
Helpful Resource Links: Offers links to trusted health resources based on query keywords (e.g., heart health, mental health).
Privacy Assurance: Displays a notice reminding users not to share sensitive information.
Conversation History: Keeps a history of the conversation within the session and allows the user to clear the conversation when done.
Styled User Interface: Custom-designed buttons and input fields for an improved user experience.
Setup Instructions
Prerequisites
Python 3.7+
Required Python Libraries:
streamlit: For building the interactive user interface.
ollama: For utilizing the gemma:2b model to generate healthcare responses.
Installation
Clone the repository or download the files.

git clone <repository-url>
cd healthcare-chatbot
Install the required Python packages.

pip install streamlit ollama
Ensure that ollama is installed and set up on your machine, as this application uses the gemma:2b model from Ollama.

Running the Application
Run the following command from the project directory to start the chatbot interface:

streamlit run app.py
Replace app.py with the filename if it’s different.

How to Use the Healthcare Chatbot
Ask Questions: Type your healthcare-related questions in the input box and click "Ask." The chatbot will provide a concise answer.
Severity Detection: If your question contains high-risk keywords, the chatbot will display a warning suggesting urgent medical attention.
Resource Links: For questions related to specific topics like heart health, mental health, or nutrition, the chatbot will provide a link to a trusted external resource.
End Conversation: To clear the chat history, click the "End Conversation" button.
Privacy Notice: A reminder is displayed, informing users to avoid sharing sensitive personal health information.
Code Overview
check_severity: This function checks for high-risk keywords and returns a warning message if any are detected in the user query.
get_resource_link: This function identifies keywords related to specific health topics and provides a relevant link to a trusted resource.
healthcare_chatbot: Uses Ollama’s gemma:2b model to generate responses based on the user’s healthcare-related question.
Streamlit Frontend: Handles the input, button interactions, and displays responses in a user-friendly format with styling for better readability.
Example Questions
Try asking questions like:

"I’m experiencing chest pain and shortness of breath."
"Can you provide tips on improving heart health?"
"What are some signs of mental health issues?"
These questions will demonstrate the chatbot’s severity detection, resource linking, and general answering capabilities.

License
This project is licensed under the MIT License. You may use, modify, and distribute it in accordance with the license terms.

