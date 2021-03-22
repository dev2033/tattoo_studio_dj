"""
Логирование
"""
from loguru import logger


logger.add(
    "logging/log.json",
    format="{time} {level} {message}",
    level="ERROR",
    rotation="2 MB",
    compression="zip",
    serialize=True
)
