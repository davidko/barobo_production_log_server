#!/usr/bin/env python3

from setuptools import setup
import re

version = '0.0.1'

setup(
    name = "barobo_production_log_server",
    version = version,
    install_requires = ["linkbot_diagnostics == 0.2.1", "bottle"],
    description = "Web server for browsing Barobo production logs",
    author = "David Ko",
    author_email = "david@barobo.com",
    scripts = ["bin/barobo_production_log_server.py",],
    )

