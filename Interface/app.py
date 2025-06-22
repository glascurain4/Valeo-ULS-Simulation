import os
import serial
import time
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

SERIAL_PORT = ""  
BAUDRATE = 

try:
    device = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1)
    time.sleep(2)
    print(f" Conectado a {SERIAL_PORT}")
except Exception as e:
    device = None
    print(f" No se pudo abrir {SERIAL_PORT}: {e}")

app = FastAPI(title="Servidor de ANA", version="1.0.0")
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@app.get("/us.html", response_class=HTMLResponse)
async def about_us(request: Request):
    return templates.TemplateResponse("us.html", {"request": request})

@app.get("/project.html", response_class=HTMLResponse)
async def about_project(request: Request):
    return templates.TemplateResponse("project.html", {"request": request})

@app.post("/send-command")
async def handle_command(request: Request):
    data = await request.json()
    command = f"{data['sensor']}{data['value']}\n"

    if device and device.is_open:
        try:
            device.write(command.encode())
            print(f"Enviado al micro: {command.strip()}")

            time.sleep(0.5)
            if device.in_waiting:
                response = device.readline().decode().strip()
                print(f"Respuesta: {response}")
            else:
                response = "No hubo respuesta del micro"

            return JSONResponse(content={"status": "ok", "sent": command.strip(), "response": response})
        except Exception as e:
            return JSONResponse(status_code=500, content={"status": "error", "message": str(e)})
    else:
        return JSONResponse(status_code=500, content={"status": "error", "message": "Puerto serial no disponible"})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9090)