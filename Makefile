.PHONY: help install dev run test lint format clean migrate seed docker-build docker-up docker-down

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install dependencies
	pip install -r requirements.txt

dev: ## Run development server
	python -m uvicorn src.main:app --reload --host 127.0.0.1 --port 8080

run: ## Run production server
	python -m uvicorn src.main:app --host 0.0.0.0 --port 8080

test: ## Run tests
	python -m pytest tests/ -v

lint: ## Run linting
	python -m black src/ tests/
	python -m isort src/ tests/
	python -m flake8 src/ tests/

format: ## Format code
	python -m black src/ tests/
	python -m isort src/ tests/

clean: ## Clean cache files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +

migrate: ## Run database migrations
	python -m src.database.migrations

seed: ## Seed database
	python -m src.database.seed

docker-build: ## Build Docker image
	docker-compose build

docker-up: ## Start Docker containers
	docker-compose up -d

docker-down: ## Stop Docker containers
	docker-compose down

docker-logs: ## View Docker logs
	docker-compose logs -f

docker-shell: ## Access container shell
	docker-compose exec app bash

docker-clean: ## Clean Docker resources
	docker-compose down -v
	docker system prune -f