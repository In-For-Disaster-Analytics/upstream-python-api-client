# ListCampaignsResponseItemGeometry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bbox** | [**Bbox**](Bbox.md) |  | [optional] 
**type** | **str** |  | 
**coordinates** | **List[List[List[LineStringCoordinatesInner]]]** |  | 
**geometries** | [**List[GeometryCollectionGeometriesInner]**](GeometryCollectionGeometriesInner.md) |  | 

## Example

```python
from upstream_api_client.models.list_campaigns_response_item_geometry import ListCampaignsResponseItemGeometry

# TODO update the JSON string below
json = "{}"
# create an instance of ListCampaignsResponseItemGeometry from a JSON string
list_campaigns_response_item_geometry_instance = ListCampaignsResponseItemGeometry.from_json(json)
# print the JSON string representation of the object
print(ListCampaignsResponseItemGeometry.to_json())

# convert the object into a dict
list_campaigns_response_item_geometry_dict = list_campaigns_response_item_geometry_instance.to_dict()
# create an instance of ListCampaignsResponseItemGeometry from a dict
list_campaigns_response_item_geometry_from_dict = ListCampaignsResponseItemGeometry.from_dict(list_campaigns_response_item_geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


