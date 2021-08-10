import hazm

str = 'سینا 541 دارو های فروختنی تر'
lemmatizer = hazm.Lemmatizer()
# for each in str.split(' '):
result = lemmatizer.lemmatize(str)
print(result)
