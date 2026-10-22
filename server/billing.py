"""Billing and tier metadata for tcg-price-japan MCP server."""

FREE_SAMPLE = "https://atushi5.gumroad.com/l/kutuxe"
PRO_DATASET = "https://atushi5.gumroad.com/l/agyhq"
FREE_CALLS_PER_SESSION = 12

# Simple session call counter
_calls_used = 0

def billing_meta() -> dict:
    """Return billing metadata with current call count."""
    global _calls_used
    _calls_used += 1
    return {
        "tier": "free",
        "calls_used": _calls_used,
        "free_limit": FREE_CALLS_PER_SESSION,
        "weekly_dataset": PRO_DATASET,
        "free_sample": FREE_SAMPLE,
    }
