# import necessary libraries
import pandas as pd
import io
import random
import string  # to process standard python strings
import json

# read file
with open('chatbot.json', 'r',encoding='utf-8') as File:
    Data = File.read()

# parse file
JsonObject = json.loads(Data)


# Keyword Matching
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there",
                      "hello", "I am glad! You are talking to me"]


def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# Generating response
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


def bot_response(user_response):
    if user_response not in JsonObject.keys():
        print("Not In")
        return json.dumps(user_response, separators=(',', ':'))
    return json.dumps(JsonObject[user_response], separators=(',', ':'))
