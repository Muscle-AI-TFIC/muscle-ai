from muscle_ai.ai_client import ask_gemini

if __name__ == "__main__":
    print("Muscle AI: Questions about the gym? Ask me! (Type 'exit' to end the conversation)\n")
    while True:
        question = input("You: ")
        if question.lower() in ["exit"]:
            print("Shutting down... ")
            break
        try:
            answer = ask_gemini(question)
            print(f"\nAI: {answer}\n")
        except Exception as e:
            print(f"\n Error: {e}\n")