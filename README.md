# Preface #

This document describes the functionality provided by the jbossdm-restarter plugin.

See the **XL Deploy Reference Manual** for background information on XL Deploy and deployment concepts.

# Overview #

The jbossdm-restarter plugin is a XL Deploy plugin that adds capability for restarting a JBoss domain, standalone server or profile when deploying to it.

## Requirements

* **XL Deploy requirements**
	* **XL Deploy**: version 4.5+
	* **Other XL Deploy Plugins**: jbossdm-plugin 4.5+

## Types ##

+ restartContainer: Must be set to true if restart needs to be performed.
+ startScript: Start script to start the container (must be located on the server)
+ stopScript: Stop script to start the container (must be located on the server)
