build:
	pip install -r requirements.txt

install:
	touch /var/log/cron.log

start:
	crontab /etc/crontab
	env | grep -e DSN -e "PASSWORD_FILE" > /etc/environment
	cron

force-stop:
	killall cron;
	rm -vf /var/run/crond.pid;
	echo "";