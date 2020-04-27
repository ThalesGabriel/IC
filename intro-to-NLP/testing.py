import nltk
import re
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet

def compare_stemmer_and_lemmatizer(stemmer, lemmatizer, word, pos):
    """
    Print the results of stemmind and lemmitization using the passed stemmer, lemmatizer, word and pos (part of speech)
    """
    print("Stemmer:", stemmer.stem(word))
    print("Lemmatizer:", lemmatizer.lemmatize(word, pos))
    print()

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()


text = "Jornal Nacional revelou troca de mensagens entre presidente e ministro, na qual Bolsonaro pede interferência na investigação de deputados aliados. Em outro diálogo, deputada Carla Zambelli sugere ao ex-ministro aceitar demissão de diretor da PF em troca de vaga no STF. Ele recusa."
sentences = nltk.sent_tokenize(text)

bagOfWords = []
for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    bagOfWords += words

stop_words = set(stopwords.words("portuguese"))

summary = ""
for word in bagOfWords:
    if word not in stop_words:
        summary += word + " "

pattern = r"[^\w]"
print(text)
print()
print(summary)
print()
print(re.sub(pattern, " ", summary).replace("  ", ""))