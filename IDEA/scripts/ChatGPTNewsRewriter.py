"""
This script queries ChatGPT to rewrite news articles.
It also calculates readability statistics such that the original and rewritten versions can be compared in terms of text complexity.
"""
import openai, json, re
from datetime import datetime, timedelta
import readability
openai.api_key = 'add_your_api_key'

"""
Handling the input data
In theory, any json formatted data can serve as input. 
In this script, we use a recently scraped set of environmental news articles from the Guardian.
"""
filename = "data/guardian_environment_articles2023-10-16.json"
with open(filename, 'r') as file:
    data = json.load(file)
documents = []
for item in data:
    id = item["_id"]
    url = item["url"]
    title = item["title"]
    teaser = item["lead"]
    body = ""
    for b in item['body']:
        body += b['text'] + " "
    document = {"id": id, "url": url, "title": title, "teaser": teaser, "body": body}
    documents.append(document)

"""
Handling the ChatGPT request
"""
def generate_gpt3_response(user_text, print_output=False):
    completions = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',             # Determines the quality, speed, and cost.
        temperature=0.7,                  # Level of creativity in the response
        messages = [
            {"role": "system", "content": "You are an editor at an online newspaper and your job is to make articles comprehensible so that everyone can understand them."},
            {"role": "user", "content": user_text}
        ]
    )
    # Displaying the output can be helpful if things go wrong
    if print_output:
        print(completions)
    # Return the first choice's text
    return completions

"""
function to reformat text for readability score calculation
"""
def reformat_text(text):
    sentences = re.split(r'(?<=[.!?]) ', text)
    reformatted_text = ' \n'.join(sentences)
    return reformatted_text


"""
function to calculate readability scores
"""
def get_readability_scores(text):
    reformatted_text = reformat_text(text)
    results = readability.getmeasures(reformatted_text, lang='en')
    return results['readability grades']['FleschReadingEase'], results['readability grades']['GunningFogIndex']

"""
function to rewrite text with ChatGPT
"""
def rewrite_with_gpt(prompt, text):
    input_text = prompt + "Here is the text I want you to rewrite:" + text
    gpt_output = generate_gpt3_response(input_text)
    rewritten_text = gpt_output["choices"][0]["message"]["content"]
    return rewritten_text

"""
Defining the exact prompts for rewriting article headlines, teasers and text
"""
output_data = []
prompt_body = "I want you to act as an editor. I will provide you with article texts and your task is to rewrite them in a way that makes sure that a 10 year old can understand it. There are a couple things I would like you to do for this, including making shorter sentences and getting rid of jargon and complicated words wherever possible. Also, it is important that you keep the structure of the article somewhat similar to the original. Please also make sure that th enew version includes at least 5 facts from the original and that the new article is not dramatically longer or shorter than the original version."
prompt_title = "I want you to act as an editor. I will provide you with titles of news articles and your task is to rewrite them in a way that makes sure that a 10 year old can understand it. There are a couple things I would like you to do for this, including getting rid of jargon and complicated words wherever possible. Also, it is important that the new title is roughly as long as the original. Please also make sure that the new title contains the same information."
prompt_teaser = "I want you to act as an editor. I will provide you with teasers of news articles and your task is to rewrite them in a way that makes sure that a 10 year old can understand it. There are a couple things I would like you to do for this, including getting rid of jargon and complicated words wherever possible. Also, it is important that the new teaser is roughly as long as the original. Please also make sure that the new teaser contains the same information."

"""
Rewriting input data, calculating the readability scores and saving the output
"""
for doc in documents[:50]:
    id = doc['id']
    url = doc['url']
    original_title = doc['title']
    original_teaser = doc['teaser']
    original_text = doc['body']

    # rewrite article using ChatGPT with prompts defined above
    rewritten_title = rewrite_with_gpt(prompt_title, original_title)
    rewritten_teaser = rewrite_with_gpt(prompt_teaser, original_teaser)
    try:
        rewritten_text = rewrite_with_gpt(prompt_body, original_text)

    except:
        rewritten_text = "something went wrong here"

    # calculate readability measures for original article
    original_title_scores = get_readability_scores(original_title)
    original_teaser_scores = get_readability_scores(original_teaser)
    original_text_scores = get_readability_scores(original_text)

    # calculate readability measures for rewritten article
    rewritten_title_scores = get_readability_scores(rewritten_title)
    rewritten_teaser_scores = get_readability_scores(rewritten_teaser)
    rewritten_text_scores = get_readability_scores(rewritten_text)

    # save all input, putput and readability scores in a dictionary
    article_info = {
        "id": id,
        "url": url,
        "original_title": {
            "text": original_title,
            "readability_scores": dict(zip(["FleschReadingEase", "GunningFogIndex"], original_title_scores))
        },
        "rewritten_title": {
            "text": rewritten_title,
            "readability_scores": dict(zip(["FleschReadingEase", "GunningFogIndex"], rewritten_title_scores))
        },
        "original_teaser": {
            "text": original_teaser,
            "readability_scores": dict(zip(["FleschReadingEase", "GunningFogIndex"], original_teaser_scores))
        },
        "rewritten_teaser": {
            "text": rewritten_teaser,
            "readability_scores": dict(zip(["FleschReadingEase", "GunningFogIndex"], rewritten_teaser_scores))
        },
        "original_text": {
            "text": original_text,
            "readability_scores": dict(zip(["FleschReadingEase", "GunningFogIndex"], original_text_scores))
        },
        "rewritten_text": {
            "text": rewritten_text,
            "readability_scores": dict(zip(["FleschReadingEase", "GunningFogIndex"], rewritten_text_scores))
        }
    }

    output_data.append(article_info)

    # Save the output data to a JSON file
    output_filename = "data/output_articles.json"
    
    with open(output_filename, 'w') as output_file:
        json.dump(output_data, output_file, indent=4)

    print(f"Output data saved to {output_filename}")
