"""Кастомный логгер"""
from loguru import logger


logger.add(
    "logging/log.json",
    format="{time} {level} {message}",
    level="DEBUG",
    rotation="2 MB",
    compression="zip",
    serialize=True
)
