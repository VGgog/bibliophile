from app import app 
from admin import route

app.include_router(
    route.admin_route,
    prefix='/api'
    )

