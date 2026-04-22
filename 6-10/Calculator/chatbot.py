import re
from add import add
from sub import sub

def parse_input(user_input):
    # Simple parsing for add or sub
    add_match = re.search(r'add (\d+) and (\d+)', user_input.lower())
    if add_match:
        a, b = int(add_match.group(1)), int(add_match.group(2))
        result = add(a, b)
        return f"The sum is {result}"
    
    sub_match = re.search(r'subtract (\d+) from (\d+)', user_input.lower())
    if sub_match:
        a, b = int(sub_match.group(1)), int(sub_match.group(2))
        result = sub(b, a)
        return f"The difference is {result}"
    
    return "I can only add or subtract numbers. Try 'add 2 and 3' or 'subtract 5 from 10'"

def chatbot():
    print("Hello! I'm a calculator chatbot. Ask me to add or subtract numbers.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break
        response = parse_input(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    chatbot()