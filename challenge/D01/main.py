from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, when, lag
from pyspark.sql.types import IntegerType
from pyspark.sql.window import Window


############################# Part 1 ################################################
def part1(df1):
    # define a window spec, because we don't want to destroy the origin order, we order by the df with a dummy
    # value
    win_spec = Window.orderBy(lit(1))
    df2 = df1.withColumn("num2", lag("num").over(win_spec))
    df2.show()
    # collect will return the dataframe as an Array of rows
    # To get the col value of the first row, see below
    # base = df2.filter(col("row_num") == 1).collect()[0]["num"]
    # print(f"base value: {base}")

    df3 = df2.withColumn("status", when(df2.num2.isNull(), "na")
                         .when(df2.num2 > df2.num, "dec")
                         .when(df2.num2 < df2.num, "inc")
                         .otherwise("equal"))

    df3.show()
    df3.groupBy("status").count().show()



############################# Part 2 ################################################
def part2(df1):
    # define a window spec, because we don't want to destroy the origin order, we order by the df with a dummy
    # value
    win_spec = Window.orderBy(lit(1))
    # Step1: Create the three column for 3 consecutive number
    df2 = df1.withColumn("num2", lag("num").over(win_spec)) \
        .withColumn("num3", lag("num", 2).over(win_spec))
    df2.show()
    # Step2: Do the sum of the three column
    df3 = df2.withColumn("sum", when(df2.num2.isNull(), 0)
                         .when(df2.num3.isNull(), 0)
                         .otherwise(df2.num + df2.num2 + df2.num3))
    df3.show()
    # clean the df to make it like
    df4 = df3.filter(col("sum") > 0).drop("num", "num2", "num3").withColumnRenamed("sum", "num")
    df4.show()
    part1(df4)


def main():
    spark = SparkSession.builder.master("local[4]").appName("getDepth").getOrCreate()
    path = "data/number.csv"
    df = spark.read.option("header", "true").csv(path)
    # convert string to int
    df_source = df.select(col("num").cast(IntegerType()))
    df_source.show(5)
    df_source.printSchema()

    # part1
    part1(df_source)

    """ the output of part1
+------+-----+
|status|count|
+------+-----+
|    na|    1|
|   inc| 1462|
|   dec|  537|
+------+-----+
The output of part2
+------+-----+
|status|count|
+------+-----+
|    na|    1|
| equal|   45|
|   inc| 1497|
|   dec|  455|
+------+-----+
    """

    # part2
    part2(df_source)


if __name__ == "__main__":
    main()
