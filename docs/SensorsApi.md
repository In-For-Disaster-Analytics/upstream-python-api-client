# upstream_api_client.SensorsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_delete**](SensorsApi.md#delete_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_delete) | **DELETE** /api/v1/campaigns/{campaign_id}/stations/{station_id}/sensors | Delete Sensor
[**force_update_sensor_statistics_api_v1_campaigns_campaign_id_stations_station_id_sensors_statistics_post**](SensorsApi.md#force_update_sensor_statistics_api_v1_campaigns_campaign_id_stations_station_id_sensors_statistics_post) | **POST** /api/v1/campaigns/{campaign_id}/stations/{station_id}/sensors/statistics | Force Update Sensor Statistics
[**force_update_single_sensor_statistics_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_statistics_post**](SensorsApi.md#force_update_single_sensor_statistics_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_statistics_post) | **POST** /api/v1/campaigns/{campaign_id}/stations/{station_id}/sensors/{sensor_id}/statistics | Force Update Single Sensor Statistics
[**get_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_get**](SensorsApi.md#get_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_get) | **GET** /api/v1/campaigns/{campaign_id}/stations/{station_id}/sensors/{sensor_id} | Get Sensor
[**list_sensors_api_v1_campaigns_campaign_id_stations_station_id_sensors_get**](SensorsApi.md#list_sensors_api_v1_campaigns_campaign_id_stations_station_id_sensors_get) | **GET** /api/v1/campaigns/{campaign_id}/stations/{station_id}/sensors | List Sensors
[**partial_update_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_patch**](SensorsApi.md#partial_update_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_patch) | **PATCH** /api/v1/campaigns/{campaign_id}/stations/{station_id}/sensors/{sensor_id} | Partial Update Sensor
[**update_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_put**](SensorsApi.md#update_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_put) | **PUT** /api/v1/campaigns/{campaign_id}/stations/{station_id}/sensors/{sensor_id} | Update Sensor


# **delete_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_delete**
> delete_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_delete(campaign_id, station_id)

Delete Sensor

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import upstream_api_client
from upstream_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = upstream_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with upstream_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = upstream_api_client.SensorsApi(api_client)
    campaign_id = 56 # int | 
    station_id = 56 # int | 

    try:
        # Delete Sensor
        api_instance.delete_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_delete(campaign_id, station_id)
    except Exception as e:
        print("Exception when calling SensorsApi->delete_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**|  | 
 **station_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **force_update_sensor_statistics_api_v1_campaigns_campaign_id_stations_station_id_sensors_statistics_post**
> ForceUpdateSensorStatisticsResponse force_update_sensor_statistics_api_v1_campaigns_campaign_id_stations_station_id_sensors_statistics_post(campaign_id, station_id)

Force Update Sensor Statistics

Force update sensor statistics for all sensors in the station

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import upstream_api_client
from upstream_api_client.models.force_update_sensor_statistics_response import ForceUpdateSensorStatisticsResponse
from upstream_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = upstream_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with upstream_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = upstream_api_client.SensorsApi(api_client)
    campaign_id = 56 # int | 
    station_id = 56 # int | 

    try:
        # Force Update Sensor Statistics
        api_response = api_instance.force_update_sensor_statistics_api_v1_campaigns_campaign_id_stations_station_id_sensors_statistics_post(campaign_id, station_id)
        print("The response of SensorsApi->force_update_sensor_statistics_api_v1_campaigns_campaign_id_stations_station_id_sensors_statistics_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SensorsApi->force_update_sensor_statistics_api_v1_campaigns_campaign_id_stations_station_id_sensors_statistics_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**|  | 
 **station_id** | **int**|  | 

### Return type

[**ForceUpdateSensorStatisticsResponse**](ForceUpdateSensorStatisticsResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **force_update_single_sensor_statistics_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_statistics_post**
> UpdateSensorStatisticsResponse force_update_single_sensor_statistics_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_statistics_post(campaign_id, station_id, sensor_id)

Force Update Single Sensor Statistics

Force update sensor statistics for a single sensor

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import upstream_api_client
from upstream_api_client.models.update_sensor_statistics_response import UpdateSensorStatisticsResponse
from upstream_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = upstream_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with upstream_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = upstream_api_client.SensorsApi(api_client)
    campaign_id = 56 # int | 
    station_id = 56 # int | 
    sensor_id = 56 # int | 

    try:
        # Force Update Single Sensor Statistics
        api_response = api_instance.force_update_single_sensor_statistics_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_statistics_post(campaign_id, station_id, sensor_id)
        print("The response of SensorsApi->force_update_single_sensor_statistics_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_statistics_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SensorsApi->force_update_single_sensor_statistics_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_statistics_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**|  | 
 **station_id** | **int**|  | 
 **sensor_id** | **int**|  | 

### Return type

[**UpdateSensorStatisticsResponse**](UpdateSensorStatisticsResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_get**
> GetSensorResponse get_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_get(station_id, sensor_id, campaign_id)

Get Sensor

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import upstream_api_client
from upstream_api_client.models.get_sensor_response import GetSensorResponse
from upstream_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = upstream_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with upstream_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = upstream_api_client.SensorsApi(api_client)
    station_id = 56 # int | 
    sensor_id = 56 # int | 
    campaign_id = 56 # int | 

    try:
        # Get Sensor
        api_response = api_instance.get_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_get(station_id, sensor_id, campaign_id)
        print("The response of SensorsApi->get_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SensorsApi->get_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **int**|  | 
 **sensor_id** | **int**|  | 
 **campaign_id** | **int**|  | 

### Return type

[**GetSensorResponse**](GetSensorResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sensors_api_v1_campaigns_campaign_id_stations_station_id_sensors_get**
> ListSensorsResponsePagination list_sensors_api_v1_campaigns_campaign_id_stations_station_id_sensors_get(campaign_id, station_id, page=page, limit=limit, variable_name=variable_name, units=units, alias=alias, description_contains=description_contains, postprocess=postprocess, sort_by=sort_by, sort_order=sort_order)

List Sensors

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import upstream_api_client
from upstream_api_client.models.list_sensors_response_pagination import ListSensorsResponsePagination
from upstream_api_client.models.sort_field import SortField
from upstream_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = upstream_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with upstream_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = upstream_api_client.SensorsApi(api_client)
    campaign_id = 56 # int | 
    station_id = 56 # int | 
    page = 1 # int |  (optional) (default to 1)
    limit = 20 # int |  (optional) (default to 20)
    variable_name = 'variable_name_example' # str | Filter sensors by variable name (partial match) (optional)
    units = 'units_example' # str | Filter sensors by units (exact match) (optional)
    alias = 'alias_example' # str | Filter sensors by alias (partial match) (optional)
    description_contains = 'description_contains_example' # str | Filter sensors by text in description (partial match) (optional)
    postprocess = True # bool | Filter sensors by postprocess flag (optional)
    sort_by = upstream_api_client.SortField() # SortField | Sort sensors by field (optional)
    sort_order = 'asc' # str | Sort order (asc or desc) (optional) (default to 'asc')

    try:
        # List Sensors
        api_response = api_instance.list_sensors_api_v1_campaigns_campaign_id_stations_station_id_sensors_get(campaign_id, station_id, page=page, limit=limit, variable_name=variable_name, units=units, alias=alias, description_contains=description_contains, postprocess=postprocess, sort_by=sort_by, sort_order=sort_order)
        print("The response of SensorsApi->list_sensors_api_v1_campaigns_campaign_id_stations_station_id_sensors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SensorsApi->list_sensors_api_v1_campaigns_campaign_id_stations_station_id_sensors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**|  | 
 **station_id** | **int**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**|  | [optional] [default to 20]
 **variable_name** | **str**| Filter sensors by variable name (partial match) | [optional] 
 **units** | **str**| Filter sensors by units (exact match) | [optional] 
 **alias** | **str**| Filter sensors by alias (partial match) | [optional] 
 **description_contains** | **str**| Filter sensors by text in description (partial match) | [optional] 
 **postprocess** | **bool**| Filter sensors by postprocess flag | [optional] 
 **sort_by** | [**SortField**](.md)| Sort sensors by field | [optional] 
 **sort_order** | **str**| Sort order (asc or desc) | [optional] [default to &#39;asc&#39;]

### Return type

[**ListSensorsResponsePagination**](ListSensorsResponsePagination.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_patch**
> SensorCreateResponse partial_update_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_patch(campaign_id, station_id, sensor_id, sensor_update)

Partial Update Sensor

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import upstream_api_client
from upstream_api_client.models.sensor_create_response import SensorCreateResponse
from upstream_api_client.models.sensor_update import SensorUpdate
from upstream_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = upstream_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with upstream_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = upstream_api_client.SensorsApi(api_client)
    campaign_id = 56 # int | 
    station_id = 56 # int | 
    sensor_id = 56 # int | 
    sensor_update = upstream_api_client.SensorUpdate() # SensorUpdate | 

    try:
        # Partial Update Sensor
        api_response = api_instance.partial_update_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_patch(campaign_id, station_id, sensor_id, sensor_update)
        print("The response of SensorsApi->partial_update_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SensorsApi->partial_update_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**|  | 
 **station_id** | **int**|  | 
 **sensor_id** | **int**|  | 
 **sensor_update** | [**SensorUpdate**](SensorUpdate.md)|  | 

### Return type

[**SensorCreateResponse**](SensorCreateResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_put**
> SensorCreateResponse update_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_put(sensor_id, station_id, campaign_id, sensor_update)

Update Sensor

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import upstream_api_client
from upstream_api_client.models.sensor_create_response import SensorCreateResponse
from upstream_api_client.models.sensor_update import SensorUpdate
from upstream_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = upstream_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with upstream_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = upstream_api_client.SensorsApi(api_client)
    sensor_id = 56 # int | 
    station_id = 56 # int | 
    campaign_id = 56 # int | 
    sensor_update = upstream_api_client.SensorUpdate() # SensorUpdate | 

    try:
        # Update Sensor
        api_response = api_instance.update_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_put(sensor_id, station_id, campaign_id, sensor_update)
        print("The response of SensorsApi->update_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SensorsApi->update_sensor_api_v1_campaigns_campaign_id_stations_station_id_sensors_sensor_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_id** | **int**|  | 
 **station_id** | **int**|  | 
 **campaign_id** | **int**|  | 
 **sensor_update** | [**SensorUpdate**](SensorUpdate.md)|  | 

### Return type

[**SensorCreateResponse**](SensorCreateResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

