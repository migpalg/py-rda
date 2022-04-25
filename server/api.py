from concurrent.futures import thread
from enum import auto
import threading
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from uuid import uuid4
from .payload_models import Execution
from .processes import automate

app = FastAPI()
app.mount('/client', StaticFiles(directory="static", html=True), name="static")


@app.post('/execute')
async def execute(execution: Execution):
    process_thread = threading.Thread(target=automate)

    process_thread.start()

    return {
        "message": execution,
        "executionId": uuid4()
    }
