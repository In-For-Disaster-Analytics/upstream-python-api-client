# GetStationResponseGeometry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bbox** | [**Bbox**](Bbox.md) |  | [optional] 
**type** | **str** |  | 
**coordinates** | **List[List[List[LineStringCoordinatesInner]]]** |  | 
**geometries** | [**List[GeometryCollectionGeometriesInner]**](GeometryCollectionGeometriesInner.md) |  | 

## Example

```python
from upstream_api_client.models.get_station_response_geometry import GetStationResponseGeometry

# TODO update the JSON string below
json = "{}"
# create an instance of GetStationResponseGeometry from a JSON string
get_station_response_geometry_instance = GetStationResponseGeometry.from_json(json)
# print the JSON string representation of the object
print(GetStationResponseGeometry.to_json())

# convert the object into a dict
get_station_response_geometry_dict = get_station_response_geometry_instance.to_dict()
# create an instance of GetStationResponseGeometry from a dict
get_station_response_geometry_from_dict = GetStationResponseGeometry.from_dict(get_station_response_geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


