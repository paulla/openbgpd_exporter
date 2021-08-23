#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
openbgpd_exporter
------------------------------
OpenBGP Prometheus Exporter

"""

__docformat__ = 'restructuredtext en'


"""Application exporter"""

import os
import time
from prometheus_client import start_http_server, Gauge, Enum
import random
import requests
import subprocess

def get_uptime():
    out = subprocess.run(['/usr/bin/uptime'], stdout=subprocess.PIPE, encoding='utf-8')
    return out.stdout.split(' ')[4].split(':')[0]
     
def get_current_requests():
    out = subprocess.run(['ls','-l', '/home/simon/dev/paulla/openbgpd_exporter/src/paulla/openbgpd_exporter/__init__.py'], stdout=subprocess.PIPE, encoding='utf-8')
    return out.stdout.split(' ')[4]

def get_health():
    health_list=["healthy", "unhealthy"]
    rand = random.randint(0,1)
    return health_list[rand]


class AppMetrics:
    """
    Representation of Prometheus metrics and loop to fetch and transform
    application metrics into Prometheus metrics.
    """

    def __init__(self, polling_interval_seconds=5):
        self.polling_interval_seconds = polling_interval_seconds

        # Prometheus metrics to collect
        self.current_requests = Gauge("app_requests_current", "Current requests")
        self.total_uptime = Gauge("node_uptime", "Uptime")
        self.health = Enum("app_health", "Health", states=["healthy", "unhealthy"])

    def run_metrics_loop(self):
        """Metrics fetching loop"""

        while True:
            self.fetch()
            time.sleep(self.polling_interval_seconds)


    def fetch(self):
        """
        Get metrics from application and refresh Prometheus metrics with
        new values.
        """


        # Update Prometheus metrics with application metrics
        self.current_requests.set(get_current_requests())
        self.total_uptime.set(get_uptime())
        self.health.state(get_health())

def main():
    """Main entry point"""

    polling_interval_seconds = int(os.getenv("POLLING_INTERVAL_SECONDS", "5"))
    exporter_port = int(os.getenv("EXPORTER_PORT", "8000"))

    app_metrics = AppMetrics(
        polling_interval_seconds=polling_interval_seconds
    )
    start_http_server(exporter_port)
    app_metrics.run_metrics_loop()

if __name__ == "__main__":
    main()

# vim:set et sts=4 ts=4 tw=80:
