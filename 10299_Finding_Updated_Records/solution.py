# Import your libraries
import pyspark

from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql.functions import col,row_number

# Start writing code
#ms_employee_salary.show()

w_spec = Window.partitionBy("id").orderBy(col("salary").desc())

df_rank = ms_employee_salary.filter(col("salary").isNotNull()).withColumn("rnum", row_number().over(w_spec))

df_top = df_rank.filter(col("rnum")==1).select("id","first_name","last_name","salary","department_id")

# To validate your solution, convert your final pySpark df to a pandas df
df_top.toPandas()
