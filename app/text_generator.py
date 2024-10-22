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
    # Assume each word is on a new line in the text file
    words = prompt.splitlines()
    
    # Ensure we have at least 3 words
    if len(words) == 1:
        selected_words = words * 3
    elif len(words) == 2:
        selected_words = words + words[:1]
    else:
        selected_words = random.sample(words, 3)
    
    print(f"Selected words: {selected_words}")
    
    # Adding randomness to the prompt
    random_number = random.randint(1, 10000)
    slogan_prompt = f"Create a catchy slogan using these words: {', '.join(selected_words)}. Make it professional and engaging. Random number: {random_number}\nSlogan:"
    print(f"Slogan prompt: {slogan_prompt}")
    
    response = model.generate(slogan_prompt, max_tokens=length).strip()
    print(f"Generated slogan: {response}")

    # Follow-up query to hashtag key words
    hashtag_prompt = f"Hashtag key words in this slogan: {response}\nHashtagged slogan:"
    print(f"Hashtag prompt: {hashtag_prompt}")
    
    hashtagged_response = model.generate(hashtag_prompt, max_tokens=length).strip()
    print(f"Hashtagged slogan: {hashtagged_response}")

    append_to_log_file(log_file, hashtagged_response)
    return hashtagged_response

def generate_hashtags(prompt, length, log_file):
    hashtag_prompt = f"Generate a single-word summary for this text: {prompt}\nSummary:"
    print(f"Hashtag prompt: {hashtag_prompt}")
    
    response = model.generate(hashtag_prompt, max_tokens=length).strip(",. #")
    print(f"Generated hashtag: #{response}")
    
    append_to_log_file(log_file, f"#{response}")
    return f"#{response}"