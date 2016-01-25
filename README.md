# Twitter Data Mining


## Setup

### Local Machine (Windows)

- **Requires:**
	- [Python 2.7.9+](https://www.python.org/downloads/)
	- Have Python & [PIP](http://stackoverflow.com/questions/4750806/how-do-i-install-pip-on-windows) in your path
- `pip install pandas`
	- My machine required [some love](http://stackoverflow.com/questions/23064899/compiler-problems-with-pip-during-numpy-install-under-windows-8-1-7-enterprise) and... [some more love](https://www.microsoft.com/en-us/download/confirmation.aspx?id=44266) to make this work.
- `pip install matplotlib`


### Hosted Server (Ubuntu 14.04)

1. [Initial Server Setup w/ Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-14-04)
	- [How to create/use SSH Keys](https://www.digitalocean.com/community/tutorials/how-to-use-ssh-keys-with-putty-on-digitalocean-droplets-windows-users)
2. [How to install Linux, Apache, MySQL, PHP (LAMP) stack on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-14-04)
3. Publishing [Python to Digital Ocean](https://nikolak.com/deploying-python-code-to-vps/)
	- `pip install pandas`
		- Install [Setup Tools](http://stackoverflow.com/questions/8650459/how-to-get-setuptools-and-easy-install)
		- Install [Numpy](http://stackoverflow.com/questions/13061379/error-of-install-numpy-on-linux-red-hat)
		- Install [Python Dev](http://stackoverflow.com/questions/21530577/fatal-error-python-h-no-such-file-or-directory)
		- [1Gb RAM Minimum](http://stackoverflow.com/questions/24455238/lxml-installation-error-ubuntu-14-04-internal-compiler-error)
	- `pip install matplotlab`
		- Install [these](http://stackoverflow.com/questions/25674612/ubuntu-14-04-pip-cannot-upgrade-matplotllib) first



## How To..

- `python twitter-streaming.py > output.txt`
	- Pipe twitter data to an output file
- `python data-parser.py`
	- Uses output.txt to generate relevant charts in root folder

### Spin up server/processes


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
- [Data mining using twitter's streaming API](http://adilmoujahid.com/posts/2014/07/twitter-analytics/) by [Adil Moujahid](https://twitter.com/AdilMouja)
- Publishing [Python to Digital Ocean](https://nikolak.com/deploying-python-code-to-vps/) by [Nikola Kovacevic](https://github.com/Nikola-K)