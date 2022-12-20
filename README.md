# Blog Post:Run PyFlink Jobs and UDFs on Ververica Platform

The accompanying code repo for the blog post above.

## What's included
The post goes over creating a new custom Flink image to be used instead of
the out-of-the-box image, in order to run PyFlink jobs and call python based UDF functions
in either pythong or java Jobs.

* Custom image Dockerfile: In the custom_image directory
* The java_python_udf folder: Contains the source code for a sample Java TableAPI job that
declares and calls a UDF function written in Python. The source code and POM of the job can be found in the "job" folder. The POM file already contains the pyflink dependency and is ready to go, if you'd like to package up the project JAR. The python UDF file can be found in the "udf" folder.
* 