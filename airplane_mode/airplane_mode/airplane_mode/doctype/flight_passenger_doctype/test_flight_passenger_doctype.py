# Copyright (c) 2025, komal panchal and Contributors
# See license.txt

# import frappe
from frappe.tests import IntegrationTestCase, UnitTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class UnitTestFlightPassengerDoctype(UnitTestCase):
	"""
	Unit tests for FlightPassengerDoctype.
	Use this class for testing individual functions and methods.
	"""

	pass


class IntegrationTestFlightPassengerDoctype(IntegrationTestCase):
	"""
	Integration tests for FlightPassengerDoctype.
	Use this class for testing interactions between multiple components.
	"""

	pass
