from transformers import pipeline
 # This will download a small model (first time only)
model = pipeline("sentiment-analysis")
result = model("It's okay")
print(result)
