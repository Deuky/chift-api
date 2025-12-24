configure:

build:

install: waiting-pg
	odoo db --db_host ${HOST} --db_password "$(shell cat ${PASSWORD_FILE})" init --username odoo --password password "chift-api";
	odoo -d "chift-api" --db_host ${HOST} --db_password "$(shell cat ${PASSWORD_FILE})" -i contacts --stop-after-init;

waiting-pg:
	pg_isready -h ${HOST} || (sleep 1 && $(MAKE) waiting-pg)