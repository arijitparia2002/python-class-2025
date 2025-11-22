from transformers import pipeline
 # Create text generator
generator = pipeline("text-generation", model="gpt2")
 # Generate text
prompt = "Artificial Intelligence is"
result = generator(prompt, max_length=5, num_return_sequences=1)
print(result[0]['generated_text'])