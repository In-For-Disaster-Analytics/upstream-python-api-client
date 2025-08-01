# coding: utf-8

"""
    Upstream Sensor Storage

    Sensor Storage for Upstream data

    The version of the OpenAPI document: 0.0.1
    Contact: wmobley@tacc.utexas.edu
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class PyTASPi(BaseModel):
    """
    PyTASPi
    """ # noqa: E501
    id: StrictInt
    username: StrictStr
    email: StrictStr
    first_name: StrictStr = Field(alias="firstName")
    last_name: StrictStr = Field(alias="lastName")
    institution: StrictStr
    institution_id: StrictInt = Field(alias="institutionId")
    department: StrictStr
    department_id: StrictInt = Field(alias="departmentId")
    citizenship: StrictStr
    citizenship_id: StrictInt = Field(alias="citizenshipId")
    source: StrictStr
    uid: StrictInt
    home_directory: StrictStr = Field(alias="homeDirectory")
    gid: StrictInt
    __properties: ClassVar[List[str]] = ["id", "username", "email", "firstName", "lastName", "institution", "institutionId", "department", "departmentId", "citizenship", "citizenshipId", "source", "uid", "homeDirectory", "gid"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PyTASPi from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PyTASPi from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "username": obj.get("username"),
            "email": obj.get("email"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "institution": obj.get("institution"),
            "institutionId": obj.get("institutionId"),
            "department": obj.get("department"),
            "departmentId": obj.get("departmentId"),
            "citizenship": obj.get("citizenship"),
            "citizenshipId": obj.get("citizenshipId"),
            "source": obj.get("source"),
            "uid": obj.get("uid"),
            "homeDirectory": obj.get("homeDirectory"),
            "gid": obj.get("gid")
        })
        return _obj


