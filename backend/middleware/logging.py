# backend/middleware/logging.py

from fastapi import Request
import time
import logging

logger = logging.getLogger("uvicorn")

async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info(f"{request.method} {request.url.path} - {response.status_code} [{duration:.2f}s]")
    return response
