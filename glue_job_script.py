import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from awsglue.transforms import ApplyMapping

# Basic Glue job setup
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Load raw data from Glue Catalog
datasource = glueContext.create_dynamic_frame.from_catalog(
    database = "sales_db",
    table_name = "raw_sales"
)

# Apply cleaning and type mapping
mapped = ApplyMapping.apply(
    frame = datasource,
    mappings = [
        ("timestamp", "string", "timestamp", "string"),
        ("product", "string", "product", "string"),
        ("quantity", "bigint", "quantity", "bigint"),
        ("price", "double", "price", "double")
    ]
)

# Write clean data to S3 in JSON format
glueContext.write_dynamic_frame.from_options(
    frame = mapped,
    connection_type = "s3",
    connection_options = {"path": "s3://my-kinesis-bucket-01/clean_sales/"},
    format = "json"
)

job.commit()
