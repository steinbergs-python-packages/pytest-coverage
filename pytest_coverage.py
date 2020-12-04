#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module provides a set of pytest hooks for generating test coverage reports."""

import coverage
import os

import pytest


class TestCoverage(object):
    """The TestCoverage class.

        Wraps the coverage functionality in a simple manner.
    """
    cov = None

    @classmethod
    def start(cls):
        """Start the test coverage as (and if) configured in .coveragerc."""
        if cls.cov is None:
            cls.cov = coverage.coverage()
        if getattr(cls.cov.config, "config_files", None) or getattr(cls.cov.config, "config_files_read", None):  # suporting 4.x and 5.x
            cls.cov.start()

    @classmethod
    def stop(cls):
        """Stop the test coverage and create reports as (and if) configured in .coveragerc."""
        if cls.cov is None:
            return
        if not getattr(cls.cov.config, "config_files", None) and not getattr(cls.cov.config, "config_files_read", None):  # suporting 4.x and 5.x
            return
        cls.cov.stop()
        if cls.cov.config.data_file not in ("", ".coverage"):  # ignore default filename. if needed, use different filename.
            os.makedirs(os.path.dirname(os.path.abspath(cls.cov.config.data_file)), exist_ok=True)
            cls.cov.save()
        if cls.cov.config.html_dir not in ("", "htmlcov"):  # ignore default path. if needed, use different path.
            cls.cov.html_report(directory=cls.cov.config.html_dir)
        if cls.cov.config.xml_output not in ("", "coverage.xml"):  # ignore default filename. if needed, use different filename.
            cls.cov.xml_report(outfile=cls.cov.config.xml_output)


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    """This is called before session.main() and test collection, i.e. at the very start."""
    TestCoverage.start()  # enabled by existing .coveragerc only


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    """This is called after whole test run has finished, i.e. at the very end."""
    TestCoverage.stop()  # enabled by existing .coveragerc only
