# tcg-price-japan — Japan TCG Used-Price MCP Server

Read-only MCP server exposing the kensho Japan TCG (Pokemon / trading card)
used-price dataset collected from suruga-ya.jp.

## Tools

| Tool | Description |
|---|---|
| `tcg_current_price(item)` | Latest used/new/list price snapshot (JPY) for an item |
| `tcg_price_history(item, limit=50)` | Price time series (oldest first) |
| `tcg_top_movers(direction, limit=10)` | Biggest `\|delta JPY\|` movers, optional up/down filter |

## Data

- Source: `data/accumulated.jsonl` (960 observations, snapshot 2026-09-21)
- Marketplace: suruga-ya.jp
- No network, no API key, no account required

## Installation (Smithery)

Install via Smithery registry:
```bash
smithery install @atushi1841/tcg-price-japan
```

## More MCP Servers

- **[kensho-kaku](https://github.com/atushi1841/kensho-kaku)** — Sweepstakes from ken-kaku.com
- **[kensho-kclub](https://github.com/atushi1841/kensho-kclub)** — Sweepstakes from kenshou.club
- **[kensho-kema](https://github.com/atushi1841/kensho-kema)** — Sweepstakes from ke-ma.net
- **[kensho-sweep-mcp](https://github.com/atushi1841/kensho-sweep-mcp)** — Full pipeline sweepstakes data
- **[japan-anime-figure-mcp](https://github.com/atushi1841/japan-anime-figure-mcp)** — Anime figure price comparison

## Data Source: Apify Store

The underlying dataset is also available as a managed Apify Actor:

- **[Apify Store: surugaya-japan-hobby-prices](https://apify.com/atushi1841/acts/surugaya-japan-hobby-prices)**
  (Actor ID: `F8Hl0a8Cx9bpJBrxR`) — same surugaya-ya.jp TCG price data, refreshed on a schedule

## Run

```bash
python server/server.py          # stdio MCP transport
python server/server.py --http   # streamable-http at /mcp
```

Requires `fastmcp>=3.0.0` (see `requirements.txt`).

## MCP Bundle

`manifest.json` follows the MCPB v0.4 spec. Pack with:

```bash
npx -y @anthropic-ai/mcpb pack . dist/tcg-price-japan.mcpb
```
