"""Кастомный логгер"""
from loguru import logger


logger.add(
    "logs_dj/log.json",
    format="{time} {level} {message}",
    level="DEBUG",
    rotation="2 MB",
    compression="zip",
    serialize=True
)
