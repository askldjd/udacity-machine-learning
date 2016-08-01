def stemString(input_string):
    from nltk.stem.snowball import SnowballStemmer
    stemmer = SnowballStemmer("english")

    tokens = input_string.split()
    singles = [stemmer.stem(token) for token in tokens]
    stemmed_string =  ' '.join(singles)

    return stemmed_string

test_string = "Still looking for Pokemon all over the street. When is Niantic fixing that stupid three step bug?"
print(stemString(test_string))