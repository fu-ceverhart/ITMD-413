counts ={}
with open('data.txt', 'r') as f:
    sentences = f.readlines()
    for sentence in sentences:
        for i in sentence:
            for vowel in ('a', 'e', 'i', 'o', 'u'):
                if i.lower() == vowel:
                    counts[vowel] = counts.get(vowel, 0) + 1
print(counts)