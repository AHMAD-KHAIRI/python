import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Function to read emails from a directory
def read_emails(directory_path, label):
    data = []
    for filename in os.listdir(directory_path):
        with open(os.path.join(directory_path, filename), mode='r', encoding='latin1') as file:
            content = file.read()
            data.append({'message': content, 'class': label, 'filename': filename})
    return data

# Function to create a DataFrame from a list of emails
def create_dataframe(directory_path, label):
    emails_data = read_emails(directory_path, label)
    return pd.DataFrame(emails_data)

# Paths to spam and ham (normal) email directories
spam_path = "C:/Users/ahmad/OneDrive/Documents/Machine Learning Course/MLCourse/emails/spam"
normal_path = "C:/Users/ahmad/OneDrive/Documents/Machine Learning Course/MLCourse/emails/ham"

# Create DataFrames for spam and normal emails
spam_df = create_dataframe(spam_path, 'spam')
normal_df = create_dataframe(normal_path, 'normal')

# Combine DataFrames into one
data = pd.concat([spam_df, normal_df])

# Vectorize the email messages
vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(data['message'].values)

# Train a Naive Bayes classifier
classifier = MultinomialNB()
targets = data['class'].values
classifier.fit(counts, targets)

# Examples to classify
examples = ['Free Viagra now!!!', "Hi Bob, how about a game of golf tomorrow?"]

# Vectorize the examples
example_counts = vectorizer.transform(examples)

# Predict using the trained classifier
predictions = classifier.predict(example_counts)

# Print the predictions
for example, prediction in zip(examples, predictions):
    print(f"Example: '{example}' is predicted as '{prediction}'")

print(tuple(zip(examples, predictions)))



# # ===================================== STEP-BY-STEP EXPLANATION OF CODE =================================================
# # 
# # 1. Explanation of: "os.listdir(directory_path)""

# # os.listdir(path='.'): Return a list containing the names of the entries in the directory given by path. The list is in arbitrary order, and does not include the special entries '.' and '..' even if they are present in the directory. If a file is removed from or added to the directory during the call of this function, whether a name for that file be included is unspecified.

# # Example:
# import os

# # path = "C:/Users/ahmad/OneDrive/Documents/Code/python"
# normal_path = "C:/Users/ahmad/OneDrive/Documents/Machine Learning Course/MLCourse/emails/ham"
# spam_path = "C:/Users/ahmad/OneDrive/Documents/Machine Learning Course/MLCourse/emails/spam"

# # print(os.listdir(path))
# # print(len(os.listdir(path)))

# normal_email_directory = os.listdir(normal_path)
# spam_email_directory = os.listdir(spam_path)

# print(normal_email_directory[0]) # '00001.7c53336b37003a9286aba55d2945844c'
# print(len(normal_email_directory))

# print(spam_email_directory[0]) # 00001.7848dde101aa985090474a91ec93fcf0
# print(len(spam_email_directory))

# # 2. Explanation of: "os.path.join(directory_path, filename)""

# # os.path.join(path, *paths): Join one or more path segments intelligently. The return value is the concatenation of path and all members of *paths, with exactly one directory separator following each non-empty part, except the last. That is, the result will only end in a separator if the last part is either empty or ends in a separator. If a segment is an absolute path (which on Windows requires both a drive and a root), then all previous segments are ignored and joining continues from the absolute path segment.

# first_filename_in_normal_dir = os.path.join(normal_path, normal_email_directory[0])
# print(first_filename_in_normal_dir)

# first_filename_in_spam_dir = os.path.join(spam_path, spam_email_directory[0])
# print(first_filename_in_spam_dir)


# # 3. Explanation of: "with open(first_filename_in_directory, mode="r", encoding="latin1") as file:"

# # with open(file, mode, encoding): Open file and return a corresponding file object

# normal_email_data = [] # create an empty list
# with open(first_filename_in_normal_dir, mode="r", encoding="utf-8") as file:
#     content = file.read() # read the file and save it in the variable "content"
#     # print(content)
#     normal_email_data.append({'message': content, 'label': 'normal', 'filename': first_filename_in_normal_dir}) # create a dictionary inside a list
# print(normal_email_data)
# print(len(normal_email_data))
# # Accessing Dictionary Elements from a Python List of Dictionary:
# print(normal_email_data[0]["message"])
# print(normal_email_data[0]["label"])
# print(normal_email_data[0]["filename"])

# spam_email_data = [] # create an empty list
# with open(first_filename_in_spam_dir, mode="r", encoding="latin1") as file:
#     content = file.read() # read the file and save it in the variable "content"
#     # print(content)
#     spam_email_data.append({'message': content, 'label': 'spam', 'filename': first_filename_in_spam_dir}) # create a dictionary inside a list
# print(spam_email_data)
# print(len(spam_email_data))
# # Accessing Dictionary Elements from a Python List of Dictionary:
# print(spam_email_data[0]["message"])
# print(spam_email_data[0]["label"])
# print(spam_email_data[0]["filename"])


# # 4. Explanation of: "return pd.DataFrame(emails_data)" 

# # This line creates a DataFrame by passing a dictionary of objects where:
# # - the "keys" are the column label
# # - and the "values" are the column values

# import pandas as pd

# normal_df = pd.DataFrame(normal_email_data)
# spam_df = pd.DataFrame(spam_email_data)
# # print(normal_df.head())
# # print(spam_df.head())


# # 5. Explanation of: "data = pd.concat([spam_df, normal_df])"

# # Concatenate pandas objects along a particular axis. In this case, two DataFrames are concatenated

# data = pd.concat([spam_df, normal_df])
# print(data.head())

# # 6. Explanation of: "# vectorizer = CountVectorizer()"

