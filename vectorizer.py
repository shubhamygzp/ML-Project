def text_to_vector(text):
    words = text.lower().split()
    return {word: words.count(word) for word in set(words)}

def cosine_similarity(vec1, vec2):
    common_words = set(vec1.keys()) & set(vec2.keys())
    dot_product = sum(vec1[word] * vec2[word] for word in common_words)
    magnitude1 = sum(v ** 2 for v in vec1.values()) ** 0.5
    magnitude2 = sum(v ** 2 for v in vec2.values()) ** 0.5
    return dot_product / (magnitude1 * magnitude2) if magnitude1 and magnitude2 else 0
