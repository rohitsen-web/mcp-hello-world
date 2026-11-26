from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hello-world")


@mcp.tool()
def say_hello(name: str) -> str:
    """Say hello to someone."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    mcp.run()
