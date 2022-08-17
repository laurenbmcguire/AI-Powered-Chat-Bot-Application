import os

import openai

my_secret = os.environ['OPENAI_API_KEY']

completion = openai.Completion()

# Default chat setting
start_chat_log = '''
The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.

Human: Hello, who are you?
AI: I am an AI created by OpenAI. How can I help you today?
'''

chat_log = None


def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    prompt = f'{chat_log}Human: {question}\nAI:'
    response = completion.create(
        prompt=prompt, engine="davinci", stop=["\n\n", "Human: "], temperature=0.7,
        top_p=1, frequency_penalty=.3, presence_penalty=0.6, best_of=1,
        max_tokens=1500)
    answer = response.choices[0].text.strip()
    return answer


def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    return f'{chat_log} {question}\n {answer}\n'
