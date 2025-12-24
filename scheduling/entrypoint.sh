#!/bin/bash

make force-stop
make install
make start

tail -f /var/log/cron.log