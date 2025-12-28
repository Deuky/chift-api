build:
	pip install -r requirements.txt

install:
	touch /var/log/cron.log
	crontab /etc/crontab

start:
	env | grep -e DSN -e "PASSWORD_FILE" > /etc/environment
	cron

force-stop:
	killall cron;
	rm -vf /var/run/crond.pid;
	echo "";