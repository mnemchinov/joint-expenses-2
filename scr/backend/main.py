from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from scr.backend.app.api.v1.routers import PartnerRouter, OrderRouter, \
    OrderPartnersRouter
from scr.backend.settings import settings

app = FastAPI(
    debug=settings.debug,
    title=settings.app_name,
    version=settings.version,
    description=settings.description,
)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_v1_prefix = '/api/v1'

app.include_router(PartnerRouter().router, prefix=api_v1_prefix)
app.include_router(OrderRouter().router, prefix=api_v1_prefix)
app.include_router(OrderPartnersRouter().router, prefix=api_v1_prefix)

if __name__ == 'main':
    import uvicorn

    uvicorn.run(
        app,
        host='0.0.0.0',
        port=8000,
        http='h11',
        loop='uvloop',
        timeout_keep_alive=20,
        backlog=8192,
        use_colors=True,
    )
