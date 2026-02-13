# Import your libraries
import pyspark

from pyspark.sql import functions as F
from pyspark.sql.window import Window

dfjoin = worker.join(title, worker.worker_id == title.worker_ref_id)

w = Window.orderBy(F.col("salary").desc())

dfrank = dfjoin.filter(F.col("salary").isNotNull()).withColumn("dense_rk",F.dense_rank().over(w))

dffilter = dfrank.filter(F.col("dense_rk")==1)

dffinal = dffilter.select(F.col("worker_title").alias("best_paid_title")).distinct()

# To validate your solution, convert your final pySpark df to a pandas df
dffinal.toPandas()
