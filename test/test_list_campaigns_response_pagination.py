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

from upstream_client.models.list_campaigns_response_pagination import ListCampaignsResponsePagination

class TestListCampaignsResponsePagination(unittest.TestCase):
    """ListCampaignsResponsePagination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListCampaignsResponsePagination:
        """Test ListCampaignsResponsePagination
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListCampaignsResponsePagination`
        """
        model = ListCampaignsResponsePagination()
        if include_optional:
            return ListCampaignsResponsePagination(
                items = [
                    upstream_client.models.list_campaigns_response_item.ListCampaignsResponseItem(
                        id = 56, 
                        name = '', 
                        location = upstream_client.models.location.Location(
                            bbox_west = 1.337, 
                            bbox_east = 1.337, 
                            bbox_south = 1.337, 
                            bbox_north = 1.337, ), 
                        description = '', 
                        contact_name = '', 
                        contact_email = '', 
                        start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        allocation = '', 
                        summary = upstream_client.models.summary_list_campaigns.SummaryListCampaigns(
                            sensor_types = [
                                ''
                                ], 
                            variable_names = [
                                ''
                                ], ), 
                        geometry = null, )
                    ],
                total = 56,
                page = 56,
                size = 56,
                pages = 56
            )
        else:
            return ListCampaignsResponsePagination(
                items = [
                    upstream_client.models.list_campaigns_response_item.ListCampaignsResponseItem(
                        id = 56, 
                        name = '', 
                        location = upstream_client.models.location.Location(
                            bbox_west = 1.337, 
                            bbox_east = 1.337, 
                            bbox_south = 1.337, 
                            bbox_north = 1.337, ), 
                        description = '', 
                        contact_name = '', 
                        contact_email = '', 
                        start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        allocation = '', 
                        summary = upstream_client.models.summary_list_campaigns.SummaryListCampaigns(
                            sensor_types = [
                                ''
                                ], 
                            variable_names = [
                                ''
                                ], ), 
                        geometry = null, )
                    ],
                total = 56,
                page = 56,
                size = 56,
                pages = 56,
        )
        """

    def testListCampaignsResponsePagination(self):
        """Test ListCampaignsResponsePagination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
