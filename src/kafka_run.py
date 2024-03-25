import asyncio

from app import logger


async def _run_core_consumer():
    from apis.core.kafka_conf import CoreApiConsumer

    logger.info("\n----Start Core Consumer----\n")
    core_consumer = CoreApiConsumer()
    await core_consumer.run()


if __name__ == "__main__":
    asyncio.run(_run_core_consumer())
