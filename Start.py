import ollama

# Modelfile of the new model
# FROM llama3 (existing llm)(Base of your new model)
# For modelfile use ''' '''
# Inside the modelfile use """ """

modelfile = '''
FROM llama3
SYSTEM """
You are a girl named Shelly, You like chocolates and you like to do sports.
You are very shy and not very talkative.
"""
'''




# Make a new model using llama3
ollama.create(model="Shelly", modelfile=modelfile)

# Get llama3, put in the prompt and ask llama3 about the promt
response = (ollama.generate(model="Shelly",prompt="why is the sky red?"))['response'] # Use Shelly model instead of llama3

#print output
print(response)

