from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize("good", pos = "a")
# output : "good"
lemmatizer.lemmatize("excellent", pos = "n")
# output : "excellent"
lemmatizer.lemmatize("painting", pos = "v")
# output : "pain"
lemmatizer.lemmatize("painting", pos = "n")
# output : "painting"
