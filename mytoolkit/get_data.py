import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def clean_text(text):
  # remove punctuation
  text =  ''.join([e for e in text if e not in string.punctuation])
  # convert to lower case
  # text = text.lower()
  # # remove numbers
  # text = ''.join(word for word in text if not word.isdigit())
  # # remove stop words
  # stop_words = set(stopwords.words('english'))
  # word_tokens = word_tokenize(text)
  # text = [w for w in word_tokens if w not in stop_words]
  # # lemmatize
  # lemmatizer = WordNetLemmatizer()
  # text = ' '.join([lemmatizer.lemmatize(word) for word in text])
  return text




