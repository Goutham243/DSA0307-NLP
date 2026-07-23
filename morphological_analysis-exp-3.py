import nltk
from nltk.stem import WordNetLemmatizer

# Download WordNet (only first time)
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

sentence = input("Enter a sentence: ")
words = sentence.split()

print("\nOriginal Words:")
print(words)

print("\nLemmatized Words:")
for word in words:
    print(lemmatizer.lemmatize(word))
