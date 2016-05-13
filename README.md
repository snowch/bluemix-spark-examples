*********************************************************************

This repository contains example projects to help you quickly get started with Spark as a Service, spark-submit.sh. 

Note that project has a dependency on the following issue: https://github.com/snowch/bluemix-spark-submit-examples/issues/1

*********************************************************************

### Pre-requisites

#### Mandatory

- Access to a Bluemix Spark service instance
- Java 8 JDK installed on your local machine
- Git client installed on your local machine
- You are comfortable running commands in the terminal or console

#### Optional

- Cloudant account details (e.g. Free tier on Bluemix)
- dashDB account details (e.g. Free tier on Bluemix)
- Objectstore container details (e.g. Free tier on Bluemix, or Softlayer account)
- Elasticsearch cluster (e.g. Free trial on Compose.io)

*********************************************************************

### Setup Instructions

- Clone this repository `git clone https://github.com/snowch/bluemix-spark-submit-examples.git`
- Copy `connection.properties_template` to `connection.properties`
- Save your `vcap.json` in the cloned folder (see the `vcap.json_template` for an example and [the bluemix docs](https://console.ng.bluemix.net/docs/services/AnalyticsforApacheSpark/index-gentopic3.html#genTopProcId4) for more information)
- Follow the instructions in the README.md for your chosen [example](./examples/README.md)

*********************************************************************

### Contributing

Contributions are welcome.  Please send a pull request or contact me at chris.snow@uk.ibm.com to get involved.
