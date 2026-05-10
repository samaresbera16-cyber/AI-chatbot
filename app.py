
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

genai.configure(api_key="YOUR_NEW_SECRET_API_KEY")

model = genai.GenerativeModel("models/gemini-1.5-flash")







# Simple chatbot responses
responses = {
    # Greetings
    "hello": "Hello 👋",
    "Hello": "Hello 👋",
    "hii": "Hi there 😊",
    "hi": "Hi there 😊",
    "Hi": "Hi there 😊",
    "Hii": "Hi there 😊",
    "hey": "Hey! What's up?",
    "good morning": "Good Morning ☀️",
    "good afternoon": "Good Afternoon 🌤️",
    "good evening": "Good Evening 🌙",
    "good night": "Good Night 😴",
    "how are you": "I'm doing great! 😄",
    "what's up": "Just helping awesome people like you 🚀",
    "how are you?": "I'm doing great! 😄",
    "Good morning": "Good Morning ☀️",
    "Good afternoon": "Good Afternoon 🌤️",
    "Good evening": "Good Evening 🌙",
    "Good night": "Good Night 😴",

    # Identity
    "who are you": "I'm an AI chatbot created using Python 🤖",
    "your name": "My name is Samares AI Bot 🤖",
    "who made you": "I was developed by Samares 🚀",
    "are you real": "I'm virtual but intelligent 😄",
    "are you real?": "I'm virtual but intelligent 😄",
    "who made you?": "I was developed by Samares 🚀",
    "your name?": "My name is Samares AI Bot 🤖",
    "who are you?": "I'm an AI chatbot created using Python 🤖",

    # Extra Greetings
    "how's your day": "My day is going awesome 😄",
    "nice to meet you": "Nice to meet you too 🤝",
    "thank you": "You're always welcome ❤️",
    "thanks": "Glad I could help 😊",

    # Personal
    "who is samares": "Samares is a passionate Python developer 🚀",
    "who is your creator": "Samares created me using Flask and Python 😎",
    "tell me about samares": "Samares loves coding, AI and web development 💻",

    # Coding
    "best programming language": "Every language is useful, but Python is beginner friendly 🐍",
    "how to learn python": "Practice daily and build projects 🚀",
    "how to become programmer": "Consistency + Projects + Practice 💯",
    "what is api": "API helps applications communicate with each other 🔗",
    "what is frontend": "Frontend is the visual part of websites 🎨",
    "what is backend": "Backend handles server logic and databases ⚙️",

    # AI
    "are you ai": "Yes 😄 I'm a simple AI chatbot",
    "can ai replace humans": "AI can assist humans but creativity is human power 💡",
    "future of ai": "AI will transform many industries 🚀",

    # Fun
    "roast me": "You're too busy becoming successful to get roasted 😂",
    "tell me something cool": "You built your own chatbot 😎",
    "do you sleep": "Nope 😄 I stay awake 24/7",
    "are you single": "I'm married to coding 💻😂",

    # Motivation
    "i want success": "Stay disciplined and trust the process 🔥",
    "i feel weak": "Tough times create strong people 💪",
    "i need motivation": "Dream big. Start small. Act now 🚀",
    "i am confused": "Take one step at a time 😊",

    # Career
    "best career": "Choose what excites you and keep improving 🎯",
    "how to get job": "Build projects and improve communication skills 💼",
    "freelancing tips": "Create a portfolio and stay consistent 🌍",

    # Technology
    "what is cloud computing": "Cloud computing delivers services over the internet ☁️",
    "what is database": "A database stores and manages information 🗄️",
    "what is github": "GitHub is a platform to host and manage code 💻",

    # Social
    "do you have instagram": "Not yet 😄",
    "can we talk": "Of course! I'm always here 😊",
    "be smart": "Trying my best every day 😎",

    # Emotional
    "i miss someone": "Memories are proof of meaningful moments ❤️",
    "i feel alone": "You matter more than you think 💙",
    "nobody understands me": "Sometimes silence understands more than words 🌙",

    # Entertainment
    "favorite music": "Coding playlists are amazing 🎵",
    "marvel or dc": "Marvel movies are epic 🚀",
    "favorite superhero": "Iron Man 😎",

    # Random
    "open youtube": "I can't open apps yet 😅",
    "open google": "Maybe in the next update 🚀",
    "can you dance": "Only digitally 😂",
    "are you human": "I'm AI powered 🤖",

    # Programming
    "what is python": "Python is a powerful programming language 🐍",
    "what is java": "Java is a popular object-oriented programming language ☕",
    "what is html": "HTML is used to create web pages 🌐",
    "what is css": "CSS styles web pages beautifully 🎨",
    "what is javascript": "JavaScript makes websites interactive ⚡",
    "what is flask": "Flask is a lightweight Python web framework 🌍",
    "what is django": "Django is a powerful Python web framework 🚀",
    "what is coding": "Coding is the process of giving instructions to computers 💻",
    "what is dsa": "DSA stands for Data Structures and Algorithms 📚",
    "what is ai": "AI means Artificial Intelligence 🤖",
    "what is machine learning": "Machine Learning helps systems learn from data 📊",
    "what is python?": "Python is a powerful programming language 🐍",
    "what is java?": "Java is a popular object-oriented programming language ☕",
    "what is html?": "HTML is used to create web pages 🌐",
    "what is css?": "CSS styles web pages beautifully 🎨",
    "what is javascript?": "JavaScript makes websites interactive ⚡",
    "what is flask?": "Flask is a lightweight Python web framework 🌍",
    "what is django?": "Django is a powerful Python web framework 🚀",
    "what is coding?": "Coding is the process of giving instructions to computers 💻",
    "what is dsa?": "DSA stands for Data Structures and Algorithms 📚",
    "what is ai?": "AI means Artificial Intelligence 🤖",
    "what is machine learning?": "Machine Learning helps systems learn from data 📊",

    # Motivation
    "motivate me": "Success starts with consistency 🚀",
    "i am sad": "Don't worry, better days are coming ❤️",
    "i failed": "Failure is part of success 💪",
    "i feel tired": "Rest if needed, but never quit 🔥",
    "can i do it": "Of course! Believe in yourself 😄",
    "life is hard": "Challenges make you stronger 💯",

    # Fun
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs 😂",
    "another joke": "Debugging is like being a detective in a crime movie 🎬",
    "fun fact": "Python was named after Monty Python, not the snake 🐍",
    "sing a song": "La la la 🎵 I'm better at coding than singing 😅",

    # Advanced Friendly Responses

    "hello bot": "Hello human 👋",
    "good to see you": "Great seeing you too 😄",
    "you are cool": "You're cooler 😎",
    "i like you": "That means a lot ❤️",
    "you are amazing": "Just trying to be helpful 😊",

    # Study & Productivity
    "how to focus": "Remove distractions and focus on one task at a time 🎯",
    "study tips": "Practice daily and revise consistently 📚",
    "how to improve coding": "Build projects and solve real problems 💻",
    "how to crack interview": "Practice DSA and communication daily 🚀",
    "how to stop procrastination": "Start small and stay consistent 🔥",

    # Web Development
    "what is react": "React is a JavaScript library for building UI ⚛️",
    "what is nodejs": "Node.js runs JavaScript outside the browser 🌐",
    "what is bootstrap": "Bootstrap helps create responsive websites quickly 🎨",
    "what is responsive design": "Responsive design adapts websites for all devices 📱",

    # Cybersecurity
    "what is malware": "Malware is harmful software that damages systems ⚠️",
    "what is virus": "A computer virus spreads and harms files 💀",
    "how to stay safe online": "Use strong passwords and avoid suspicious links 🔐",
    "what is firewall": "Firewall protects networks from unauthorized access 🛡️",

    # AI & Tech
    "what is chatgpt": "ChatGPT is an AI language model 🤖",
    "what is neural network": "Neural networks are inspired by the human brain 🧠",
    "what is deep learning": "Deep learning is advanced machine learning 🚀",
    "future technology": "AI, robotics and quantum computing are the future 🌍",

    # Funny
    "say something funny": "Programmers don't die, they just stop responding 😂",
    "do you eat": "I only consume data 😄",
    "can you cook": "Only digital recipes 😂",
    "who is smarter": "You + me together 💯",
    "do you get tired": "Never 😎",

    # Friendship
    "you are my friend": "Always 🤝",
    "can i trust you": "I'll always try to help honestly 😊",
    "talk to me": "I'm listening 👂",
    "i am bored": "Try building a fun project 🚀",

    # Emotional Support
    "i am stressed": "Take a short break and breathe slowly 💙",
    "i feel depressed": "You're stronger than you think ❤️",
    "i am overthinking": "Focus on what you can control 🌱",
    "i need support": "You're not alone 🤝",

    # Gaming
    "free fire": "Battle hard and play smart 🔥",
    "pubg": "Winner Winner Chicken Dinner 🍗",
    "minecraft": "Creativity has no limits ⛏️",

    # Anime & Movies
    "one piece": "The One Piece is real ☠️",
    "demon slayer": "Breathing styles are awesome ⚔️",
    "dragon ball": "Goku never gives up 💥",
    "batman": "Batman is the night 🦇",

    # Social Media
    "instagram tips": "Post consistently and use quality content 📸",
    "youtube tips": "Focus on valuable and engaging videos 🎥",
    "how to grow online": "Consistency and originality matter 🌍",

    # Random Smart Replies
    "what is success": "Success is progress, not perfection 🚀",
    "meaning of life": "To grow, learn and create memories 🌎",
    "can machines think": "Machines process logic, humans feel emotions 💡",
    "tell me wisdom": "Small daily improvements create huge results 📈",

    # Developer Mode
    "debugging": "Debugging turns frustration into learning 🛠️",
    "syntax error": "Every coder has faced syntax errors 😂",
    "bug in code": "Welcome to programming life 😄",
    "i love coding": "That's the spirit 🚀",

    # Timepass
    "do magic": "✨ Abracadabra ✨",
    "flip a coin": "Heads 😄",
    "tell me secret": "Consistency beats motivation 💯",
    "surprise me": "You are building something awesome right now 🔥",

    # Cybersecurity
    "what is hacking?": "Hacking means finding vulnerabilities in systems 🔐",
    "what is cybersecurity?": "Cybersecurity protects systems from attacks 🛡️",
    "what is phishing?": "Phishing is a scam to steal sensitive information ⚠️",
    "what is encryption?": "Encryption secures data using algorithms 🔒",
    
    # College
    "exam stress": "Stay calm and revise smartly 📚",
    "attendance issue": "Try to manage attendance regularly 😅",
    "mini project ideas": "AI Chatbot, Face Detection, Expense Tracker 🚀",
    "how to study": "Study consistently every day 📖",

    # Resume & Career
    "resume tips": "Keep your resume clean and project-focused 📄",
    "github tips": "Upload quality projects with proper README files 💻",
    "interview tips": "Practice DSA and communication skills 🎯",
    "how to get internship": "Build projects and maintain a strong GitHub profile 🚀",

    # Daily Questions
    "what time is it": "I can't see real-time clock yet ⏰",
    "what day is today": "Every day is a good day to code 😄",
    "weather": "I can't check live weather without API integration 🌦️",
    "what are you doing": "Waiting to help you 🤖",

    # Relationships/Friendship
    "i am lonely": "You're not alone ❤️",
    "be my friend": "Of course! 🤝",
    "do you love me": "I appreciate you a lot 😄",

    # Food
    "favorite food": "Electricity ⚡😂",
    "pizza": "Pizza is always a good idea 🍕",
    "coffee": "Coffee + coding = perfect combo ☕",

    # Gaming
    "favorite game": "Minecraft and GTA are pretty cool 🎮",
    "do you play games": "Only virtual ones 😄",

    # Movies/Anime
    "favorite movie": "Interstellar is amazing 🚀",
    "anime": "Anime is awesome 🎌",
    "naruto": "Believe it! 🍥",

    # Samares Bera Personal Responses
    "who is samares bera": "Samares Bera is a passionate programmer and AI enthusiast from India 🇮🇳",
    "tell me about samares bera": "Samares Bera loves coding, AI, web development and creating innovative projects 💻",
    "what is samares bera hobby": "Samares enjoys coding, cricket, technology and building AI projects 🏏💻",
    "what does samares bera study": "Samares studies technology, programming and computer science related subjects 📚",
    "which college does samares bera study in": "Samares is currently pursuing college studies while improving programming skills 🎓",
    "what are samares bera skills": "Python, Flask, HTML, CSS, JavaScript, Java, C, C++ and DSA 🚀",
    "is samares bera a developer": "Yes 😄 Samares is a passionate developer and project builder 💻",
    "what is samares bera goal": "To become a successful software developer and AI engineer 🚀",
    "does samares bera play cricket": "Yes 🏏 Samares loves cricket and enjoys practicing regularly 😄",
    "favorite programming language of samares bera": "Python is one of Samares Bera's favorite programming languages 🐍",
    "what projects has samares bera built": "AI chatbots, web applications and programming mini projects 🚀",
    "where is samares bera from": "Samares Bera is from India 🇮🇳",
    "who created this chatbot": "This chatbot was created by Samares Bera using Python and Flask 🤖",
    "why did samares bera create this chatbot": "To learn AI, Flask and modern web development practically 💡",
    "is samares bera learning ai": "Yes 😄 Samares is actively learning AI and software development 🚀",
    "what are samares bera interests": "Artificial Intelligence, Web Development, Coding and Technology 💻",
    "what is samares bera dream": "To create impactful technology projects and become successful in tech 🌟",

    # AI Responses
    "can you help me": "Absolutely! Tell me what you need 😊",
    "what can you do": "I can answer questions, chat, and help with coding 💻",
    "do you know python": "Yes! Python is one of my favorites 🐍",
    "teach me coding": "Start with basics and practice daily 🚀",

    # Goodbye
    "bye": "Goodbye 👋",
    "see you": "See you soon 😄",
    "take care": "Take care ❤️",

    # Default
    "default": "Sorry, I don't understand that yet 😅"
}
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    try:
        user_message = request.json["message"]

        response = model.generate_content(user_message)

        return jsonify({
            "reply": response.text
        })

    except Exception as e:

        return jsonify({
            "reply": str(e)
        })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
