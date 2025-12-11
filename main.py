from app import create_app
import uvicorn
from settings.local import PORT
import os

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", PORT))
    uvicorn.run(app, host="0.0.0.0", port=port)
