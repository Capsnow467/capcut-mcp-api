from app import create_app
import uvicorn
from settings.local import PORT

app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
