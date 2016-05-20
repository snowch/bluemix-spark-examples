#### Overview

This example uses the [Stocator](https://github.com/SparkTC/stocator) spark library to:

- process an Apache 2.0 LICENSE file and push the summary of word counts to an objectstore container
- connect to objectstore and pull the summary word count data into the spark environment

The [build.gradle](./build.gradle) script contains two main tasks for the above behavior, with task names 'ExamplePush' and 'ExamplePull'.  Inspect these tasks for details.

*********************************************************************
#### Instructions

Complete the Setup Instructions in the main project [README](../../READM.md).  Next edit the `connection.properties` file in the main project folder so that it has the following properties that point to your Objectstore container:

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

Run this example by changing into this directory `./examples/Objectstore` then executing:

```
./gradlew ExamplePush
./gradlew ExamplePull
```

