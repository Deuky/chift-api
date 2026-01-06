#!/bin/bash

make force-stop
make start

tail -f /var/log/cron.log