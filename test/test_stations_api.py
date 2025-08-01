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

from upstream_client.api.stations_api import StationsApi


class TestStationsApi(unittest.TestCase):
    """StationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StationsApi()

    def tearDown(self) -> None:
        pass

    def test_create_station_api_v1_campaigns_campaign_id_stations_post(self) -> None:
        """Test case for create_station_api_v1_campaigns_campaign_id_stations_post

        Create Station
        """
        pass

    def test_delete_sensor_api_v1_campaigns_campaign_id_stations_delete(self) -> None:
        """Test case for delete_sensor_api_v1_campaigns_campaign_id_stations_delete

        Delete Sensor
        """
        pass

    def test_get_station_api_v1_campaigns_campaign_id_stations_station_id_get(self) -> None:
        """Test case for get_station_api_v1_campaigns_campaign_id_stations_station_id_get

        Get Station
        """
        pass

    def test_list_stations_api_v1_campaigns_campaign_id_stations_get(self) -> None:
        """Test case for list_stations_api_v1_campaigns_campaign_id_stations_get

        List Stations
        """
        pass

    def test_partial_update_station_api_v1_campaigns_campaign_id_stations_station_id_patch(self) -> None:
        """Test case for partial_update_station_api_v1_campaigns_campaign_id_stations_station_id_patch

        Partial Update Station
        """
        pass

    def test_update_station_api_v1_campaigns_campaign_id_stations_station_id_put(self) -> None:
        """Test case for update_station_api_v1_campaigns_campaign_id_stations_station_id_put

        Update Station
        """
        pass


if __name__ == '__main__':
    unittest.main()
