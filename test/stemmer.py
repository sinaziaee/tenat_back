from nltk import stem

# str = '4 Chapter 1 Computer Abstractions and Technology'
str = 'Abstractions'

# stemmer = stem.SnowballStemmer(language='english')
stemmer = stem.PorterStemmer()

result = stemmer.stem(str)

print(result)

