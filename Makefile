TEMPLATE_DIR=./template
-include .env

configure: .env 

build:
	docker compose build

install: $(SECRET_DIR)/odoo_pg_pass $(SECRET_DIR)/api_mariadb_root_pass
	docker compose up -d postgres
	docker compose run --rm -w /data odoo make install
	docker compose exec -w /data postgres make install

.env: 
	cp -v $(TEMPLATE_DIR)/$@ .
	vim $@

$(SECRET_DIR):
	mkdir -v -p $@

$(SECRET_DIR)/odoo_pg_pass: $(SECRET_DIR)
	read -p "DB Postgres Password : " pass && (echo $${pass} > $@)

$(SECRET_DIR)/api_mariadb_root_pass: $(SECRET_DIR)
	read -p "DB MariaDB Password : " pass && (echo $${pass} > $@)