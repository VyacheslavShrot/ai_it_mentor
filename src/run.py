import uvicorn
from fastapi import HTTPException


async def _run_server():
    from app import logger
    try:
        from test_app import test_main_route

        await test_main_route()
        logger.info("\n----The application test has been successfully executed----\n")
    except Exception as e:
        logger.error(f"\n----An error occurred when running tests----\n {e}\n")
        raise HTTPException(status_code=500, detail=f"An error occurred when running tests\n {e}")

    uvicorn_cmd = "app:app"
    uvicorn.run(uvicorn_cmd, host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    import asyncio

    asyncio.run(_run_server())
