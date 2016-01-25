# Twitter Data Mining

## Requirements

- [Python 2.7.9+](https://www.python.org/downloads/)
- Have Python & [PIP](http://stackoverflow.com/questions/4750806/how-do-i-install-pip-on-windows) in your path

## Setup

- `pip install pandas`
	- My machine required [some love](http://stackoverflow.com/questions/23064899/compiler-problems-with-pip-during-numpy-install-under-windows-8-1-7-enterprise) and... [some more love](https://www.microsoft.com/en-us/download/confirmation.aspx?id=44266) to make this work.
- `pip install matplotlib`


## How To..

- `python twitter-streaming.py > output.txt`
	- Pipe twitter data to an output file
- `python data-parser.py`
	- Uses output.txt to generate relevant charts in root folder

### After following "Remote Hosting" Instructions

- `screen -S [name]`
	- Start new session with [name]
- `screen -ls`
	- List active sessions
- `screen -r [name]`
	- Attach running session to [name]
- `screen -X -S [session # to kill] kill`
	- Kill a screen session
- `CTRL + a, d`
	- Detach from active screen

## Sources
- This wonderful [blog post](http://adilmoujahid.com/posts/2014/07/twitter-analytics/) by [Adil Moujahid](https://twitter.com/AdilMouja)
- Publishing [Python to Digital Ocean](https://nikolak.com/deploying-python-code-to-vps/) by [Nikola Kovacevic](https://github.com/Nikola-K)