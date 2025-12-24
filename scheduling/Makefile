build:
	pip install -r requirements.txt

install:
	touch /var/log/cron.log
	crontab /etc/crontab

start:
	cron

force-stop:
	killall cron;
	rm -vf /var/run/crond.pid;
	echo "";