import gpt4all

def generate_text(prompt, length):
    gpt = gpt4all.GPT4All(model="orca-mini-3b-gguf2-q4_0.gguf")
    response = gpt.generate(prompt, max_length=length)
    return response

def generate_hashtags(prompt, length=5):
    gpt = gpt4all.GPT4All(model="orca-mini-3b-gguf2-q4_0.gguf")
    response = gpt.generate(prompt, max_length=length)
    hashtags = response.split()
    return ' '.join([f'#{tag.strip(",. ")}' for tag in hashtags if tag.strip(",. ")])