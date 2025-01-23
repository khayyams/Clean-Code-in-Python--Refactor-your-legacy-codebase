from metrics_client import MetricsClient

class WrappedClient:
    """Wrapper around MetricsClient to ensure proper type conversion"""

    def __init__(self):
        self.client = MetricsClient()

    def send(self, metric_name, metric_value):
        # Convert both parameters to strings before sending
        return self.client.send(str(metric_name), (metric_value))


class Process:
    def __init__(self):
        # Use WrappedClient instead of MetricsClient directly
        self.client = WrappedClient()

    def run_process(self):
        # Return a constant value
        return 42

    def process_iterations(self, n_iterations):
        for i in range(n_iterations):
            result = self.run_process()
            self.client.send(f"iteration.{i}", result)


# Example of running the code
if __name__ == "__main__":
    process = Process()
    process.process_iterations(5)  # Run 5 iterations
