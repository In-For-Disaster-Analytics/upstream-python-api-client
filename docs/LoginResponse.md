# LoginResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**token_type** | **str** |  | 

## Example

```python
from upstream_api_client.models.login_response import LoginResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LoginResponse from a JSON string
login_response_instance = LoginResponse.from_json(json)
# print the JSON string representation of the object
print(LoginResponse.to_json())

# convert the object into a dict
login_response_dict = login_response_instance.to_dict()
# create an instance of LoginResponse from a dict
login_response_from_dict = LoginResponse.from_dict(login_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


