# UpdateSensorStatisticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sensor_id** | **int** |  | 
**updated** | **bool** |  | 

## Example

```python
from upstream_api_client.models.update_sensor_statistics_response import UpdateSensorStatisticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSensorStatisticsResponse from a JSON string
update_sensor_statistics_response_instance = UpdateSensorStatisticsResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateSensorStatisticsResponse.to_json())

# convert the object into a dict
update_sensor_statistics_response_dict = update_sensor_statistics_response_instance.to_dict()
# create an instance of UpdateSensorStatisticsResponse from a dict
update_sensor_statistics_response_from_dict = UpdateSensorStatisticsResponse.from_dict(update_sensor_statistics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


