from transformers import pipeline

ner = pipeline('ner', grouped_entities=True)
result = ner('I\'m Haidun, I study at NSCC AI, I live in Halifax, Canada')
print(result)