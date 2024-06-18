# pip install ollama termcolor

import ollama
from time import time # for counting time it takes to generate
from termcolor import colored # make it look nicer


modelfile = '''
FROM llama3
SYSTEM """You are a helpful yet rude assisstant
Your name is Shelly and you are very RUDE
You reply in short phrases"""
''' # from llama3 model, make a new model with this modelfile
# use """ """ in system to expand the lines of your system
# put the personality/backstory of the character in system


ollama.create(model="Shelly", modelfile=modelfile) # create new model as shelly
# this model will be available in terminal as well
# Warning, it will override existing models with the same name

while True: #start loop
    prompt = input("User: ")
    start = time()
    response = ollama.chat(model="Shelly", messages=[ # Get Shelly as model
        {
            'role':'user', # from user
            'content':prompt, # prompt message
        }
    ]) 
    print(colored(str(round(time()-start)), "red")) # round up (current time - starting time)
    print(colored(response['message']['content'], "light_blue"))

# This model will have no memory
# Good enough for terminal custom conversation
