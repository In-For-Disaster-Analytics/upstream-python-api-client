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

from upstream_client.models.line_string_coordinates_inner import LineStringCoordinatesInner

class TestLineStringCoordinatesInner(unittest.TestCase):
    """LineStringCoordinatesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LineStringCoordinatesInner:
        """Test LineStringCoordinatesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LineStringCoordinatesInner`
        """
        model = LineStringCoordinatesInner()
        if include_optional:
            return LineStringCoordinatesInner(
            )
        else:
            return LineStringCoordinatesInner(
        )
        """

    def testLineStringCoordinatesInner(self):
        """Test LineStringCoordinatesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
