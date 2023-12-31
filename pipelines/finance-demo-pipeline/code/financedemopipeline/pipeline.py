from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from financedemopipeline.config.ConfigStore import *
from financedemopipeline.udfs.UDFs import *
from prophecy.utils import *
from financedemopipeline.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Script_0 = Script_0(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/finance-demo-pipeline")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/finance-demo-pipeline", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/finance-demo-pipeline")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
