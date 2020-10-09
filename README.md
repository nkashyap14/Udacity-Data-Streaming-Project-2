# Udacity-Data-Streaming-Project-2


## How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

By changing values within the SparkSession property parameters we were able to affect throughput aka processedRowsPerSecond. When this increases we are also increasing the latency of the data as we are able to process more of the data per second.

## What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

2 of the most efficient properties you could adjust in order to increase the throughput aka processedRowsPerSecond were spark.default.parallelism which effectively allows us to take advantage of the cores present throughout various nodes and thus increase througput. Another good property to fiddle with in order to affect latency and throughput was the number of partitions which by increasing you could effectively parallelize a larger portion of the computations you have to do across node thusly increasing processed nodes per second.
