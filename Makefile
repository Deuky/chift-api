TEMPLATE_DIR=./template
MARIADB_PASSWORD=$(shell cat secrets/api_mariadb_root_pass)
ifeq ("$(wildcard .env)", ".env")
	include .env
endif

configure: .env

build: _models _database
	docker compose build

install: _secrets
	docker compose up -d postgres mariadb
	docker compose run --rm -w /data odoo make install APP_NAME=${ODOO_APP_NAME} USERNAME=${ODOO_USERNAME} PASSWORD=${ODOO_PASSWORD}
	cat postgresql/init.sql | docker compose exec -T postgres psql -U odoo $(ODOO_APP_NAME)
	$(MAKE) waiting-mariadb
	@cat mariadb/init.sql | docker compose exec -T mariadb mariadb -p'$(MARIADB_PASSWORD)'
	docker compose down

start:
	docker compose up -d

stop:
	docker compose

clear:
	docker compose down -v
	git clean -Xfd

_secrets: $(SECRET_DIR) $(SECRET_DIR)/odoo_pg_pass $(SECRET_DIR)/api_mariadb_root_pass
_models: app/fastapi/app/models scheduling/tasks/models app/flask/app/models
_database: app/fastapi/app/database.py scheduling/tasks/database.py app/flask/app/database.py

$(SECRET_DIR):
	mkdir -v -p $@

$(SECRET_DIR)/odoo_pg_pass: 
	read -p "DB Postgres Password : " pass && (echo $${pass} > $@)

$(SECRET_DIR)/api_mariadb_root_pass: 
	read -p "DB MariaDB Password : " pass && (echo $${pass} > $@)

waiting-mariadb:
	@docker compose exec mariadb healthcheck.sh --connect --innodb_initialized || (sleep 2 && $(MAKE) waiting-mariadb)

app/fastapi/app/models scheduling/tasks/models app/flask/app/models:
	cp -rfv app/models $@

app/fastapi/app/database.py scheduling/tasks/database.py app/flask/app/database.py:
	cp -fv app/database/database.py $@

.env: 
	cp -v $(TEMPLATE_DIR)/$@ .
	vim $@
