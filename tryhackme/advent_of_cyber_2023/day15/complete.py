#!/usr/bin/env python3
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

#Read the email dataset.
data = pd.read_csv('emails_dataset.csv')
df = pd.DataFrame(data)

#Convert text to numbers.
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['Message'])

#Split the dataset for training and testing
y = df['Classification']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#Train the model
clf = MultinomialNB()
clf.fit(X_train, y_train)

#Evaluate the model's performance
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

#Add a simple test to the model
message = vectorizer.transform(["Today's Offer! Claim ur $150 worth of discount vouchers! Text YES to 85023 now! SavaMob, member offers mobile! T Cs 08717898035. $3.00 Sub. 16 . Unsbub reply X"])
prediction = clf.predict(message)
print("The email is: ", prediction[0])

#Run the complete test of the emails inside "test_emails.csv"
test_data = pd.read_csv("test_emails.csv")

X_new = vectorizer.transform(test_data['Messages'])
new_predictions = clf.predict(X_new)
results_df = pd.DataFrame({'Messages': test_data['Messages'], 'Prediction': new_predictions})
print(results_df)
