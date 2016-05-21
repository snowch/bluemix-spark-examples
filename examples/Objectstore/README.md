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
- Save your `vcap.json` into this folder (see the `vcap.json_template` for an example and [the bluemix docs](https://console.ng.blue mix.net/docs/services/AnalyticsforApacheSpark/index-gentopic3.html#genTopProcId4) for more info)
- Copy connection.properties_template `cp connection.properties_template connection.properties`
- Next edit the `connection.properties` file with values for your Objectstore service:

```bash
### auth url ###

# SoftLayer Dallas    > E.g. https://dal05.objectstorage.softlayer.net/auth/v1.0/
# Bluemix Keystone V3 > https://identity.open.softlayer.com/v3/auth/tokens
objectstore_auth_url:https://identity.open.softlayer.com/v3/auth/tokens

### tenant ###

# Bluemix Keystone V3 > use project_id
objectstore_tenant:changeme

### username ###

# SoftLayer Dallas    > username
# Bluemix Keystone V3 > user_id
objectstore_username:changeme

### password ###

# SoftLayer Dallas    > API key
# Bluemix Keystone V3 > Password
objectstore_password:changeme

### region ###

# SoftLayer Dallas    > E.g. dal05
# Bluemix Keystone V3 > dallas
objectstore_region:dallas

### auth method ###

# SoftLayer Dallas    > swiftauth
# Bluemix Keystone V3 > keystoneV3
objectstore_auth_method:keystoneV3

```

- Finally, run this example by changing into this directory (`./examples/Objectstore`) and executing:

```
./gradlew ExamplePush
```
Or
```
./gradlew ExamplePull
```
