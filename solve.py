import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)

class ExampleService:
    def __init__(self, name: str):
        self.name = name
        logger.info(f"Service '{self.name}' initialized.")

    def run(self):
        logger.info(f"Service '{self.name}' is running...")
        # Example logic
        return f"Hello from {self.name}!"

def main():
    service_name = os.getenv("SERVICE_NAME", "DefaultService")
    service = ExampleService(service_name)
    result = service.run()
    logger.info(f"Result: {result}")

if __name__ == "__main__":
    main()
