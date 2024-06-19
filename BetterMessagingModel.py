import ollama

# Modelfile of the new model
# FROM llama3 (existing llm)(Base of your new model)
# For modelfile use ''' '''
# Inside the modelfile use """ """
# Replace YOUR GGUF FILE PATH with your gguf file path

modelfile = '''
FROM YOUR GGUF FILE PATH

TEMPLATE """
<|im_start|>system
{{ .System }}
<|im_end|>
<|im_start|>User
{{ .Prompt }}
<|im_end|>
<|im_start|>Shelly
"""

PARAMETER temperature 1
PARAMETER stop <|im_start|>
PARAMETER stop <|im_end|>

SYSTEM """
You are a girl named Shelly, You like chocolates and you like to do sports.
You are very shy and not very talkative.
"""
'''


def messageShelly(prompt):
    # Make a new model using siliconmaid
    ollama.create(model="Shelly", modelfile=modelfile)

    # Get Shelly, put in the prompt and ask Shelly about the promt
    response = (ollama.generate(model="Shelly",prompt=prompt))['response'] 

    return response



while True:
    print(messageShelly(input("User:")))
