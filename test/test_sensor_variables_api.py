# coding: utf-8

"""
    Upstream Sensor Storage

    Sensor Storage for Upstream data

    The version of the OpenAPI document: 0.0.1
    Contact: wmobley@tacc.utexas.edu
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from upstream_client.api.sensor_variables_api import SensorVariablesApi


class TestSensorVariablesApi(unittest.TestCase):
    """SensorVariablesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SensorVariablesApi()

    def tearDown(self) -> None:
        pass

    def test_list_sensor_variables_api_v1_sensor_variables_get(self) -> None:
        """Test case for list_sensor_variables_api_v1_sensor_variables_get

        List Sensor Variables
        """
        pass


if __name__ == '__main__':
    unittest.main()
