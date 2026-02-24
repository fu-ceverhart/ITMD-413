sentences = []
for i in range(5):
    sentence = input("Enter a sentence: ")
    sentences.append(sentence)
with open('data.txt', 'w') as f:
    for sentence in sentences:
        f.write(sentence + '\n')