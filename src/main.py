from app import app 
from app.admin import route

app.include_router(
    route.admin_route,
    prefix='/api'
    )
