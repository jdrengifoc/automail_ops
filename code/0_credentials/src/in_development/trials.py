"""
Description: This script demonstrates good practices in Python coding.
Author: Juan David Rengifo Castro
Date: June 3, 2024
"""

import numpy as np
import pyarrow.parquet as pq
import pyarrow as pa
import pandas as pd
import os

if __name__ == "__main__":
    # Create dataframe.
    df = pd.DataFrame(
        {'one': [-1, np.nan, 2.5],
         'two': ['foo', 'bar', 'baz'],
         'three': [True, False, True]
         }, index=list('abc')
         )
    file_name_pd = 'pandas.parquet'
    df.to_parquet(file_name_pd)
    print(df)
    # Write parquet.
    table = pa.Table.from_pandas(df)
    file_name = 'example.parquet'
    pq.write_table(table, file_name)
    print(f'Succesfully write {file_name}')

    # Read parquet.
    table2 = pq.read_table(file_name)
    print(table2.to_pandas())
    print(f'Succesfully read {file_name}')
    
    # Remove parquet.
    os.remove(file_name)
    os.remove(file_name_pd)
    print(f'Succesfully remove {file_name} and {file_name_pd}')
