# -*- coding: utf-8 -*-
"""
@author: Rosario Distefano
@email: rosario.distefano@osumc.edu
"""

from motor.motor_asyncio import AsyncIOMotorClient
import yaml
import os


def load_config() -> dict:
    with open('config/config.yml') as yaml_file:
        conf = yaml.load(yaml_file.read(), Loader=yaml.SafeLoader)
    return conf

CONF = load_config()

DB_CLIENT = AsyncIOMotorClient(
    host=os.getenv("MONGO_HOST", ""),
    port=int(os.getenv("MONGO_PORT", "")),
    username=os.getenv("MONGO_USER", ""),
    password=os.getenv("MONGO_PASS", "")
)

DB = DB_CLIENT[os.getenv("MONGO_DB", "")]

def close_db_client():
    DB_CLIENT.close()
