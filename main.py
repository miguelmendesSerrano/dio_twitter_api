from fastapi import FastAPI
import uvicorn

from src.services import get_user, save_user, get_db_user

app = FastAPI()


@app.get("/")
def root():
    return "In the URL, enter the user name to get infos. Ex: .../user_name Or access: .../docs"


@app.get("/{user_name}")
async def get_info_user(user_name: str):

    if get_db_user(screen_name=user_name) == []:
        get_user(user_name=user_name)
        save_user(user_name=user_name)

    return get_db_user(screen_name=user_name)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
