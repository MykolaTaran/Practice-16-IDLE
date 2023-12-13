import nltk

# Download the Punkt resource
nltk.download('punkt')

# Continue with the rest of your code
from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
import string

# Наявний код
file_id = 'whitman-leaves.txt'
file_content = gutenberg.raw(file_id)

# Токенізація слів
words = word_tokenize(file_content)

# Визначення кількості слів
word_count = len(words)
print(f"Кількість слів у тексті: {word_count}")

# Визначення 10 найбільш вживаних слів та побудова стовпчастої діаграми
word_freq = Counter(words)
top_words = word_freq.most_common(10)

# Відокремлення слів та їх частоти
top_words, freq = zip(*top_words)

# Побудова стовпчастої діаграми
plt.figure(figsize=(10, 5))
plt.bar(top_words, freq, color='skyblue')
plt.title('10 найбільш вживаних слів у тексті')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.show()

# Видалення стоп-слів та пунктуації
stop_words = set(stopwords.words('english'))
filtered_words = [word.lower() for word in words if word.lower() not in stop_words and word not in string.punctuation]

# Визначення 10 найбільш вживаних слів після очищення та побудова стовпчастої діаграми
filtered_word_freq = Counter(filtered_words)
top_filtered_words = filtered_word_freq.most_common(10)

# Відокремлення слів та їх частоти
top_filtered_words, freq_filtered = zip(*top_filtered_words)

# Побудова стовпчастої діаграми після очищення
plt.figure(figsize=(10, 5))
plt.bar(top_filtered_words, freq_filtered, color='salmon')
plt.title('10 найбільш вживаних слів після очищення тексту')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.show()
