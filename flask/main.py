import os
from dotenv import load_dotenv
from app import create_app

# load .env
dotenv_path = os.path.join(os.path.dirname(__file__), '.flaskenv')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path, override=True)

app = create_app(os.environ.get("FLASK_ENV"))

if __name__ == "__main__":
    app.run(debug=True)
