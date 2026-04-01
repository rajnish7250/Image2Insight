def create_bigrams(word):
    return [word[i:i+2] for i in range(len(word)-1)]

def similarity(w1, w2):
    b1, b2 = create_bigrams(w1), create_bigrams(w2)
    common = set(b1) & set(b2)
    return len(common) / max(len(b1), len(b2)) if max(len(b1), len(b2)) else 0

def autocorrect(word, dictionary, threshold=0.5):
    best_word = word
    max_score = 0

    for dict_word in dictionary:
        score = similarity(word, dict_word)
        if score > max_score:
            max_score = score
            best_word = dict_word

    return best_word if max_score > threshold else word