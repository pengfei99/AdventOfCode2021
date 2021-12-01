from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, when, lag
from pyspark.sql.types import IntegerType
from pyspark.sql.window import Window


def main():
    spark = SparkSession.builder.master("local[4]").appName("getDepth").getOrCreate()
    path = "data/number.csv"
    df = spark.read.option("header", "true").csv(path)
    # convert string to int
    df1 = df.select(col("num").cast(IntegerType()))
    df1.show(5)
    df1.printSchema()

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


if __name__ == "__main__":
    main()
