# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(firstnumber: int, secondnumber: int) -> int:
    """Add two numbers"""
    return firstnumber + secondnumber