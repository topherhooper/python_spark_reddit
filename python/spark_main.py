"""SimpleApp.py"""
from collections import OrderedDict
from pyspark import SparkContext, Row
from pyspark.sql import SparkSession


def parse_file(file_stream):
    sc = SparkContext("local", "Simple App")
    broadcaster = sc.broadcast(file_stream)

    numAs = broadcaster.filter(lambda s: 'a' in s).count()
    numBs = broadcaster.filter(lambda s: 'b' in s).count()

    print "Lines with a: %i, lines with b: %i" % (numAs, numBs)


def convert_to_row(d):
    return Row(**OrderedDict(sorted(d.items())))


def nsj_to_df(nsj, sc):
    spark = SparkSession(sc)

    # https://stackoverflow.com/questions/37584077/convert-a-standard-python-key-value-dictionary-list-to-pyspark-data-frame

    return sc.parallelize(nsj) \
        .map(convert_to_row) \
        .toDF()