from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from financedemopipeline.config.ConfigStore import *
from financedemopipeline.udfs.UDFs import *

def Script_0(spark: SparkSession) -> DataFrame:
    import time
    out0 = spark.sql("SELECT * FROM sample_data.finance.finance_data")
    time.sleep(10)
    out0 = spark.sql("SELECT * FROM sample_data.finance.finance_data")

    return out0
