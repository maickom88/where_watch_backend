# type: ignore
from src import init_app
import uvicorn


if __name__ == "__main__":
    app = init_app()
    uvicorn.run(app, host='0.0.0.0', port=5000)
