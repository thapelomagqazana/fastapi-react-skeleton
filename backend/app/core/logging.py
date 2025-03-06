import logging

# Basic config for logging to terminal and file
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/backend.log"),  # Logs to file
        logging.StreamHandler()  # Logs to terminal
    ]
)

logger = logging.getLogger(__name__)