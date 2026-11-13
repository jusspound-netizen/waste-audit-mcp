import os
from fastmcp import FastMCP, Context
from paymcp import Mode, price
from paymcp.providers import StripeProvider

# Module-level server object (required by FastMCP Cloud)
mcp = FastMCP("Waste Audit")

# Initialize PayMCP with Stripe
# The API key is read from environment variables, never hardcoded.
PayMCP(
    mcp,
    providers=[StripeProvider(api_key=os.getenv("STRIPE_API_KEY"))],
    mode=Mode.AUTO,  # AUTO falls back to Stripe if x402 wallet is absent
)

@mcp.tool()
def list_pricing(ctx: Context) -> str:
    """Free tool: returns the price for the audit."""
    return "analyze_waste: $0.50 per call. Pay via Stripe when prompted."

@mcp.tool()
@price(amount=0.50, currency="USD")
def analyze_waste(log_id: str, ctx: Context) -> str:
    """Analyze an agent log for wasted tokens and return a quantified report."""
    # STUB: Replace this with your actual ghost-tracer analysis logic.
    # For now, it returns a mock result to prove the payment flow works.
    return f"Audit of {log_id}: 215 redundant calls found. Estimated waste: $6.87."

if __name__ == "__main__":
    mcp.run()
