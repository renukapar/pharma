#from sklearn.feature_extraction.text import CountVectorizer
documents = ["This is the first document.",
              "This document is the second document.",
              "And this is the third one.",
              "Is this the first document?"]
 
#vectorizer = CountVectorizer()
# X = vectorizer.fit_transform(documents)
# feature_names = vectorizer.get_feature_names_out()
#
# print("Bag-of-Words Matrix:")
# print(X.toarray())
# print("Vocabulary (Feature Names):", feature_names)

# skipgram_model = Word2Vec(sentences=[tokenized_corpus],
#                           vector_size=100,  # Dimensionality of the word vectors
#                           window=5,  # Maximum distance between the current and predicted word within a sentence
#                           sg=1,  # Skip-Gram model (1 for Skip-Gram, 0 for CBOW)
#                           min_count=1,  # Ignores all words with a total frequency lower than this
#                           workers=4)  # Number of CPU cores to use for training the model
