import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

# Зчитати текст з файлу
with open('Sick story.txt', 'r', encoding='utf-8') as file:
    original_text = file.read()

# Токенізація
tokens = word_tokenize(original_text)

# Лемматизація та стеммінг
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
stemmed_tokens = [stemmer.stem(token) for token in tokens]

# Видалення стоп-слів
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in lemmatized_tokens if token.lower() not in stop_words]

# Видалення пунктуації
filtered_tokens = [token for token in filtered_tokens if token not in string.punctuation]

# Запис обробленого тексту у новий файл
processed_text = ' '.join(filtered_tokens)
with open('Reworked file.txt', 'w', encoding='utf-8') as file:
    file.write(processed_text)
