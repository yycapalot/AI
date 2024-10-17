import streamlit as st


# Function to display the chatbot interface
def show_chatbot():
    # Custom CSS for the chatbot
    chatbot_css = """
    <style>
    .chatbot {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 300px;
        height: 400px;
        border: 1px solid #ccc;
        border-radius: 8px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        background-color: white;
        display: none;  /* Hidden by default */
        z-index: 9999;
    }
    .chatbot-header {
        background-color: #4CAF50;
        color: white;
        padding: 10px;
        text-align: center;
        border-top-left-radius: 8px;
        border-top-right-radius: 8px;
    }
    .chatbot-body {
        padding: 10px;
        height: 320px;
        overflow-y: auto;  /* Scroll if needed */
    }
    .chatbot-input {
        padding: 10px;
        border: none;
        width: 100%;
        box-sizing: border-box;
    }
    .chatbot-button {
        padding: 10px;
        background-color: #4CAF50;
        color: white;
        border: none;
        cursor: pointer;
        width: 100%;
        border-bottom-left-radius: 8px;
        border-bottom-right-radius: 8px;
    }
    </style>
    <script>
    function toggleChatbot() {
        var chatbot = document.getElementById("chatbot");
        chatbot.style.display = chatbot.style.display === "none" ? "block" : "none";
    }
    </script>
    """
    st.markdown(chatbot_css, unsafe_allow_html=True)

    # Chatbot HTML structure
    chatbot_html = """
    <div class="chatbot" id="chatbot">
        <div class="chatbot-header">Chatbot</div>
        <div class="chatbot-body" id="chatbot-body">
            <div id="chatbot-messages">
                HI
            </div>
        </div>
        <
            input class="chatbot-input" id="chatbot-input"
            type="text" placeholder="Type your message..."
        />
        <button class="chatbot-button" onclick="sendMessage()">Send</button>
    </div>
    <button onclick="toggleChatbot()" style="
        border: 1px solid red;
        color: blue;
        position: relative;
        float: right;
        top: 10px;">
        Chat
    </button>
    <script>
    function sendMessage() {
        var input = document.getElementById("chatbot-input");
        var message = input.value;
        if (message) {
            var messagesDiv = document.getElementById("chatbot-messages");
            messagesDiv.innerHTML += "<div>User: " + message + "</div>";
            input.value = "";  // Clear input
            // Simulate bot response
            setTimeout(() => {
                messagesDiv.innerHTML += "<div>Bot: "+getBotResponse(message)+"</div>";
            }, 1000);
        }
    }

    function getBotResponse(message) {
        // Simple predefined responses
        const responses = {
            "hi": "Hello! How can I help you?",
            "how are you?": "I'm just a bot, but thanks for asking!",
            "what's your name?": "I'm a simple chatbot.",
            "bye": "Goodbye! Have a great day!",
        };
        return responses[message.toLowerCase()] || "I didn't understand that.";
    }
    </script>
    """

    st.markdown(chatbot_html, unsafe_allow_html=True)


# Streamlit application title
st.title("Streamlit Chatbot Example")

# Call the function to display the chatbot
show_chatbot()
