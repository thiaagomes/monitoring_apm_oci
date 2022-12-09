# Introduction

This is a simple python example to show python instrumentation using zipkin library and forward the traces onto OCI APM.

# Pre-Requisites and dependencies

Have python 3.0+ Version

$ pip3 install flask

$ pip3 install requests

$ pip3 install py_zipkin

# Find APM URL

Change `apm_upload_endpoint_url` variable value before starting. This is the APM data upload endpoint that you will need to retrieve from OCI console -> APM 

# How to run

$ python3 oci-apm.py

# How to test

$ curl http://127.0.0.1:5000/tracing

# Verify

Go to OCI console and verify the traces. OCI console -> APM -> Trace Explorer


