from __future__ import annotations

from dataclasses import dataclass
from typing import List

from cognite.extractorutils.configtools import BaseConfig
from cognite.extractorutils.configtools import RawStateStoreConfig
from cognite.extractorutils.configtools import StateStoreConfig


@dataclass
class ApiConfig:
    url: str
    sites: List[str]


@dataclass
class ExtractorConfig:
    state_store: StateStoreConfig = StateStoreConfig(
        local=None,
        raw=RawStateStoreConfig(database="src:002:opcua:db:state", table="datapoints", upload_interval=5),
    )

    create_assets: bool = False
    upload_interval: int = 5  # Automatically trigger an upload each m seconds when run as a thread
    parallelism: int = 2


@dataclass
class BackFillConfig:
    enabled: bool
    history_days: int


@dataclass
class FrontFillConfig:
    enabled: bool
    continuous: bool
    lookback_min: float


@dataclass
class IceCreamFactoryConfig(BaseConfig):
    api: ApiConfig
    backfill: BackFillConfig
    frontfill: FrontFillConfig
    oee_timeseries_dataset_ext_id: str  # ext id of dataset for oee timeseries. Used to populate timeseries in the correct dataset
    extractor: ExtractorConfig
