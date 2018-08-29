# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# (optional) Converting .xls file to .csv 
inputf_path = '' 
df = pd.read_excel(inputf_path, encoding='utf-16')
df.to_csv(inputf_path, encoding='utf-16')

# Importing the dataset
text_col_num = 
X = df.iloc[:, text_col_num].values 
            
# Cleans the text (basic, see README)
import re 
import nltk
from nltk.corpus import stopwords
for i in range(0, len(X)):
    text = re.sub('[^a-zA-Z]', ' ', X[i])
    text = text.lower()
    text = text.split()
    text = [word for word in text if not word in set(stopwords.words('english'))]
    text = ' '.join(text) 
    X[i] = text
    
# Converting the part-of-speech tag to a WordNet tag 
from nltk.corpus import wordnet
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return 'a'
    elif tag.startswith('V'):
        return 'v'
    elif tag.startswith('N'):
        return 'n'
    elif tag.startswith('R'):
        return 'r'
    else:
        return -1

# Check if the word is in the set of lemmas
wn_lemmas = set(wordnet.all_lemma_names())
def is_lemma(word):
    if word in wn_lemmas:
        return True
    else:
        return False

# Get the total score for each 
def get_score(word, tag):
    pos_score = 0
    neg_score = 0
    num_scores = 0
    synsets = wordnet.synsets(word, pos = tag)
    synset_num = 0
    for synset in synsets:
        if synset_num < 3:
            word_copy = swn.senti_synset(synset.name())
            pos = word_copy.pos_score()
            neg = word_copy.neg_score()
            pos_score += pos
            neg_score += neg
            num_scores += 1
            synset_num += 1
    return [pos_score / num_scores, neg_score / num_scores] if not num_scores == 0 else [0, 0]    

# Perform Sentiment Analysis based on the logit function 
import math 
from nltk.corpus import sentiwordnet as swn
y = [0] * len(X)
for i in range(0, len(X)):
    article = nltk.pos_tag(nltk.word_tokenize(X[i]))
    pos_score = 0
    neg_score = 0
    for j in range(0, len(article)):
        word = article[j][0]
        if is_lemma(word):
            tag = get_wordnet_pos(article[j][1])
            if tag != -1:
                current_score = get_score(word, tag)
                pos_score += current_score[0]
                neg_score += current_score[1]
    y[i] = math.log(pos_score + 0.5) - math.log(neg_score + 0.5)
        
            
# Write the sentiment score to an output CSV file 
import csv
inputf_csv_path = ''
outputf_path = ''
with open(inputf_csv_path, 'r', encoding='utf-16') as csv_input:
    with open(outputf_path, 'w') as csv_output:
        writer = csv.writer(csv_output)
        index = 0
        for row in csv.reader(csv_input):
            if index < len(y):
                writer.writerow(len(row) + [y[index]])
                index += 1

    
    
    
    
    
    
    
    
    
    
    
