#
#
# Copyright (c) 2021 Oracle, Inc.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl
#

import io
import json
import logging
from fdk import response

# this is the entry point of the function

def handler(ctx, data: io.BytesIO=None):
    logging.getLogger().info("Invoked function with custom image") 
    return response.Response(
        ctx, 
        response_data=json.dumps({"status": "Presenting during monday touchpoint for OCI demo inside customImage "}),
        headers={"Content-Type": "application/json"}
    )
