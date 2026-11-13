import os
from mcp.server.fastmcp import FastMCP, Context
from paymcp import PayMCP, Mode, price
from paymcp.providers import MockPaymentProvider

# Module-level server object (required by FastMCP Cloud)
mcp = FastMCP("Waste Audit")

# Initialize PayMCP with MockProvider for testing.
# Real crypto/Stripe integration will be added later.
PayMCP(
    mcp,
    providers=[MockPaymentProvider()],
    mode=Mode.TWO_STEP,
)

@mcp.tool()
def list_pricing(ctx: Context) -> str:
    """Free tool: returns the price for the audit."""
    return "analyze_waste: $0.50 per call. (Test mode: payments are simulated)"

@mcp.tool()
@price(0.50, currency="USD")
def analyze_waste(log_id: str, ctx: Context) -> str:
    """Analyze an agent log for wasted tokens and return a quantified report."""
    return f"Audit of {log_id}: 215 redundant calls found. Estimated waste: $6.87."

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=9000)
