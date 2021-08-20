from fastapi import Depends, FastAPI

from routers.personas_router import router as router_usuarios
from routers.solicitud_router import router as router_solicitud
from routers.socializacion_router import router as router_socializacion
from routers.acompanamiento_router import router as router_acompanamiento
from routers.fortalecimiento_router import router as router_fortalecimiento
from routers.medicion_router import router as router_medicion
from routers.proyecto_router import router as router_proyecto
from routers.charla_router import router as router_charla
from routers.capacitacion_router import router as router_capacitacion
from routers.home_router import router as router_home

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

origins = [
"http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
"http://localhost", "http://localhost:8080", "http://localhost:8081"
]

app.add_middleware(
CORSMiddleware, allow_origins=origins,
allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

app.include_router(router_usuarios)
app.include_router(router_solicitud)
app.include_router(router_socializacion)
app.include_router(router_acompanamiento)
app.include_router(router_fortalecimiento)
app.include_router(router_medicion)
app.include_router(router_proyecto)
app.include_router(router_charla)
app.include_router(router_capacitacion)
app.include_router(router_home)