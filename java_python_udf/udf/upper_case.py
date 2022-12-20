from pyflink.table.udf import udf
from pyflink.table import DataTypes

@udf(result_type=DataTypes.STRING())
def to_upper( str ):
    "This capitalizes the whole string"
    return str.upper()

