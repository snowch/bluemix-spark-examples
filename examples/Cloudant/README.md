#### Overview

##### Export to Cloudant

This example processes an Apache LICENSE file and uploads the summary table of wordcounts to Cloudant. A database will be created for you that holds this data.

This pattern is an example of uploading the results of batch processed data to a NoSQL store for random access rather than sequential access.

##### Import from Cloudant

This example runs the Export to Cloudant example, and then retrieves the data from the Export and prints 10 records to standard out.

*********************************************************************
#### Instructions

Make sure your connection.properties file has values set to point to the Cloudant account where you want the results saved:

```
cl_push_hostname:changeme.cloudant.com
cl_push_username:changeme
cl_push_password:changeme
```

See the [setup instructions](https://github.com/snowch/bluemix-spark-submit-examples) for more information on creating the connection.propertie file.

Run this example by changing into the current directory then executing:

- on *nix using:

```
../../gradlew ExamplePull
../../gradlew ExamplePush
```

- on Windows using:

```
../../gradlew.bat ExamplePull
../../gradlew.bat ExamplePush
```

*********************************************************************