# # sklearn.feature_extraction.text.CountVectorizer(): Convert a collection of text documents to a matrix of token counts.

# from sklearn.feature_extraction.text import CountVectorizer

# vectorizer = CountVectorizer()


# # 7. Explanation of : "counts = vectorizer.fit_transform(data['message'].values)"

# # fit_transform(raw_documents, y=None): Learn the vocabulary dictionary and return "document-term matrix".
# # the fit_transform method calculates the necessary parameters from the input data. 
# # In the case of vectorization, it learns the vocabulary from a collection of text documents
# # The fit_transform method is used during the training phase to learn the vocabulary and transform the training data. 

# # A document-term matrix is a mathematical matrix that describes the frequency of terms that occur in a each document in a collection. 
# # In a document-term matrix, rows correspond to documents in the collection and columns correspond to terms.

# counts = vectorizer.fit_transform(data['message'].values)

# # print(counts)
# # print(vectorizer.get_feature_names_out()) # get_feature_names_out([input_features]): Get output feature names for transformation.
# # print(counts.toarray())

# # Let's make a simple example to try to understand what's happening:
# # Assuming 'simple_data' is a list of text documents
# simple_data = ["This is an example.", 
#                "Another example.", 
#                "And yet another one."]

# # Use fit_transform to learn the vocabulary and transform the documents
# simple_counts = vectorizer.fit_transform(simple_data)
# print(simple_counts)
# # (i, j) k: This notation represents that in the i-th document, the j-th term has a frequency of k.
# # Document index 0: "This is an example."
# # Document index 1: "Another example."
# # Document index 2: "And yet another one."

# # output: 
# # (0, 6) 1  # In the first document (document index 0), the 6th term (word) has a frequency of 1.
# # (0, 4) 1  # In the first document, the 4th term has a frequency of 1.
# # (0, 0) 1  # In the first document, the 0th term has a frequency of 1.
# # (0, 3) 1  # In the first document, the 3rd term has a frequency of 1.

# # (1, 3) 1  # In the second document (document index 1), the 3rd term has a frequency of 1.
# # (1, 2) 1  # In the second document, the 2nd term has a frequency of 1.

# # (2, 2) 1  # In the third document (document index 2), the 2nd term has a frequency of 1.
# # (2, 1) 1  # In the third document, the 1st term has a frequency of 1.
# # (2, 7) 1  # In the third document, the 7th term has a frequency of 1.
# # (2, 5) 1  # In the third document, the 5th term has a frequency of 1.

# feature_names = vectorizer.get_feature_names_out() # get_feature_names_out([input_features]): Get output feature names for transformation.
# print(feature_names)
# # output: 
# # ['an' 'and' 'another' 'example' 'is' 'one' 'this' 'yet']

# print(feature_names[0]) # "an"
# print(feature_names[1]) # "and"
# print(feature_names[2]) # "another"
# print(feature_names[3]) # "example"
# print(feature_names[4]) # "is"
# print(feature_names[5]) # "one"
# print(feature_names[6]) # "this"
# print(feature_names[7]) # "yet"

# print(simple_counts.toarray())
# # output: 
# # [[1 0 0 1 1 0 1 0]
# #  [0 0 1 1 0 0 0 0]
# #  [0 1 1 0 0 1 0 1]]


# # bigram_vectorizer = CountVectorizer(ngram_range=(1, 2),token_pattern=r'\b\w+\b', min_df=1)
# # simple_counts_2 = bigram_vectorizer.fit_transform(simple_data)
# # feature_names_2 = bigram_vectorizer.get_feature_names_out()
# # print(simple_counts_2)
# # print(feature_names_2)
# # print(simple_counts_2.toarray())

# # ngram_vectorizer = CountVectorizer(analyzer="char_wb", ngram_range=(2, 2))
# # simple_counts_3 = ngram_vectorizer.fit_transform(simple_data)
# # feature_names_3 = ngram_vectorizer.get_feature_names_out()
# # print(simple_counts_3)
# # print(feature_names_3)
# # print(simple_counts_3.toarray())


# # 8. Explanation for:

# from sklearn.naive_bayes import MultinomialNB
# # Create an instance of MultinomialNB class from scikit-learn, initializing a Multinomial Naive Bayes classifier. 
# classifier = MultinomialNB()

# targets = data['label'].values # In Bayes' Theorem, this represents P(A)

# # The fit method is used to train the Multinomial Naive Bayes classifier.
# # - "counts" is the input data representing the features (word frequencies) which is the result of vectorizing using "CountVectorizer"
# # - "targets" is the data representing the class 
# classifier.fit(counts, targets) # In Bayes' Theorem, this represents P(B|A) 


# # 9. Explanation for:
# # Examples to classify
# examples = ['Free Viagra now!!!', "Hi Bob, how about a game of golf tomorrow?"]

# # Vectorize the examples
# # transform: This method is used when you have already trained the vectorizer (using fit_transform) and you want to apply the same transformation to new data. The vectorizer "remembers" the parameters it learned during training, and you can use transform on new data to apply the same transformation without re-computing those parameters.
# example_counts = vectorizer.transform(examples)

# # Predict using the trained classifier
# predictions = classifier.predict(example_counts) # In Bayes' Theorem, this represents P(A|B)


# # 10. Explanation for:
# # # Print the predictions
# # for example, prediction in zip(examples, predictions):
# #     print(f"Example: '{example}' is predicted as '{prediction}'")

# # The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.

# # syntax: zip(iterator1, iterator2, iterator3 ...) 
# # Example:
# a = ["A", "B", "C", "D"]
# b = ["1", "2", "3", "4"]
# zipped = zip(a, b)

# # use the tuple() function to display a readable version of the result:
# print(tuple(zipped))