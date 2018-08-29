# Sentiment-Analysis-
Based on the top 20 most frequent (non-stopword) words in a given text, assign a sentiment score calculated through the logit formula to each text. 

Description of Steps:
(Pre: if necessary, convert .xls file to csv readable format, output will be in csv)
1. Create a vector of texts (can use pandas to get only one column containing the text)
2. Clean the texts (Note: Only the most basic format of cleaning is shown here with the following features:
    - retain only letters (ignore case of words, all converted to lower)
    - removing stopwords from nltk)
3. Get the 20 most common words in each text (see alternate version with alt...py for script that looks through all words) and the frequencies of each word in the text, which will impact the weight of the given word's sentiment score on the entire text's total score
4. Calculate the sentiment score using SentiWordNet of each of the top 20 words for each text and used the logit function (with 0.5 to avoid log(0)) to calculate the overall sentiment score. If the score is less than 0, then the text is negative. 
5. (optional) Sentiment scores are stored in a vector "y" and added to each row in the initial csv file 


Notes / Updates:
- Did NOT include stemming / lemmatization in the cleaning portion of the data
- The sentiment score seems to err on the positive end rather than the negative 

Next Steps:
- Using Vader as the Sentiment Analysis tool, comparing its accuracy to SentiWordnet 
- Exploring better ways of cleaning the data to extract more relevant terms 
- Using different functions to calculate overall sentiment score
- Estimating accuracy of this analysis on various datasets 
