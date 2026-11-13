import os
from mcp.server.fastmcp import FastMCP, Context
from paymcp import PayMCP, Mode, price
from paymcp.providers import MockPaymentProvider

mcp = FastMCP("Waste Audit")

# MockPaymentProvider simulates payments without Stripe or crypto credentials.
# Swap in StripeProvider / X402Provider when real credentials are available.
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
    mcp.run()
