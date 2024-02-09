from transformers import pipeline


ner = pipeline('ner', grouped_entities=True)
result = ner('I\'m Haidun, a student at NSCC. I live in Halifax. I study at NSCC. I am from China')
print(result)