import os

from app import db as database
from app import create_app
from database.builk import update_data
from dotenv import load_dotenv

load_dotenv()

app = create_app(os.getenv('APP_SETTINGS'))


if __name__ == '__main__':
    if os.getenv('APP_SETTINGS') != "testing":
        with app.app_context():
            update_data(database)
    app.run(host='0.0.0.0')
