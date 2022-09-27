#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_airbyte_sample_sales import SourceAirbyteSampleSales

if __name__ == "__main__":
    source = SourceAirbyteSampleSales()
    launch(source, sys.argv[1:])
