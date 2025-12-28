configure:

build:

install: waiting-pg
	odoo db --db_host ${HOST} --db_password "$(shell cat ${PASSWORD_FILE})" init --username $(USERNAME) --password $(PASSWORD) "$(APP_NAME)";
	odoo -d "$(APP_NAME)" --db_host ${HOST} --db_password "$(shell cat ${PASSWORD_FILE})" -i contacts --stop-after-init;

waiting-pg:
	pg_isready -h ${HOST} -t 3 || $(MAKE) waiting-pg