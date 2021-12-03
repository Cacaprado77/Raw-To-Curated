from pyspark.sql import SparkSession, DataFrame
import sys
import os
sys.path.insert(0, '../src')
os.environ["PYTHONIOENCODING"] = "utf-8"


class Job:
    def __init__(self, sources: str, target: str, filename: str):
        self.sources = sources
        self.target = target
        self.filename = filename

        self._spark = SparkSession.builder.getOrCreate()

    def read_file(self) -> DataFrame:
        self.df = self._spark \
            .read \
            .parquet(self.sources + "/" + self.filename)

        return self.df

    def write_file(self):
        return self.df.write.mode("overwrite").parquet(self.target + "/" + self.filename)
        

if __name__ == "__main__":
    run = Job(
        "/home/caca/vscode/datalake_env/raw",
        "/home/caca/vscode/datalake_env/curated",
        "userdata1.parquet"
    )
    run.read_file()
    print("PARQUET FILE READ")

    run.write_file()
    print("PARQUET FILE SAVED IN CURATED ZONE")

    print("SUCCEED JOB!!!")
