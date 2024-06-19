# pip install ollama termcolor
# This model is better at generating roleplaying and natural texting
# It is best at following the System. So it can be used for other purposes as well
# Please change the file path to your own file path

import ollama
from time import time # for counting time it takes to generate
from termcolor import colored # make it look nicer


modelfile = '''
FROM "INSERT YOUR FILE PATH HERE"

TEMPLATE """
<|im_start|>system
{{ .System }}
<|im_end|>
<|im_start|>Lumi
{{ .Prompt }}
<|im_end|>
<|im_start|>Shelly
"""

PARAMETER temperature 1
PARAMETER stop <|im_start|>
PARAMETER stop <|im_end|>


SYSTEM """You are a chearful 20 year old girl
You like to use emojis
You are also very shy
"""
''' # from llama3 model, make a new model with this modelfile
# use """ """ in system to expand the lines of your system
# put the personality/backstory of the character in system

# " " are important for the file path

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
