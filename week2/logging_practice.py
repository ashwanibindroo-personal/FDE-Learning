import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    filename="week2/run.log",
)
logger = logging.getLogger(__name__)

logger.debug("This is a debug message")
logger.info("Loaded 428 roads")
logger.warning("Skipped road id 1: no tags")
logger.error("Could not find the file")

