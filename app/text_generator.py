from gpt4all import GPT4All
import random

# Initialize the GPT-4All model with a valid model name
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

def load_log_file(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def append_to_log_file(filepath, content):
    with open(filepath, 'a') as file:
        file.write(content + '\n')

def generate_text(prompt, length, log_file):
    words = prompt.split()
    selected_words = random.sample(words, 3)
    print(f"Selected words: {selected_words}")
    
    hashtag_prompt = f"Create a catchy slogan using these words: {', '.join(selected_words)}. Make it professional and engaging. Hashtag key words in the slogan."
    print(f"Hashtag prompt: {hashtag_prompt}")
    
    response = model.generate(hashtag_prompt, max_tokens=length).strip()
    print(f"Generated slogan: {response}")

    append_to_log_file(log_file, response)
    return response

def generate_hashtags(prompt, length, log_file):
    hashtag_prompt = f"Generate a single-word hashtag that effectively summarizes this text: {prompt}"
    print(f"Hashtag prompt: {hashtag_prompt}")
    
    response = model.generate(hashtag_prompt, max_tokens=length).strip(",. #")
    print(f"Generated hashtag: #{response}")
    
    append_to_log_file(log_file, f"#{response}")
    return f"#{response}"