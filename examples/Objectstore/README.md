#### Overview

This example uses the [Stocator](https://github.com/SparkTC/stocator) spark library to:

- process an Apache 2.0 LICENSE file and push the summary of word counts to an objectstore container
- connect to objectstore and pull the summary word count data into the spark environment

The [build.gradle](./build.gradle) script contains two main tasks for the above behavior, with task names 'ExamplePush' and 'ExamplePull'.  Inspect these tasks in build.gradle for details - you do *not* need to have experience with gradle to understand this file.

*********************************************************************

### Pre-requisites

- Access to a Bluemix Spark service instance (e.g. free tier)
- Objectstore container details (e.g. Free tier on Bluemix, or Softlayer account)
- Your local machine is OS/X or Linux (Cygwin *should* work on Windows - see [here](http://stackoverflow.com/questions/37315709/bluemix-spark-as-a-service-how-to-run-spark-submit-sh-with-cygwin))
- Java 8 JDK installed on your local machine
- Git client installed on your local machine

*********************************************************************

### Setup Instructions

- Clone this repository `git clone https://github.com/snowch/bluemix-spark-examples.git`
- Save your `vcap.json` in the cloned folder (see the `vcap.json_template` for an example and [the bluemix docs](https://console.ng.bluemix.net/docs/services/AnalyticsforApacheSpark/index-gentopic3.html#genTopProcId4) for more information)
- Copy `connection.properties_template` to `connection.properties`
- Next edit the `connection.properties` file in the main project folder so that it has the following properties for your Objectstore instance:

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

Finally, run this example by changing into this directory (`./examples/Objectstore`) and executing:

```
./gradlew ExamplePush
```
Or
```
./gradlew ExamplePull
```
