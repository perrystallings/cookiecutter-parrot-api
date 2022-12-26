from locust import HttpUser, task, events
import requests
import logging

TEMPLATE_UUID = None


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    pass


class PerformanceUser(HttpUser):
    @task
    def test_home(self):
        self.client.get("/v1/ui")


@events.quitting.add_listener
def _(environment, **kw):
    if environment.stats.total.fail_ratio > 0.01:
        logging.error("Test failed due to failure ratio > 1%")
        environment.process_exit_code = 1
    elif environment.stats.total.avg_response_time > 100:
        logging.error("Test failed due to average response time ratio > 100 ms")
        environment.process_exit_code = 1
    elif environment.stats.total.get_response_time_percentile(0.95) > 500:
        logging.error("Test failed due to 95th percentile response time > 500 ms")
        environment.process_exit_code = 1
    else:
        environment.process_exit_code = 0
