import logging

class NoOpenAILogFilter(logging.Filter):
    def filter(self, record):
        return 'openai' not in record.getMessage()

def setup_logging(log_file='app.log'):
    logging.basicConfig(
        level=logging.INFO,  # Set the logging level to INFO
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    # Add the custom filter to suppress OpenAI debug logs
    for handler in logging.getLogger().handlers:
        handler.addFilter(NoOpenAILogFilter())
