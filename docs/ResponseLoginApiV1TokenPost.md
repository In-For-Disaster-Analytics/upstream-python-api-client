# ResponseLoginApiV1TokenPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**token_type** | **str** |  | [optional] 

## Example

```python
from upstream_api_client.models.response_login_api_v1_token_post import ResponseLoginApiV1TokenPost

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseLoginApiV1TokenPost from a JSON string
response_login_api_v1_token_post_instance = ResponseLoginApiV1TokenPost.from_json(json)
# print the JSON string representation of the object
print(ResponseLoginApiV1TokenPost.to_json())

# convert the object into a dict
response_login_api_v1_token_post_dict = response_login_api_v1_token_post_instance.to_dict()
# create an instance of ResponseLoginApiV1TokenPost from a dict
response_login_api_v1_token_post_from_dict = ResponseLoginApiV1TokenPost.from_dict(response_login_api_v1_token_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


