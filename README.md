# Waste Audit

A hosted MCP server that audits AI agent logs for wasted tokens and returns a quantified savings report.

## What it does

Reads an agent's tool-call log and finds three patterns that waste context:

- **Redundant calls** — the same tool with identical arguments, over and over. Usually a missing memoization layer.
- **Retry loops** — the same tool called again immediately after an error. Usually a retry policy with no backoff and no cap.
- **Duplicate reasoning steps** — the agent re-thinking a step it already resolved because the context window dropped it.

For each pattern it returns a count and a quantified estimate of wasted tokens and dollars, so you can rank fixes by ROI instead of guessing.

## Status

**This is a stub.** The `analyze_waste` tool returns a fixed example report. The payment layer uses `MockPaymentProvider` — it simulates the payment flow so the deployment can be tested end to end, but it does not process real charges.

The real analysis logic lives in [agent-cost-auditor](https://github.com/jusspound-netizen/agent-cost-auditor). Porting it into `analyze_waste` is the next step.

## Tools

| Tool | Price | What it does |
|---|---|---|
| `list_pricing` | Free | Returns the price for the audit |
| `analyze_waste` | $0.50 (mocked) | Returns a quantified waste report for a log ID |

## Deployment

The server runs on FastMCP Cloud (`https://waste-audit.fastmcp.app/mcp`) and is also listed on [mcprush](https://mcprush.com/jusspound-netizen/waste-audit-mcp) as a hosted endpoint.

Requires a running MCP server with `fastmcp`, `paymcp`, and `mcp<2.0.0`.

## License

MIT
