
import os
import time
#os.system("/opt/datadog-agent/embedded/bin/pip install datadog")
#os.system("/opt/datadog-agent/embedded/bin/pip install datadog-api-client")
os.system("pip install datadog")
os.system("pip install datadog-api-client")
import random
"""
Submit metrics returns "Payload accepted" response
"""
from datetime import datetime
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.metric_intake_type import MetricIntakeType
from datadog_api_client.v2.model.metric_payload import MetricPayload
from datadog_api_client.v2.model.metric_point import MetricPoint
from datadog_api_client.v2.model.metric_resource import MetricResource
from datadog_api_client.v2.model.metric_series import MetricSeries
configuration = Configuration(
    host="https://app.datadoghq.com/"
)
configuration.api_key['apiKeyAuth'] = '0e57a2d8fec71136d61f13f28a3d4280'
configuration.api_key['appKeyAuth'] = '34a9ec74b0d4a4b95051fdf5652e76491de1cf98'
#for user in range(100):
body = MetricPayload(
    series=[
        MetricSeries(
            metric="logged_in_user_count",
            type=MetricIntakeType.COUNT,
            points=[
                MetricPoint(
                    timestamp=int(datetime.now().timestamp()),
                    #value=print(os.system("(quser).count-1")),
                    value=print(os.system("users | wc -w")),
                    #value=print(os.system("w | awk -F',' '{print $2}'")),
                ),
            ],
            resources=[
                MetricResource(
                    name="localhost",
                    type="host",
                ),
            ],
            tags=["method:test","custom:metric"]
        ),
    ],
)
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.submit_metrics(body=body)
    print(response)

