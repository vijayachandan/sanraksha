document.addEventListener('DOMContentLoaded', () => {
    const chatBody = document.getElementById('chat-body');

    // Send message when Enter key is pressed
    document.getElementById('user-input').addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
});

// Predefined responses for the chatbot
const responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! What can I do for you?",
    "what is a fever": "A fever is a temporary increase in your body temperature, often due to an illness.",
    "how to treat a cold": "Rest, drink plenty of fluids, and consider taking over-the-counter medications to relieve symptoms.",
    "what is a healthy diet": "A healthy diet includes a balance of fruits, vegetables, whole grains, proteins, and healthy fats. It's important to limit processed foods, sugar, and salt.",
    "how to reduce stress": "Some effective ways to reduce stress include practicing mindfulness, exercising, maintaining a healthy diet, and ensuring adequate sleep.",
    "symptoms of covid-19": "Common symptoms of COVID-19 include fever, cough, fatigue, loss of taste or smell, and difficulty breathing. If you experience any of these, consider getting tested.",
    "how to improve sleep": "To improve sleep, maintain a consistent sleep schedule, create a comfortable sleep environment, and avoid caffeine or screens before bedtime.",
    "what is hypertension": "Hypertension, or high blood pressure, is a condition where the force of the blood against the artery walls is too high, often requiring lifestyle changes or medication to control.",
    "exercise for weight loss": "Cardio exercises like running, cycling, and swimming, along with strength training, can be effective for weight loss when combined with a healthy diet.",
    "emergency contact numbers": "For any emergency, call 911 in the U.S., 112 in Europe, or the local emergency number in your country.",
    "default": "I'm not sure how to respond to that. Can you please rephrase your question?"
};

// Function to send a message
function sendMessage() {
    const userInput = document.getElementById('user-input');
    const message = userInput.value.trim();

    if (message === "") return;

    addMessageToChat('user-message', message);
    userInput.value = '';

    setTimeout(() => {
        getBotResponse(message.toLowerCase());
    }, 500); // Simulate delay
}

// Function to display messages in the chat
function addMessageToChat(type, text) {
    const chatBody = document.getElementById('chat-body');
    const messageElement = document.createElement('div');
    messageElement.className = `chat-message ${type}`;
    messageElement.textContent = text;
    chatBody.appendChild(messageElement);
    chatBody.scrollTop = chatBody.scrollHeight;
}

// Function to generate chatbot response
function getBotResponse(message) {
    const response = responses[message] || responses["default"];
    addMessageToChat('bot-message', response);
}
