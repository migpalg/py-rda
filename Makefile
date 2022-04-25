main:
	uvicorn server.api:app --host 0.0.0.0

dev:
	uvicorn server.api:app --reload