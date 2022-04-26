from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from uuid import uuid4
from .processes import automate

app = FastAPI()
app.mount('/client', StaticFiles(directory="static", html=True), name="static")


@app.post('/execute')
async def execute():
    buffer = automate()

    print(buffer)

    res = StreamingResponse(iter([buffer.getvalue()]), media_type='text/csv')

    res.headers["Content-Disposition"] = "attachment; filename=export.csv"

    return res
