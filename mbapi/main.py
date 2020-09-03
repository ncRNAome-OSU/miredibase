# -*- coding: utf-8 -*-
"""
@author: Rosario Distefano
@email: rosario.distefano@osumc.edu
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import mb_router, mbc_router
from config import config
import os

app = FastAPI(
    title="MiREDiBase",
    debug=False,
    description="MiREDiBase APIs with auto docs API.",
    version="1.0"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    mb_router,
    tags=["Search APIs"],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    mbc_router,
    tags=["Comparison APIs"],
    responses={404: {"description": "Not found"}},
)

@app.on_event("startup")
async def app_startup():
    """Initialization"""
    config.load_config()

@app.on_event("shutdown")
async def app_shutdown():
    """Termination"""
    config.close_db_client()
