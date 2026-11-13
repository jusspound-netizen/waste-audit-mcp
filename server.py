import os
from fastmcp import FastMCP, Context
from paymcp import Mode, price
from paymcp.providers import StripeProvider, X402Provider

# Module-level server object (required by FastMCP Cloud)
mcp = FastMCP("Waste Audit")

# Initialize PayMCP with both payment rails:
# - Stripe for card-capable clients
# - x402 (Solana USDC) for wallet-capable agents
PayMCP(
    mcp,
    providers=[
        StripeProvider(api_key=os.getenv("STRIPE_API_KEY")),
        X402Provider(pay_to=[{"address": "47yaLqSsDFv8ah6gYNVuAgZYWxjakGTeff3UAFarhioo"}]),
    ],
    mode=Mode.AUTO,
)

@mcp.tool()
def list_pricing(ctx: Context) -> str:
    """Free tool: returns the price for the audit."""
    return "analyze_waste: $0.50 per call. Pay via Stripe or Solana USDC."

@mcp.tool()
@price(amount=0.50, currency="USD")
def analyze_waste(log_id: str, ctx: Context) -> str:
    """Analyze an agent log for wasted tokens and return a quantified report."""
    # STUB: Replace with ghost-tracer analysis logic.
    return f"Audit of {log_id}: 215 redundant calls found. Estimated waste: $6.87."

if __name__ == "__main__":
    mcp.run()
