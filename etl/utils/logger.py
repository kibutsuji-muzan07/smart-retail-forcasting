import logging
import os

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=f"{LOG_DIR}/etl.log",
    level = logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)