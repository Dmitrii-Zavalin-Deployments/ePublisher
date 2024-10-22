from gpt4all import GPT4All

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
    paraphrase_prompt = f"Make paraphrased short slogan from this text with the same meaning, proper punctuation, and make it catchy and engaging: {prompt}\nParaphrased text:"
    existing_texts = load_log_file(log_file)
    response = model.generate(paraphrase_prompt, max_tokens=length).strip()
    append_to_log_file(log_file, response)
    return response

def generate_hashtags(prompt, length, log_file):
    hashtag_prompt = f"Generate a single-word summary for this text: {prompt}\nSummary:"
    existing_hashtags = load_log_file(log_file)
    response = model.generate(hashtag_prompt, max_tokens=length).strip(",. #")
    hashtag = f'#{response}'
    append_to_log_file(log_file, hashtag)
    return hashtag