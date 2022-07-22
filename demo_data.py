from tecton import BatchSource, SnowflakeConfig
from datetime import datetime


transactions = BatchSource(
    name="transactions",
    batch_config=SnowflakeConfig(
      database="SANIKA",
      schema="PUBLIC",
      table="STDDEV_VAR_TABLE",
      timestamp_field="TIMESTAMP",
    ),
)
