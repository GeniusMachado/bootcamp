from fastmcp import FastMCP

# Initialize the server
mcp = FastMCP("AgentHelper")

# 1. Add a TOOL: Functions an LLM can execute
@mcp.tool()
def calculate_area(radius: float) -> float:
    """Calculates the area of a circle given its radius."""
    import math
    return math.pi * (radius ** 2)

# 2. Add a RESOURCE: Read-only data an LLM can query
# This uses a template URI to provide dynamic data
@mcp.resource("config://{env}")
def get_config(env: str) -> dict:
    """Provides configuration details for a specific environment."""
    configs = {
        "prod": {"version": "1.0.0", "status": "stable"},
        "dev": {"version": "1.1.0-beta", "status": "experimental"}
    }
    return configs.get(env, {"error": "Environment not found"})

# 3. Add a PROMPT: Predefined instructions for the user/agent
@mcp.prompt()
def review_code(code: str) -> str:
    """Generates a prompt for the LLM to review specific code."""
    return f"Please review the following Python code for security vulnerabilities: \n\n{code}"

if __name__ == "__main__":
    # Standard run command using 'stdio' for local client connection
    mcp.run()

