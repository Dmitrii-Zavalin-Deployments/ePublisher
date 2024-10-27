from gpt4all import GPT4All
from keybert import KeyBERT
import random
import string

# Initialize the GPT-4All model and KeyBERT
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
kw_model = KeyBERT()

def load_log_file(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def append_to_log_file(filepath, content):
    with open(filepath, 'a') as file:
        file.write(content + '\n')

def extract_keywords(text):
    try:
        keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=5)
        return [keyword[0] for keyword in keywords]
    except AttributeError:
        # Handling different versions of CountVectorizer
        from sklearn.feature_extraction.text import CountVectorizer
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform([text])
        feature_names = vectorizer.get_feature_names_out()  # Updated method
        return list(feature_names)[:5]  # Ensure we return top 5 to maintain consistency

def hashtag_word(word, keywords):
    stripped_word = word.strip(string.punctuation)
    if any(keyword in stripped_word.lower() for keyword in [k.lower() for k in keywords]):
        punct_before = ''.join(c for c in word if c in string.punctuation and word.index(c) < len(stripped_word))
        punct_after = ''.join(c for c in word if c in string.punctuation and word.index(c) >= len(stripped_word))
        return f"{punct_before}#{stripped_word}{punct_after}"
    return word

def is_appropriate_topic(text, link_sentence):
    text_to_refine = link_sentence + " " + text
    query = f"Does the text: {link_sentence} logically continue the text: {text}? Answer only with 'yes' or 'no'.\nResponse:"
    print(f"First censorship query: {query}")
    first_response = model.generate(query).strip().lower()
    print(f"GPT-4All censorship first check response: {first_response}")
    
    first_word = first_response.split()[0] if first_response else ""
    print(f"First word: {first_word}")
    
    if first_word == "yes":
        print("Calling the second censorship check.")
        query = f"Is the topic of the following text political, offensive, insulting, violent, abusive, negative, unclear, irrelevant, nonsensical, inappropriate, misleading, boastful, self-promotional, or confusing? Answer only with 'yes' or 'no': {text}?\nResponse:"
        print(f"Second censorship query: {query}")
        second_response = model.generate(query).strip().lower()
        print(f"GPT-4All censorship check response: {second_response}")
        second_word = second_response.split()[0] if second_response else ""
        print(f"Second word: {second_word}")
        return second_word == "no"
    else:
        return False

def generate_text(prompt, length, log_file, link_sentence):
    words = prompt.splitlines()
    if len(words) == 1:
        selected_words = words * 3
    elif len(words) == 2:
        selected_words = words + words[:1]
    else:
        selected_words = random.sample(words, 3)
  
    print(f"Selected words: {selected_words}")

    random_number = random.randint(1, 10000000)
    slogan_prompt = f"{random_number}. Create a catchy, professional, appropriate, polite, clear and engaging complete sentence slogan using these words: {', '.join(selected_words)}.\nSlogan:"
    print(f"Slogan prompt: {slogan_prompt}")

    response = model.generate(slogan_prompt, max_tokens=length).strip()
    print(f"Generated slogan: {response}")

    # Remove surrounding quotes and dashes
    response = response.strip('"').strip("'").strip('-')
    print(f"Cleaned slogan: {response}")

    for attempt in range(10):
        complete_sentence_prompt = f"Proofread this text to make a sentence: {response} \nSentence:"
        complete_sentence_text = model.generate(complete_sentence_prompt, max_tokens=length).strip()
        print(f"Attempt {attempt + 1}: Complete sentence: {complete_sentence_text}")

        # Check if the complete sentence ends with proper punctuation and is appropriate
        if complete_sentence_text[-1] in '.!?' and is_appropriate_topic(complete_sentence_text, link_sentence):
            # Log before capitalization
            print(f"Complete sentence before capitalization: {complete_sentence_text}")
            # Capitalize only the first letter of the first word
            complete_sentence_text = complete_sentence_text[0].capitalize() + complete_sentence_text[1:]
            print(f"Complete sentence after capitalization: {complete_sentence_text}")
            # Extract key words and hashtag them
            keywords = extract_keywords(complete_sentence_text)
            print(f"Extracted keywords: {keywords}")
            hashtagged_response = ' '.join([hashtag_word(word, keywords) for word in complete_sentence_text.split()])
            break
    else:
        # If no proper complete sentence is formed after 10 attempts
        keywords = extract_keywords(response)
        print(f"Extracted keywords after 10 attempts: {keywords}")
        hashtagged_response = ' '.join([hashtag_word(word, keywords) for word in keywords])
        
    print(f"Hashtagged slogan: {hashtagged_response}")
    append_to_log_file(log_file, hashtagged_response)
    return hashtagged_response


