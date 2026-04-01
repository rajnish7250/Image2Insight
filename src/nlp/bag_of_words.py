from sklearn.feature_extraction.text import CountVectorizer

def generate_bow(text_list):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(text_list)
    return vectorizer.get_feature_names_out(), X.toarray()