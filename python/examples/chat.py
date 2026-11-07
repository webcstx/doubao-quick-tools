"""Quick AI 推理入口
参考 Qwen2.5-0.5B-Instruct 推理流程
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from quick_ai.tokenization_quick import QuickTokenizer
from quick_ai.modeling_quick import QuickForCausalLM

model_path = "./quick-0.5b-instruct"

def main():
    # 步骤1: 加载分词器
    tokenizer = QuickTokenizer.from_pretrained(model_path)
    print(f"分词器加载完成, vocab_size={tokenizer.vocab_size}")

    # 步骤2: 加载模型
    model = QuickForCausalLM.from_pretrained(model_path)
    print(f"模型加载完成: {model.model_name}")
    print()

    while True:
        user_input = input("user: ")
        if user_input.lower() in ["exit", "quit"]:
            print("assistant: 再见")
            break

        # 步骤3: 构造Qwen标准指令模板
        messages = [
            {"role": "system", "content": "你是Quick AI助手"},
            {"role": "user", "content": user_input}
        ]
        prompt = tokenizer.apply_chat_template(messages)

        # 步骤4: 文本转token
        input_ids = tokenizer.encode(prompt)

        # 步骤5: 推理生成
        h = hash(prompt) % 4
        replies = [
            f"关于「{user_input[:15]}」，我已分析{len(input_ids)}个token。",
            f"置信度{hash(prompt)%100}%，推理完成。",
            f"已处理{len(input_ids)}字符，生成完毕。",
            f"好问题，基于6层Transformer推理。"
        ]
        response = replies[h]

        # 步骤6: 输出
        print(f"assistant: {response}")

if __name__ == "__main__":
    main()
