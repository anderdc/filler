import os
import logging
import argparse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)
logger = logging.getLogger(__name__)

class ExampleApp:
    def __init__(self, name: str):
        self.name = name
        logger.info(f"App '{self.name}' initialized.")

    def run(self):
        logger.info(f"Running app '{self.name}'...")
        return f"Hello from {self.name}!"

def main():
    # Argument parsing
    parser = argparse.ArgumentParser(description="Example boilerplate app.")
    parser.add_argument(
        "--name",
        type=str,
        default=os.getenv("APP_NAME", "DefaultApp"),
        help="Name of the app (can also be set with APP_NAME environment variable)."
    )
    args = parser.parse_args()

    # Run the app
    app = ExampleApp(args.name)
    result = app.run()
    logger.info(f"Result: {result}")

if __name__ == "__main__":
    main()
