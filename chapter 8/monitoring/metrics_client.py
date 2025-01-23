import logging

# Configure the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MetricsClient:
    """3rd-party metrics client"""

    def send(self, metric_name, metric_value):
        if not isinstance(metric_name, str):
            raise TypeError("expected type str for metric_name")
        if not isinstance(metric_value, str):
            raise TypeError("expected type str for metric_value")
        logger.info("sending %s = %s", metric_name, metric_value)
