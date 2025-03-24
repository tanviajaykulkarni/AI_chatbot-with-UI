# AI_chatbot-with-UI
Learn to build AI-powered chatbots using Flask &amp; Python! 🚀 Simple, fast, and interactive chatbot development

![Yellow   Orange Modern Marketing Courses YouTube Thumbnail (2)](https://github.com/user-attachments/assets/ceaee688-4c7c-4c90-a2e9-2e2806d5f3fb)
youtube link:-
(https://www.youtube.com/watch?v=FbBSyk51zM0)

steps:-
1. Install Required Packages
Ensure you have Python installed on your system.

Navigate to your project directory in the terminal or command prompt.

Install all dependencies specified in the requirements.txt file using the following command:

pip install -r requirements.txt

This will install all the necessary libraries needed for the project, such as Flask, OpenAI (or Groq's SDK), and other dependencies.

2. Create an API Key in Groq and Update .env File
Go to the Groq website and sign in (or create an account if you don’t have one).

Generate a new API Key from the API section.

In your project directory, create a .env file if it doesn’t already exist.

Open the .env file and add the API key like this:

GROQ_API_KEY=your_generated_api_key

This key will be used by the chatbot to communicate with the LLM models available in Groq.

3. Create a Folder for index.html and Reference It in the Code
Inside your project directory, create a new folder (e.g., templates) to store HTML files.

Move your index.html file into this templates folder.

Your project structure should look like this:

/project_directory  
│── /templates  
│   ├── index.html  
│── chat_bot.py  
│── .env  
│── requirements.txt  
In your Python code (chat_bot.py), modify the Flask configuration to use this folder for rendering HTML templates:


4. Use the LLM Models Mentioned in the Code or Choose One from Groq
If the code specifies a particular LLM model, ensure that it is correctly referenced in your implementation.

If you want to use a different model available in Groq, update your chatbot code accordingly.

5. Run the Flask Application and Interact with the Chatbot
Start the Flask app by running the following command in your terminal:

python chat_bot.py
Once the server is running, Flask will provide a URL (e.g., http://127.0.0.1:5000/).

Open this URL in your browser to access the chatbot UI.

Enter your queries and chat with the AI bot.

Verify that the responses align with your expectations.
