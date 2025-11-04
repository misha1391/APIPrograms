from fastapi import FastAPI
import uvicorn
# Нужно использовать uvicorn
app = FastAPI()

@app.get("/home") # Отправить клиенту
def get_home_page():
    return {"message": "Привет сосед, когда перестанешь воровать?"}

@app.get("/PC/{id}") # Пример ввода можно посмотреть у Youtube
def get_PC_info(id: int, q: str):
    return {"info": "Это просто компьютер", "id": id, "q": q}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")