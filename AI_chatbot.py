import re

print("AI ChatBot:I'm your Chatbot...")
print("Type 'exit' to quit.\n")
name = input("Please Enter your name user: ").title()

greetings = ("hello","hi","hey","hola")
farewell = ("bye","bye bye","goodbye","see ya","see you")


knowledge_base = {}

for word in greetings:
    knowledge_base[word] = f"Hello {name}!"

for word in farewell:
    knowledge_base[word] = f"See you later {name}!"

knowledge_base.update({

    # Feelings
    "how are you": "I'm fine. What about you?",
    "im good": "Great to hear that!",
    "im fine": "Glad to hear that!",
    "great": "That's awesome!",
    "superb": "Yayyy!",
    "im sad": "I'm sorry to hear that.",
    "im tired": "Maybe take a short break and rest.",
    "im bored": "Try learning something new or playing a game!",

    # Personal Questions
    "what is your name": "I'm ChatBot.",
    "who are you": "I'm a simple AI chatbot.",
    "who made you": "I was created using Python.",
    "are you real": "I'm a virtual assistant.",

    # Time & Date
    "what day is today": "I don't know today's date yet.",
    "what time is it": "I can't check the time right now.",

    # Learning
    "what is python": "Python is a popular programming language.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine Learning enables computers to learn from data.",
    "what is cybersecurity": "Cybersecurity protects systems and data from attacks.",

    # Fun
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
    "tell me something interesting": "The first computer bug was an actual moth found in a computer.",
    "do you like pizza": "I can't eat, but pizza sounds popular!",
    "what is your favorite color": "I like all colors equally.",

    # Weather
    "what is todays weather": "Sorry! Check a weather application.",
    "is it raining": "I can't access live weather data.",

    # Help
    "help": "Try saying hello, asking my name, or requesting a joke.",
    "what can you do": "I can answer simple questions and chat with you.",
    "commands": "Try: hello, joke, python, ai, help, bye.",

    # Gratitude
    "thank you": "You're welcome!",
    "thanks": "Happy to help!",
    "thanks chatbot": "Anytime!",

    # Farewell Extras
    "good night": "Good night! Sweet dreams.",
    "good morning": "Good morning! Have a great day.",
    "good afternoon": "Good afternoon!",
    "good evening": "Good evening!"
})

while True:

    user = input("You: ").lower().strip()
    user = re.sub(r"[^\w\s]", "", user)
    if user == "exit":
        print("Bot: Goodbye!")
        break
    
    response = knowledge_base.get(
        user,
        "Sorry, I don't understand that."
    )
    print("Bot:", response)

    
