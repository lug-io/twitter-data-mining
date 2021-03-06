#!/usr/bin/python

# Turn off visial settings (breaks on OS w/ no visuals)
import matplotlib
matplotlib.use('Agg')

import os
import re # Regular Expression
import sys
import json
import traceback
import pandas as pd
import matplotlib.pyplot as plt 
from datetime import datetime
from matplotlib import rcParams

# Set paths
base_directory 		= os.environ['HOME']
output_directory    = base_directory + '/output/'
tweets_data_path	= base_directory + '/data/2016/01/29/14.txt'

## Current Date Time
current_datetime = datetime.now()

# Set matplot settings
rcParams.update({'figure.autolayout': True})

def mapToTweet(line):
	newTweet = {}
	newTweet['text'] = None
	newTweet['lang'] = None
	newTweet['country'] = None
	try:
		tweet = json.loads(line)
	except Exception as e:
		print(e)
		return newTweet
	newTweet['text'] = tweet.get('text', None)
	newTweet['lang'] = tweet.get('lang', None)
	newTweet['country'] = None if tweet.get('place', None) is None else tweet.get('place', {}).get('country')
	return newTweet

tweets_data = []
with open(tweets_data_path) as f:
	tweets_data =	[mapToTweet(line)
					for line in f
					if len(line.strip())]

## Total # of tweets captured
print("decoded tweets: " + str(len(tweets_data)))

## New Panda DataFrame
tweets = pd.DataFrame()

## Populate/map DataFrame with data
## tweet.get('text', None) ~= tweet['text'] ?? None
tweets['text'] 		= map(lambda tweet: tweet.get('text', None), tweets_data)
tweets['lang'] 		= map(lambda tweet: tweet.get('lang', None), tweets_data)
tweets['country']   = map(lambda tweet: tweet.get('country', None), tweets_data)

## Chart for top 5 languages
tweets_by_lang = tweets['lang'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Top 5 Languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')

fig.savefig(output_directory + 'top-5-languages-' + str(current_datetime) + '.png')

## Chart for top 5 countries
tweets_by_country = tweets['country'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Top 5 Countries', fontsize=15, fontweight='bold')
tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')

fig.savefig(output_directory + 'top-5-countries-' + str(current_datetime) + '.png')

# Returns true if "word" is in "text"
def word_in_text(word, text):
	if text is None:
		return False
	print(text)
	word = word.lower()
	text = text.lower()
	match = re.search(word, text)
	if match:
		return True
	return False

# Add columns to our tweets DataFrame
tweets['python']     	= map(lambda tweet: words_in_text('python', tweet), tweets['text'])
tweets['javascript'] 	= map(lambda tweet: words_in_text('javascript', tweet), tweets['text'])
tweets['ruby']			= map(lambda tweet: words_in_text('ruby', tweet), tweets['text'])
tweets['csharp']		= map(lambda tweet: words_in_text('csharp', tweet), tweets['text'])
tweets['fsharp']		= map(lambda tweet: words_in_text('fsharp', tweet), tweets['text'])

## Calculate # of tweets for each language
print(tweets['python'])
print(tweets['python'].value_counts())
print(tweets['python'].value_counts()[True])
print(tweets['javascript'].value_counts()[True])
print(tweets['ruby'].value_counts()[True])
print(tweets['csharp'].value_counts()[True])
print(tweets['fsharp'].value_counts()[True])

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

fig.savefig(output_directory + 'raw-comparison-' + str(current_datetime) + '.png')

## Targeting relevant tweets
tweets['programming'] 	= tweets['text'].apply(lambda tweet: word_in_text('programming', tweet))
tweets['tutorial']		= tweets['text'].apply(lambda tweet: word_in_text('tutorial', tweet))

##
tweets['relevant']		= tweets['text'].apply(lambda tweet: word_in_text('programming', tweet) or word_in_text('tutorial', tweet))

print(tweets['programming'].value_counts()[True])
print(tweets['tutorial'].value_counts()[True])
print(tweets['relevant'].value_counts()[True])

## Compare the popularity of the programming languages
print("Relevant Counts:")
print(tweets[tweets['relevant'] == True]['python'].value_counts()[True])
print(tweets[tweets['relevant'] == True]['javascript'].value_counts()[True])
print(tweets[tweets['relevant'] == True]['ruby'].value_counts()[True])
print("C# Count: " + str(tweets[tweets['relevant'] == True]['csharp'].value_counts()[True]))
print("F# Count: " + str(tweets[tweets['relevant'] == True]['fsharp'].value_counts()[True]))

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

fig.savefig(output_directory + 'relevant-comparison-' + str(current_datetime) + '.png')

## Extract links from tweets (http:// and https://)
def extract_link(text):
	if text is None:
		return ''
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
print(tweets_relevant_with_link[tweets_relevant_with_link['python'] == True]['link'])
print(tweets_relevant_with_link[tweets_relevant_with_link['javascript'] == True]['link'])
print(tweets_relevant_with_link[tweets_relevant_with_link['ruby'] == True]['link'])
print(tweets_relevant_with_link[tweets_relevant_with_link['csharp'] == True]['link'])
print(tweets_relevant_with_link[tweets_relevant_with_link['fsharp'] == True]['link'])

## Show all of our grids ;)
##plt.show()	