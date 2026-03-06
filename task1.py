import datetime
def my_smart_bot():
    print("--- Welcome to my AI Chatbot (Version 2.0) ---")
    print("Commands: 'time','weather','ai','hi','quit'")
    while True:
        user_text=input("Me: ").lower()
        if "hello" in user_text or "hi" in user_text:
            print("Bot: Hey there! Hope you are having a productive day.")
        elif "time" in user_text:
            t=datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Bot: The current time is {t}. Time to code!")
        elif "weather" in user_text:
            print("Bot: I can't check the sky, but it's always 72 degrees inside this computer!")
        elif "ai" in user_text or "task" in user_text:
            print("Bot: AI is amazing! This is Task 1 of my CodSoft internship.")
        elif "codsoft" in user_text:
            print("Bot: They are a great community for student developers!")
        elif "quit" in user_text or "exit" in user_text:
            print("Bot: Catch you later! Good luck with your other 2 tasks.")
            break
        else:
            print("Bot: I'm not quite sure about that. Try asking for the 'time'!")
if __name__=="__main__":
    my_smart_bot()