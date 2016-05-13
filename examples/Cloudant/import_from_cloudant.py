#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from __future__ import print_function

import time
import sys
from operator import add

from pyspark import SparkContext
from pyspark.sql import SQLContext

if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: import_from_cloudant <cloudant hostname> <cloudant username> <cloudant password> <cloudant database>", file=sys.stderr)
        exit(-1)

    cl_hostname = sys.argv[1]
    cl_username = sys.argv[2]
    cl_password = sys.argv[3]
    cl_database = sys.argv[4]

    sc = SparkContext(appName="Cloudant data pull")

    sqlContext = SQLContext(sc)

    # Connect to database 'sales' and read schema using all documents as schema sample size
    cloudantdata = sqlContext.read.format("com.cloudant.spark") \
            .option("cloudant.host",cl_hostname) \
            .option("cloudant.username",cl_username) \
            .option("cloudant.password",cl_password) \
            .option("schemaSampleSize", -1) \
            .load(cl_database)

    print(cloudantdata.rdd.take(10))

    sc.stop()
