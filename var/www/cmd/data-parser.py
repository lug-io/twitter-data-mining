#!/usr/bin/python
import sys
import json
import pandas as pd
import matplotlib.pyplot as plt
import re # Regular Expression
from matplotlib import rcParams

## Use system to parse command line arguments
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

# Path to image output directory
input_directory = '/var/www/html/content/data/'
output_directory = '/var/www/html/content/graphs/'

# Set matplot settings
rcParams.update({'figure.autolayout': True})
#plt.gcf().subplots_adjust(bottom=0.15) # gcf -> GetCurrentFigure
#plt.gca().tight_layout() # gca -> GetCurrentAxis

# Set target file
tweets_data_path = input_directory + '1-24-2016.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
	try:
		tweet = json.loads(line)
		tweets_data.append(tweet)
	except:
		continue

## Total # of tweets captured
print len(tweets_data)

## New Panda DataFrame
tweets = pd.DataFrame()

## Populate/map DataFrame with data
tweets['text']		= map(lambda tweet: tweet['text'], tweets_data)
tweets['lang']		= map(lambda tweet: tweet['lang'], tweets_data)
tweets['country']	= map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

## Chart for top 5 languages
tweets_by_lang = tweets['lang'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Top 5 Languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')

fig.savefig(output_directory + 'top-5-languageszz.png')

## Chart for top 5 countries
tweets_by_country = tweets['country'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Top 5 Countries', fontsize=15, fontweight='bold')
tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')

fig.savefig(output_directory + 'top-5-countrieszz.png')

# Returns true if "word" is in "text"
def word_in_text(word, text):
	word = word.lower()
	text = text.lower()
	match = re.search(word, text)
	if match:
		return True
	return False

# Add columns to our tweets DataFrame
tweets['python']     	= tweets['text'].apply(lambda tweet: word_in_text('python', tweet))
tweets['javascript'] 	= tweets['text'].apply(lambda tweet: word_in_text('javascript', tweet))
tweets['ruby']			= tweets['text'].apply(lambda tweet: word_in_text('ruby', tweet))
tweets['csharp']		= tweets['text'].apply(lambda tweet: word_in_text('csharp', tweet))
tweets['fsharp']		= tweets['text'].apply(lambda tweet: word_in_text('fsharp', tweet))

## Calculate # of tweets for each language
print tweets['python'].value_counts()[True]
print tweets['javascript'].value_counts()[True]
print tweets['ruby'].value_counts()[True]
print tweets['csharp'].value_counts()[True]
print tweets['fsharp'].value_counts()[True]

## Create a simple comparison chart
prg_langs = ['python', 'javascript', 'ruby', 'csharp', 'fsharp']
tweets_by_prg_lang = [	tweets['python'].value_counts()[True],
						tweets['javascript'].value_counts()[True],
						tweets['ruby'].value_counts()[True],
						tweets['csharp'].value_counts()[True],
						tweets['fsharp'].value_counts()[True]]

x_pos = list(range(len(prg_langs)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')

# Settings axis labels and ticks
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: python, vs. javascript vs. ruby vs. csharp vs. fsharp (Raw data', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(prg_langs)
plt.grid()

## Targeting relevant tweets
tweets['programming'] 	= tweets['text'].apply(lambda tweet: word_in_text('programming', tweet))
tweets['tutorial']		= tweets['text'].apply(lambda tweet: word_in_text('tutorial', tweet))

##
tweets['relevant']		= tweets['text'].apply(lambda tweet: word_in_text('programming', tweet) or word_in_text('tutorial', tweet))

print tweets['programming'].value_counts()[True]
print tweets['tutorial'].value_counts()[True]
print tweets['relevant'].value_counts()[True]

## Compare the popularity of the programming languages
print tweets[tweets['relevant'] == True]['python'].value_counts()[True]
print tweets[tweets['relevant'] == True]['javascript'].value_counts()[True]
print tweets[tweets['relevant'] == True]['ruby'].value_counts()[True]
print tweets[tweets['relevant'] == True]['csharp'].value_counts()[True]
#print tweets[tweets['relevant'] == True]['fsharp'].value_counts()[True]

tweets_by_prg_lang = [tweets[tweets['relevant'] == True]['python'].value_counts()[True], 
                      tweets[tweets['relevant'] == True]['javascript'].value_counts()[True], 
                      tweets[tweets['relevant'] == True]['ruby'].value_counts()[True],
                      tweets[tweets['relevant'] == True]['csharp'].value_counts()[True],
                      tweets[tweets['relevant'] == True]['fsharp'].value_counts()[True]]
x_pos = list(range(len(prg_langs)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang, width,alpha=1,color='g')
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: python vs. javascript vs. ruby (Relevant data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(prg_langs)
plt.grid()

## Extract links from tweets
## http:// and https://
def extract_link(text):
	regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
	match = re.search(regex, text)
	if match:
		return match.group()
	return ''

## Add a column that includes links
tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))

## New DataFrame: subset of tweets that contain links
tweets_relevant = tweets[tweets['relevant'] == True]
tweets_relevant_with_link = tweets_relevant[tweets_relevant['link'] != '']

## Print links
print tweets_relevant_with_link[tweets_relevant_with_link['python'] == True]['link']
print tweets_relevant_with_link[tweets_relevant_with_link['javascript'] == True]['link']
print tweets_relevant_with_link[tweets_relevant_with_link['ruby'] == True]['link']
print tweets_relevant_with_link[tweets_relevant_with_link['csharp'] == True]['link']
print tweets_relevant_with_link[tweets_relevant_with_link['fsharp'] == True]['link']

## Show all of our grids ;)
##plt.show()	