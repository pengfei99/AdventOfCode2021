from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, when, lag, first, substring, sum, concat, row_number
from pyspark.sql.types import IntegerType, StructType, StructField, StringType
from pyspark.sql.window import Window


def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


############################# Part 1 ################################################
def part1(df):
    win_spec = Window.orderBy("total")
    df1 = df.withColumn("sum_n1", sum("n1").over(win_spec)) \
        .withColumn("sum_n2", sum("n2").over(win_spec)) \
        .withColumn("sum_n3", sum("n3").over(win_spec)) \
        .withColumn("sum_n4", sum("n4").over(win_spec)) \
        .withColumn("sum_n5", sum("n5").over(win_spec)) \
        .withColumn("sum_n6", sum("n6").over(win_spec)) \
        .withColumn("sum_n7", sum("n7").over(win_spec)) \
        .withColumn("sum_n8", sum("n8").over(win_spec)) \
        .withColumn("sum_n9", sum("n9").over(win_spec)) \
        .withColumn("sum_n10", sum("n10").over(win_spec)) \
        .withColumn("sum_n11", sum("n11").over(win_spec)) \
        .withColumn("sum_n12", sum("n12").over(win_spec))
    df1.show()
    df2 = df1.withColumn("n1_maj_val", when(col("sum_n1") > (col("total") / 2), "1").otherwise("0")) \
        .withColumn("n2_maj_val", when(col("sum_n2") > (col("total") / 2), "1").otherwise("0")) \
        .withColumn("n3_maj_val", when(col("sum_n3") > (col("total") / 2), "1").otherwise("0")) \
        .withColumn("n4_maj_val", when(col("sum_n4") > (col("total") / 2), "1").otherwise("0")) \
        .withColumn("n5_maj_val", when(col("sum_n5") > (col("total") / 2), "1").otherwise("0")) \
        .withColumn("n6_maj_val", when(col("sum_n6") > (col("total") / 2), "1").otherwise("0")) \
        .withColumn("n7_maj_val", when(col("sum_n7") > (col("total") / 2), "1").otherwise("0")) \
        .withColumn("n8_maj_val", when(col("sum_n8") > (col("total") / 2), "1").otherwise("0")) \
        .withColumn("n9_maj_val", when(col("sum_n9") > (col("total") / 2), "1").otherwise("0")) \
        .withColumn("n10_maj_val", when(col("sum_n10") > (col("total") / 2), "1").otherwise("0")) \
        .withColumn("n11_maj_val", when(col("sum_n11") > (col("total") / 2), "1").otherwise("0")) \
        .withColumn("n12_maj_val", when(col("sum_n12") > (col("total") / 2), "1").otherwise("0"))
    df2.show()
    df3 = df2.withColumn("gamma", concat(col("n1_maj_val"), col("n2_maj_val"), col("n3_maj_val"), col("n4_maj_val"),
                                         col("n5_maj_val"), col("n6_maj_val"), col("n7_maj_val"), col("n8_maj_val"),
                                         col("n9_maj_val"), col("n10_maj_val"), col("n11_maj_val"), col("n12_maj_val")))
    df3.select("gamma").show(1)
    return df2


############################# Part 2 ################################################

def part2(df):
    df1 = df.drop("total", "sum_n1", "sum_n2", "sum_n3", "sum_n4", "sum_n5", "sum_n6", "sum_n7", "sum_n8", "sum_n9",
                  "sum_n10", "sum_n11", "sum_n12")

    df1.filter(col("n1") == col("n1_maj_val")) \
        .filter(col("n2") == col("n2_maj_val")) \
        .filter(col("n3") == col("n3_maj_val")) \
        .filter(col("n4") == col("n4_maj_val")) \
        .filter(col("n5") == col("n5_maj_val")) \
        .filter(col("n6") == col("n6_maj_val")) \
        .filter(col("n7") == col("n7_maj_val")) \
        .filter(col("n8") == col("n8_maj_val")) \
        .filter(col("n9") == col("n9_maj_val")) \
        .show()

    tmp = df1.filter(col("n1") == 0)
    tmp = tmp.filter(col("n2") != col("n2_maj_val"))
    tmp = tmp.filter(col("n3") != col("n3_maj_val"))
    tmp = tmp.filter(col("n4") != col("n4_maj_val"))
    tmp = tmp.filter(col("n5") != col("n5_maj_val"))
    tmp = tmp.filter(col("n6") != col("n6_maj_val"))
    tmp = tmp.filter(col("n7") != col("n7_maj_val"))
    tmp = tmp.filter(col("n8") != col("n8_maj_val"))
    tmp = tmp.filter(col("n9") != col("n9_maj_val"))
    tmp.show()


def main():
    spark = SparkSession.builder.master("local[4]").appName("getDepth").getOrCreate()
    path = "data/number.csv"
    schema = StructType([
        StructField("num", StringType(), True)
    ])
    df = spark.read.csv(path, header=False, schema=schema)
    total_num = df.count()
    print(f"total row number: {total_num}")

    # convert string to int
    df_source = df\
        .withColumn("n1", substring("num", 1, 1).cast(IntegerType())) \
        .withColumn("n2", substring("num", 2, 1).cast(IntegerType())) \
        .withColumn("n3", substring("num", 3, 1).cast(IntegerType())) \
        .withColumn("n4", substring("num", 4, 1).cast(IntegerType())) \
        .withColumn("n5", substring("num", 5, 1).cast(IntegerType())) \
        .withColumn("n6", substring("num", 6, 1).cast(IntegerType())) \
        .withColumn("n7", substring("num", 7, 1).cast(IntegerType())) \
        .withColumn("n8", substring("num", 8, 1).cast(IntegerType())) \
        .withColumn("n9", substring("num", 9, 1).cast(IntegerType())) \
        .withColumn("n10", substring("num", 10, 1).cast(IntegerType())) \
        .withColumn("n11", substring("num", 11, 1).cast(IntegerType())) \
        .withColumn("n12", substring("num", 12, 1).cast(IntegerType())) \
        .withColumn("total", lit(total_num))
    win_spec = Window.partitionBy("total").orderBy("total")
    df_source=df_source.withColumn("id", row_number().over(win_spec))
    df_source.show(5)
    df_source.printSchema()

    # part1
    df_with_maj = part1(df_source)
    gamma = binaryToDecimal(110111001001)
    print(f"gamma: {gamma}")
    epsilon = binaryToDecimal(1000110110)
    print(f"epsilon: {epsilon}")
    print(f"power consumption: {gamma * epsilon}")

    """ the output of part1
     +------------+
|       gamma| epsilon
+------------+
|1101 1100 1001| 001000110110
+------------+
    """

    # part2, can't find a way to solve part with dataframe!
    part2(df_with_maj)
    oxy = binaryToDecimal(110111001011)
    print(f"oxygen: {oxy}")
    co2 = binaryToDecimal(1000110111)
    print(f"co2: {co2}")
    print(f"life support rating: {oxy * co2}")

    print(binaryToDecimal(1010))


"""
oxygen generator rating = 110111001011
co2: 1000110111

oxy:3573
co2:289
"""

if __name__ == "__main__":
    main()
