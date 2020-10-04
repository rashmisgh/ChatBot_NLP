# import necessary libraries
import numpy
import pandas as pd
import io
import random
import string  # to process standard python strings
import json

import math
import re
from collections import Counter

WORD = re.compile(r"\w+")

# import tflearn
# import tensorflow

# read file
with open('Chatbot.json', 'r') as File:
    Data = File.read()

# parse file
JsonObject = json.loads(Data)


queries = []

def initQuery():
    for w in JsonObject.keys():
        queries.append(w)


initQuery()

# Rashmi Singh - Get Cosine - Similarity Vectore
def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

# Rashmi Singh  - Vector Generation from Text
def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)



# Keyword Matching
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there",
                      "hello", "I am glad! You are talking to me"]


def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# Generating response -  Rashmi Singh
def response(user_response):
    if user_response != '':
        if user_response.lower() != 'bye':
            if (user_response.lower() == 'thanks' or user_response.lower() == 'thank you'):
                return "You are welcome.."
            else:
                # return user_response
                if greeting(user_response.lower()) != None:
                    return greeting(user_response.lower())
                else:
                    result = bot_response(user_response)
                    return result
        else:
            return "Bye! take care.."

# Rashmi Singh - Response Function
def bot_response(user_response):
    hasFound = False
    FoundIndex = -1;
    MaxCosine = -1;
    for qIndex in range(len(queries)):
        CosVal = get_cosine(text_to_vector(user_response.lower()), text_to_vector(queries[qIndex].lower()))
        if CosVal > MaxCosine and CosVal != 0:
            MaxCosine = CosVal
            FoundIndex = qIndex
    if MaxCosine == -1:
        return json.dumps("Could Not Understand Question", separators=(',', ':'))
    return json.dumps(JsonObject[queries[FoundIndex]], separators=(',', ':'))

                        
 
