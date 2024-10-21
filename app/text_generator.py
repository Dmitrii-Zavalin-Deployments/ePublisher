from gpt4all import GPT4All

# Initialize the GPT-4All model with a valid model name
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

def generate_text(prompt, length):
    paraphrase_prompt = f"Paraphrase this text with the same meaning, proper punctuation, and make it catchy and engaging: {prompt}\nParaphrased text:"
    response = model.generate(paraphrase_prompt, max_tokens=length)
    return response.strip()

def generate_hashtags(prompt, length=5):
    hashtag_prompt = f"Generate a single-word hashtag for this text without the '#' symbol and ensure it is a real word: {prompt}\nHashtag:"
    response = model.generate(hashtag_prompt, max_tokens=length)
    hashtag = response.strip(",. #")
    return f'{hashtag}'
