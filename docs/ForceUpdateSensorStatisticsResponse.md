# ForceUpdateSensorStatisticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_sensor_ids** | **List[int]** |  | 
**total_updated** | **int** |  | 

## Example

```python
from upstream_api_client.models.force_update_sensor_statistics_response import ForceUpdateSensorStatisticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ForceUpdateSensorStatisticsResponse from a JSON string
force_update_sensor_statistics_response_instance = ForceUpdateSensorStatisticsResponse.from_json(json)
# print the JSON string representation of the object
print(ForceUpdateSensorStatisticsResponse.to_json())

# convert the object into a dict
force_update_sensor_statistics_response_dict = force_update_sensor_statistics_response_instance.to_dict()
# create an instance of ForceUpdateSensorStatisticsResponse from a dict
force_update_sensor_statistics_response_from_dict = ForceUpdateSensorStatisticsResponse.from_dict(force_update_sensor_statistics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


