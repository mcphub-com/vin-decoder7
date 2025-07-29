import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/vincheckinfo/api/vin-decoder7'

mcp = FastMCP('vin-decoder7')

@mcp.tool()
def full_vin_decode(vin: Annotated[str, Field(description='Must be 17 digits')]) -> dict: 
    '''Lookup year, make, model and other vehicle information from the 17-digit VIN.'''
    url = 'https://vin-decoder7.p.rapidapi.com/vin'
    headers = {'x-rapidapi-host': 'vin-decoder7.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'vin': vin,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
