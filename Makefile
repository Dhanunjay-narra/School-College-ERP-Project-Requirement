.PHONY: help install test run-backend run-frontend docker-up docker-down

help:
	@echo "Enterprise School & College ERP - Developer Commands"
	@echo "  make install       Install python and node dependencies"
	@echo "  make test          Run pytest suite"
	@echo "  make run-backend   Start FastAPI server"
	@echo "  make run-frontend  Start Vite development server"
	@echo "  make docker-up     Start complete docker-compose stack"

install:
	pip install -r requirements.txt
	cd frontend && npm install

test:
	pytest tests/ -v

run-backend:
	uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload

run-frontend:
	cd frontend && npm run dev

docker-up:
	docker-compose up -d --build

docker-down:
	docker-compose down
