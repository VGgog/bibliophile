import os

from dotenv import load_dotenv


load_dotenv()


class Config:

    admin_token = os.environ.get('ADMIN_TOKEN')
    db_url = os.environ.get('DATABASE_URL')
