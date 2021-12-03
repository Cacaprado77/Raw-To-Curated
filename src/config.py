from pyspark.sql import SparkSession


class Configs:
    def __init__(self, appName: str):
        self.appName = appName

    def spark_session(self) -> SparkSession:
        """Creates a SparkSession with specified app_name"""
        spark = SparkSession \
            .builder \
            .master("local[*]") \
            .appName(self.appName) \
            .config("spark.driver.extraClassPath", "jtds-1.3.1.jar") \
            .config("spark.executor.extraClassPath", "jtds-1.3.1.jar") \
            .getOrCreate()
        
        return spark
 