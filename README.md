# Twitter Data Mining


## Initial Setup

There are quite a few steps here, but I wanted to provide as much information as I could to reproduce the hosted environment I'm using. If you run into issues, please feel free to message me. Also, a large number of these technologies have equivelants that they can be swapped out for.

### Basic Server Setup

- [Create a Droplet](https://cloud.digitalocean.com/droplets/new)
	- Ubuntu 15.10 x64
	- 512mb, 20GB SSD, 1000 GB Transfer
	- Datacenter of your choice
- [Follow initial server setup](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-14-04)
	- [How to create/use SSH Keys](https://www.digitalocean.com/community/tutorials/how-to-use-ssh-keys-with-putty-on-digitalocean-droplets-windows-users)
- [How to install Linux, Apache, MySQL, PHP (LAMP) stack on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-14-04)
- [Installing (and securing) PHPMyAdmin](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-phpmyadmin-on-ubuntu-12-04)


### Specific to our Application

**Install Anaconda:**

Installing Python3 and the packages we want to use can be difficult. To ease that burdern, we're going to install Anaconda. Anaconda is a cross-platform Python distribution for data analytics and scientific computing. It lowers the barrier for us to start, and is easy to install/uninstall.

- `sudo wget https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda3-2.4.1-Linux-x86_64.sh`
- `bash Anaconda3-2.4.1-Linux-x86_64.sh`
	- `yes` Accept the terms and conditions
	- `yes` Add Anaconda to your system's PATH
	- [For more info](http://conda.pydata.org/docs/install/full.html)
	- [Conda Cheat Sheet](http://conda.pydata.org/docs/_downloads/conda-cheatsheet.pdf)
	- [30 minute test drive](http://conda.pydata.org/docs/test-drive.html)

- `conda install pip`
- `conda install matplotlib`
- `conda install pandas`
- `pip install tweepy` [docs](http://tweepy.readthedocs.org/en/v3.5.0/getting_started.html) | [github](https://github.com/tweepy/tweepy)


### Local Machine ONLY Setup

...



## STUFF

- `sudo nano /var/mail/root`
	- Shows emails from CRON to `root` user
	- Requires postfix be installed (e-mail)
- `sudo grep CRON /var/log/syslog`
	- Shows system logs specific to cron
- `sudo crontab -e`
	- Access root's cron list
	- Make sure target scripts are chmod +x for execution
- [Backing up and storing crontab](http://askubuntu.com/questions/216692/where-is-the-user-crontab-stored)


### Hosted Server (Docker)

To come at a later date.


## Executing Code Examples/HowTo

### The Basics

- `python twitter-streaming.py > output.txt`
	- Pipe twitter data to an output file
- `python data-parser.py`
	- Uses output.txt to generate relevant charts in root folder

	sudo sh -c 'python twitter-streaming.py > /var/www/html/content/data/1-24-2016.txt'


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

### Automating

- Storing daily/weekly/monthly results in a database (and deleting old files)
- Running daily/weekly/monthly reports on existing data
- Accessing collected/stored data and reports via web requests

## Sources
- [Data mining using twitter's streaming API](http://adilmoujahid.com/posts/2014/07/twitter-analytics/) by [Adil Moujahid](https://twitter.com/AdilMouja)
- Publishing [Python to Digital Ocean](https://nikolak.com/deploying-python-code-to-vps/) by [Nikola Kovacevic](https://github.com/Nikola-K)