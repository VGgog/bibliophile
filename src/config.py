import os

from dotenv import load_dotenv


load_dotenv()


class Config:
    db_url = os.environ.get('DATABASE_URL')
    admin_token = os.environ.get('ADMIN_TOKEN')

