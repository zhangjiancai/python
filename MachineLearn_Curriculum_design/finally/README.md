# Sentiment-Analysis-using-Python

One of the applications of text mining is sentiment analysis. Most of the data is getting 
generated in textual format and in the past few years. Improvement is a continuous process and 
many product-based companies leverage these text mining techniques to examine the 
sentiments of the customers to find about what they can improve in the product. This 
information also helps them to understand the trend and demand of the end user which results 
in Customer satisfaction.

As text mining is a vast concept, the article is divided into two subchapters. The main 
focus of this article will be calculating two scores: sentiment polarity and subjectivity using 
python. The range of polarity is from -1 to 1(negative to positive) and will tell us if the text 
contains positive or negative feedback. Most companies prefer to stop their analysis here but in 
our second article, we will try to extend our analysis by creating some labels out of these scores.

# Data Preprocessing
In the above-given problem statement we have performed various pre-processing steps 
on the dataset that mainly dealt with removing stopwords, removing emojis. The text document 
is then converted into the lowercase for better generalization.
Subsequently, the punctuations were cleaned and removed thereby reducing the 
unnecessary noise from the dataset. After that, we have also removed the repeating characters 
from the words along with removing the URLs as they do not have any significant importance.
At last, we then performed Stemming (reducing the words to their derived stems) and 
Lemmatization (reducing the derived words to their root form known as lemma) for better 
results.
# Data Cleaning process
1.Making statement text in lower case.

2.Cleaning and removing the above stop words list from the text
## Removing punctuation, numbers and special characters
This will replace everything except characters and hashtags with spaces. "[^a-zA-Z#]" 
this regular expression means everything except alphabets and hashtags.

3.Cleaning and removing punctuations

4.Cleaning and removing repeating characters

5.Cleaning and removing URL’s

6.Cleaning and removing Numeric numbers

7.Remove short words
We remove those words which are of little or no use. So, we will select the length of 
words which we want to remove

## Tokenization

Tokenization is a way to split the strings into a list of words. In this example you’ll use the 
Natural Language Toolkit which has built-in functions for tokenization. we can also use regex to 
tokenize it but it is a bit difficult. Though it gives you more control over our text

## Stemming

Stemming refers to the process of normalization, where we reduce a word to its base 
stem, for example, “automate”, “automatic”, “automation,” “automations” will be reduced to 
“automat” such that all these forms refer to automat

## Lemmatization

Lemmatization on the other hand usually refers to doing things properly with the use of 
a vocabulary and morphological analysis, normally aiming to remove inflectional endings only 
and to return the dictionary form of a word.

## Subjectivity and Polarity
The two measures that are used to analyze the sentiment are:

• Polarity – talks about how positive or negative the opinion is

• Subjectivity – talks about how subjective the opinion is

TextBlob(text).sentiment gives us the Polarity, Subjectivity values.
Polarity ranges from -1 to 1 (1 is more positive, 0 is neutral, -1 is more negative)
Subjectivity ranges from 0 to 1(0 being very objective and 1 being very subjective

## Data Exploration
Let's form a WordCloud
A wordcloud is a visualization wherein the most frequent words appear in large size and 
the less frequent words appear in smaller sizes.
