from quick_ai import QuickAI
ai = QuickAI(size="1.5B")
prompt = input("提示词: ")
print(ai.generate(prompt))
