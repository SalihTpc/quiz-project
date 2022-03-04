from .base import *
import os
from decouple import config

env_name = config("ENV_NAME")


if env_name == "production":

    from .production import *

elif env_name == "dev":

    from .dev import *