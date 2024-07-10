# To enable dogstatsd
# vi /etc/datadog-agent/datadog.yaml
# use_dogstatsd: true
# dogstatsd_port: 8125
# systemctl restart datadog-agent.service

#import subprocess
#subprocess.call(/opt/datadog-agent/embedded/bin/pip install datadog)

import os
import time
os.system("/opt/datadog-agent/embedded/bin/pip install datadog")
os.system("/opt/datadog-agent/embedded/bin/pip install datadog-api-client")

from datadog import initialize, statsd

options = {
    'statsd_host':'127.0.0.1',
    'statsd_port':8125
}

initialize(**options)

while(1):
  statsd.increment('example_metric.increment', tags=["environment:test"])
  statsd.decrement('example_metric.decrement', tags=["environment:test"])
  time.sleep(10)
