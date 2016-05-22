

*********************************************************************

[![Build Status](https://travis-ci.org/snowch/bluemix-spark-examples.png)](https://travis-ci.org/snowch/bluemix-spark-examples) 


(click the icon and then click 'View Log' in travis-ci to view the build output and the test results from running the examples against live services)

*********************************************************************

#### Overview

This project has two examples that use the high performance [Stocator](https://github.com/SparkTC/stocator) Objectstore spark library.  The examples:

- process an Apache 2.0 LICENSE file and push the summary of word counts to an objectstore container (ExamplePush)
- connect to objectstore and pull the summary word count data into the spark environment (ExamplePull)

The examples are run by gradle (you do *not* need to know or install gradle).  Gradle uses a simple script, [build.gradle](./build.gradle) that contains two main tasks 'ExamplePush' and 'ExamplePull'.  Inspect these tasks in build.gradle for details - you do *not* need to have experience with gradle to understand this file.  Read the comments to understand what is being done.

The python spark scripts are [exporttoswift.py](./exporttoswift.py) and [importfromswift.py](./importfromswift.py).


*********************************************************************

#### Pre-requisites

- Access to a Bluemix Spark service instance (e.g. free tier)
- Objectstore container details (e.g. Free tier on Bluemix, or Softlayer account)
- Your local machine is OS/X or Linux (if you are using Windows, Cygwin *should* work - see [here](http://stackoverflow.com/questions/37315709/bluemix-spark-as-a-service-how-to-run-spark-submit-sh-with-cygwin))
- Java 8 JDK installed on your local machine [download](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
- Git client installed on your local machine [download](https://git-scm.com/downloads)

*********************************************************************

#### Instructions

- Clone this repository `git clone https://github.com/snowch/bluemix-spark-examples.git`
- Change into the cloned folder `cd bluemix-spark-examples`
- Save your spark service vcap.json into this folder (see [vcap.json_template](../../vcap.json_template) for an example or see the [docs](https://console.ng.bluemix.net/docs/services/AnalyticsforApacheSpark/index-gentopic3.html#genTopProcId4) for more info)
- Copy connection.properties_template `cp connection.properties_template connection.properties`
- Next edit the connection.properties file to add the details for your Objectstore service:

```bash
objectstore_auth_url
objectstore_tenant
objectsore_username
objectstore_password
objectstore_region
objectstore_auth_method
```

- Finally, run this example by changing into this directory (`cd ./examples/Objectstore`) and executing:

```
./gradlew ExamplePush
```
Or
```
./gradlew ExamplePull
```

**NOTE:** The connection.properties and vcap.json files are stored in the top level folder and not in the examples/Objectstore folder because those files are shared between all of the examples.
