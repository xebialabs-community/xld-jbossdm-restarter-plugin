# Preface #

This document describes the functionality provided by the jbossdm-restarter plugin.

See the **XL Deploy Reference Manual** for background information on XL Deploy and deployment concepts.

# CI status #

[![Build Status][xld-jbossdm-restarter-plugin-travis-image]][xld-jbossdm-restarter-plugin-travis-url]
[![Codacy Badge][xld-jbossdm-restarter-plugin-codacy-image] ][xld-jbossdm-restarter-plugin-codacy-url]
[![Code Climate][xld-jbossdm-restarter-plugin-code-climate-image] ][xld-jbossdm-restarter-plugin-code-climate-url]

[xld-jbossdm-restarter-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xld-jbossdm-restarter-plugin.svg?branch=master
[xld-jbossdm-restarter-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xld-jbossdm-restarter-plugin
[xld-jbossdm-restarter-plugin-codacy-image]: https://api.codacy.com/project/badge/Grade/0c1d76f521374e819f37e40ab6132e7b
[xld-jbossdm-restarter-plugin-codacy-url]: https://www.codacy.com/app/joris-dewinne/xld-jbossdm-restarter-plugin
[xld-jbossdm-restarter-plugin-code-climate-image]: https://codeclimate.com/github/xebialabs-community/xld-jbossdm-restarter-plugin/badges/gpa.svg
[xld-jbossdm-restarter-plugin-code-climate-url]: https://codeclimate.com/github/xebialabs-community/xld-jbossdm-restarter-plugin



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
