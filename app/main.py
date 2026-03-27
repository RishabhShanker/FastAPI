from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import routes_auth, routes_predict
from app.middleware.logging_middleware import LoggingMiddleware
from app.core.exceptions import register_exception_handlers

app = FastAPI(title="Car Price Prediction API", version="1.0")

app.add_middleware(LoggingMiddleware)

app.include_router(routes_auth.router, tags=["Authentication"])
app.include_router(routes_predict.router, tags=["Prediction"])

#monitoring with Prometheus
Instrumentator().instrument(app).expose(app)

#add exception handlers
register_exception_handlers(app)