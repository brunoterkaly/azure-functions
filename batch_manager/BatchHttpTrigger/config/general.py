# -------------------------------------------------------------------------
#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
# ----------------------------------------------------------------------------------
# The example companies, organizations, products, domain names,
# e-mail addresses, logos, people, places, and events depicted
# herein are fictitious. No association with any real company,
# organization, product, domain name, email address, logo, person,
# places, or events is intended or should be inferred.
# --------------------------------------------------------------------------

# Global constant variables (Azure Storage account/Batch details)

# import "config.py" in "python_quickstart_client.py "

import random
import string

_BATCH_ACCOUNT_NAME = "etl"
_BATCH_ACCOUNT_URL = "https://etl.westus3.batch.azure.com"
_INPUT_FILE = "person.csv"
_CONTAINER_NAME = "input"
_STORAGE_ACCOUNT_NAME = "bonobostorage"
_POOL_ID = "WindowsPoolV2"
_POOL_NODE_COUNT = 1
_POOL_VM_SIZE = "STANDARD_A2_v2"
_TASK_ID = "CDMInsert"
_STANDARD_OUT_FILE_NAME = "stdout.txt"
_STANDARD_ERR_FILE_NAME = "stderr.txt"
_REGISTRY_USER_NAME = "registryetl"
_REGISTRY_SERVER = "registryetl.azurecr.io"
_DOCKER_IMAGE = "registryetl.azurecr.io/images/python-etl:latest"
_DOCKER_IMAGE_ABBREV = "registryetl.azurecr.io/images/python-etl:latest"
