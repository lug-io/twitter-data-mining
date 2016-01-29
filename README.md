# Twitter Data Mining

This project has two main functions. The first is to capture tweets from [Twitter's Streaming API](https://dev.twitter.com/streaming/overview) that include key terms we care about. The second is to apply text mining techniques to parse our captured tweets and derive insights that are relevenat, novel, and interesting. At a high level, here are the questions we're trying to answer and our results:

**How do the popularities of programming languages compare?**

[insert graphs here]

**How do we identify the most useful/best hyperlinks for relevant programming resources?**

[insert top article links here]

**Which twitter users are the best evangelists for a given topic?**

[insert twitter users and metrics that weigh them here]


### Why?

Why not? This is a fun project that shows us how to collect data at the moment it's created. We have tons of it at our fingertips, and from it we can create value. This is also a great introduction to basic mining + refining concepts, and a good example of where Python shines.


### Folder Structure

    .
    ├── home
    │     └── usr 					# home directory for our user
	│		   ├── app 				# project directory for our Python 3 scripts
	│		   ├── data 			# /yyyy/mm/dd/HH.txt for captured tweets
	│		   └── anaconda3		# Install directory for Anaconda
    ├── var
    │	 └── www
    │   	  └── html         		# Root directory for our MySQL/PHP website
    └── ...



## Initial Setup

The below steps are a collection of resources that assist in getting an environment up and running. If you run into issues, please feel free to message me. Also, a large number of these technologies have equivelants that can be swapped out/in.

You can skip the steps below if you have an environment that has:

- Python3
- Tweepy
- Pandas
- Matplotlib
- Screen


### Option 1: Local Machine

...


### Option 2: VPS (Ubuntu)

This setup uses Digital Ocean for hosting. You're welcome to explore other hosting options.

- [Create a Droplet](https://cloud.digitalocean.com/droplets/new)
	- Ubuntu 15.10 x64
	- 512mb, 20GB SSD, 1000 GB Transfer
	- Datacenter of your choice
- [Follow initial server setup](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-14-04)
	- [How to create/use SSH Keys](https://www.digitalocean.com/community/tutorials/how-to-use-ssh-keys-with-putty-on-digitalocean-droplets-windows-users)
- [How to install Linux, Apache, MySQL, PHP (LAMP) stack on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-14-04)
- [Installing (and securing) PHPMyAdmin](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-phpmyadmin-on-ubuntu-12-04)


#### Specific to our Application

**1. Install Anaconda:**

Installing Python3 and the packages we want to use can be difficult. To ease that burdern, we're going to install Anaconda. Anaconda is a cross-platform Python distribution for data analytics and scientific computing. It lowers the barrier for us to start, and is easy to install/uninstall.

- `sudo wget https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda3-2.4.1-Linux-x86_64.sh`
- `bash Anaconda3-2.4.1-Linux-x86_64.sh`
	- `yes` Accept the terms and conditions
	- `yes` Add Anaconda to your system's PATH
	- [For more info](http://conda.pydata.org/docs/install/full.html)
	- [Conda Cheat Sheet](http://conda.pydata.org/docs/_downloads/conda-cheatsheet.pdf)
	- [30 minute test drive](http://conda.pydata.org/docs/test-drive.html)
- `sudo Anaconda3-2.4.1-Linux-x86_64.sh`
- `sudo apt-get install python-qt4`

**2. Install Packages:**

These packages will only be available to your user. That means, any commands run with `sudo` will not be able to use these packages. Unfortunately, we're not leveraging Anaconda's environment features, but I recommend looking into them.

- `conda install pip`
	- [docs](https://pip.pypa.io/en/stable/) | [github](https://github.com/pypa/pip)
- `conda install matplotlib`
	- [docs](http://matplotlib.org/contents.html) | [github](https://github.com/matplotlib/matplotlib)
- `conda install pandas`
	- [docs](http://pandas.pydata.org/pandas-docs/stable/) | [github](https://github.com/pydata/pandas)
- `pip install tweepy`
	- [docs](http://tweepy.readthedocs.org/en/v3.5.0/getting_started.html) | [github](https://github.com/tweepy/tweepy)


**3. Install Screen:**

Screen allows us to run programs in the background without tying up our main console/terminal.

- `sudo apt-get install screen`
	- [More about the screen command](http://www.tecmint.com/screen-command-examples-to-manage-linux-terminals/)


### Option 3: VPS (Docker)

...


## The Basics

- `screen -S data-miner`
- `python3 twitter-streaming.py`
- `CTRL + a, d`
	- Detach from active screen

- `sudo nano /var/mail/root`
	- Shows emails from CRON to `root` user
	- Requires postfix be installed (e-mail)
- `sudo grep CRON /var/log/syslog`
	- Shows system logs specific to cron
- `sudo crontab -e`
	- Access root's cron list
	- Make sure target scripts are chmod +x for execution
- [Backing up and storing crontab](http://askubuntu.com/questions/216692/where-is-the-user-crontab-stored)


### Running Data Mining in the Background

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