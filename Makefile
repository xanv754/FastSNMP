VENV_EXISTS := $(shell if [ -d "$(CURDIR)/.venv" ]; then echo 1; else echo 0; fi)

.PHONY: venv setup-local

venv:
ifeq ($(VENV_EXISTS),0)
	@echo "Creando entorno virtual del sistema..."
	python3 -m venv $(CURDIR)/.venv
endif

setup-local: venv
ifeq ($(VENV_EXISTS),0)
	@echo "Instalando..."
	$(CURDIR)/.venv/bin/pip install .
endif

setup:
	@echo "Instanciando contenedor..."
	docker buildx build -f Dockerfile . --tag fast-snmp
	docker create --name fast-snmp -p 8888:8000 fast-snmp 
	docker start fast-snmp

start-local:
	@echo "Iniciando servicio..."
	$(CURDIR)/.venv/bin/python3 -m uvicorn fast_snmp.api.app:app --reload --port 8001

start:
	@echo "Iniciando contenedor..."
	docker start fast-snmp

stop:
	@echo "Deteniendo contenedor..."
	docker stop fast-snmp

drop:
	@echo "Eliminando instancia del contenedor..."
	docker stop fast-snmp
	docker rm fast-snmp
	docker image rm fast-snmp

restart: drop setup
	


