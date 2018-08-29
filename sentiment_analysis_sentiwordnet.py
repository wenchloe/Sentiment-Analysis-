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

# Gets the top 20 words (with frequency of the word) from an array of all the words in the initial text 
import operator 
def get_top_20_words(list_of_words):
    word_dict = {}
    for word in list_of_words:
        if not word in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    word_dict = sorted(word_dict.items(), key = operator.itemgetter(1), reverse = True)
    top_20 = []
    for word in word_dict:
        if len(top_20) < 20:
            top_20.append(word)
    return top_20
            
# Cleans the text (basic cleaning, see README), creates a vector with each row being a list of the top 20 words and its frequency
import re 
from nltk.corpus import stopwords
X_top20 = []
for i in range(0, len(X)):
    article = re.sub('[^a-zA-Z]', ' ', X[i])
    article = article.lower()
    article = article.split()
    article = [word for word in article if not word in set(stopwords.words('english'))]
    top_20 = get_top_20_words(article)
    X_top20.append(top_20)
    
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
y = [0] * len(X_top20)
for i in range(0, len(X_top20)):
    total_pos_score = 0
    total_neg_score = 0
    article_wordset = X_top20[i]
    for wordset in article_wordset:
        word_tag_set = nltk.pos_tag(nltk.word_tokenize(wordset[0]))
        word = word_tag_set[0][0]
        word_tag = get_wordnet_pos(word_tag_set[0][1])
        if word_tag != -1:
            current_score = get_score(word, word_tag)
            total_pos_score += current_score[0] * wordset[1]
            total_neg_score += current_score[1] * wordset[1]
    y[i] = math.log(total_pos_score + 0.5) - math.log(total_neg_score + 0.5) 
        
            
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

    
    
    
    
    
    
    
    
    
    
    
