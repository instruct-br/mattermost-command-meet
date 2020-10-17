import uvicorn

from settings import DEBUG


if __name__ == "main":
    if DEBUG:
        uvicorn.run(
            'main:app',
            host="0.0.0.0",
            port=8000,
            log_level="debug",
            reload=True,
            debug=True
        )
    else:
        uvicorn.run(
            'main:app',
            host="0.0.0.0",
            port=8000,
            log_level="info",
            workers=2
        )
