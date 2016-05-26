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

import re
import sys
from operator import add

from pyspark import SparkContext
from pyspark.sql import SQLContext

if __name__ == "__main__":
    if len(sys.argv) != 8:
        print("Usage: importfromswift <auth url> <tenant> <username> <password> <region> <auth method> <container>", file=sys.stderr)
        exit(-1)

    os_auth_url      = sys.argv[1]
    os_tenant        = sys.argv[2]
    os_username      = sys.argv[3]
    os_password      = sys.argv[4]
    os_region        = sys.argv[5]
    os_auth_method   = sys.argv[6]
    os_container     = sys.argv[7]

    sc = SparkContext()

    # configure the Stocator swift library with our connection details

    prefix = "fs.swift2d.service." + os_region

    sc._jsc.hadoopConfiguration().set("fs.swift2d.impl","com.ibm.stocator.fs.ObjectStoreFileSystem")

    sc._jsc.hadoopConfiguration().set(prefix + ".auth.url",     os_auth_url)
    sc._jsc.hadoopConfiguration().set(prefix + ".public",       "true")
    sc._jsc.hadoopConfiguration().set(prefix + ".tenant",       os_tenant)
    sc._jsc.hadoopConfiguration().set(prefix + ".username",     os_username)
    sc._jsc.hadoopConfiguration().set(prefix + ".password",     os_password)
    sc._jsc.hadoopConfiguration().set(prefix + ".auth.method",  os_auth_method)

    if (os_auth_method != 'swiftauth'):
        sc._jsc.hadoopConfiguration().set(prefix + ".region",       os_region)

    sqlContext = SQLContext(sc)
    
    # Before running this script, build.gradle runs the script ./exporttoswift.py to create some data for us
    # in Objectstore.  This script loads that data.  The structure of the data looks like this:
    
    # counts                                                  04/18/2016 8:21 PM        0 KB
    # counts/_SUCCESS                                         04/18/2016 8:21 PM        0 KB
    # counts/part-00000-attempt_201604181921_0003_m_000000_2  04/18/2016 8:21 PM        6 KB

    swift_file_url = "swift2d://{0}.{1}/counts".format(os_container, os_region)

    # import the data

    imported_data = sc.textFile(swift_file_url)

    # now print out some of the imported data to standard out.  You can see this in the file stdout_xxx
    # created by spark-submit.sh

    print(">> Successfully imported data from objectstore 'imported_data.take(10)':")

    print(imported_data.take(10))
    
    sc.stop()
