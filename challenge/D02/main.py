from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, when, lag, first
from pyspark.sql.types import IntegerType
from pyspark.sql.window import Window


############################# Part 1 ################################################
def part1(df):
    action_list = ["down", "forward", "up"]
    df1 = df.groupBy("action").sum("num")
    df1.show()
    df2 = df1.groupBy().pivot("action").agg(first(col("sum(num)")))
    df2.show()
    df3 = df2.withColumnRenamed("forward", "horizontal").withColumn("depth", col("down") - col("up"))
    df3.show()
    df4 = df3.withColumn("result", col("horizontal") * col("depth"))
    df4.show()


############################# Part 2 ################################################
def part2(df):
    rows = df.collect()
    aim = 0
    hor = 0
    depth = 0
    for row in rows:
        action = row["action"]
        num = row["num"]
        if action == "forward":
            hor = hor + num
            depth = depth + (num * aim)
        elif action == "up":
            aim = aim - num
        elif action == "down":
            aim = aim + num
    print(f"horizontal:{hor}, depth:{depth}, result:{hor*depth}")


def main():
    spark = SparkSession.builder.master("local[4]").appName("getDepth").getOrCreate()
    path = "data/number.csv"
    df = spark.read.option("header", "true").csv(path)
    # convert string to int
    df_source = df.select(col("action"), col("num").cast(IntegerType()))
    df_source.show(5)
    df_source.printSchema()

    # part1
    # part1(df_source)

    """ the output of part1
+----+----------+----+-----+-------+
|down|horizontal|  up|depth| result|
+----+----------+----+-----+-------+
|1927|      2018|1107|  820|1654760|
+----+----------+----+-----+-------+
    """

    # part2, can't find a way to solve part with dataframe!
    part2(df_source)


if __name__ == "__main__":
    main()
