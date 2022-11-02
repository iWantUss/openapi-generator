# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import collections
import unittest
from unittest.mock import patch

import urllib3

import petstore_api
from petstore_api.paths.fake_query_param_with_json_content_type import get  # noqa: E501
from petstore_api import configuration, schemas, api_client

from ... import ApiTestMixin, ParamTestCase


class TestFakeQueryParamWithJsonContentType(ApiTestMixin, unittest.TestCase):
    """
    FakeQueryParamWithJsonContentType unit test stubs
        query param with json content-type  # noqa: E501
    """
    @patch.object(urllib3.PoolManager, 'request')
    def test_get(self, mock_request):
        used_api_client = api_client.ApiClient()
        api = get.ApiForget(api_client=used_api_client)

        response_json = {}
        body = self.json_bytes(response_json)
        mock_request.return_value = self.response(body)

        test_cases = (
            ParamTestCase(
                None,
                'null'
            ),
            ParamTestCase(
                1,
                '1'
            ),
            ParamTestCase(
                3.14,
                '3.14'
            ),
            ParamTestCase(
                'blue',
                '%22blue%22'
            ),
            ParamTestCase(
                'hello world',
                '%22hello%20world%22'
            ),
            ParamTestCase(
                '',
                '%22%22'
            ),
            ParamTestCase(
                True,
                'true'
            ),
            ParamTestCase(
                False,
                'false'
            ),
            ParamTestCase(
                [],
                '%5B%5D'
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                '%5B%22blue%22%2C%22black%22%2C%22brown%22%5D'
            ),
            ParamTestCase(
                {},
                '%7B%7D'
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                '%7B%22R%22%3A100%2C%22G%22%3A200%2C%22B%22%3A150%7D'
            ),
        )

        for test_case in test_cases:
            api_response = api.get(query_params={'someParam': test_case.payload})
            self.assert_pool_manager_request_called_with(
                mock_request,
                f'http://petstore.swagger.io:80/v2/fake/queryParamWithJsonContentType?someParam={test_case.expected_serialization}',
                body=None,
                method='GET',
                content_type=None,
                accept_content_type='application/json',
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.AnyTypeSchema)
            assert isinstance(api_response.body, schemas.frozendict.frozendict)
            assert isinstance(api_response.headers, schemas.Unset)
            assert api_response.response.status == 200


if __name__ == '__main__':
    unittest.main()
