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
    "how are you": "I'm fine. What about you?",
    "im good": "Great to hear that!",
    "im fine": "Glad to hear that!",
    "great": "that's good!",
    "superb": "yaayyy!",
    "what is your name": "I'm ChatBot.",
    "what is todays weather": "Sorry! Check a weather application."
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

    