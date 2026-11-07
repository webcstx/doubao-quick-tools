from quick_ai import QuickAI
ai = QuickAI(size="0.5B")
print(ai.info())
while True:
    msg = input("你: ")
    if msg.lower() == "exit": break
    print("AI:", ai.chat(msg))
