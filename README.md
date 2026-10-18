# tcg-price-japan — Japan TCG Used-Price MCP Server

Read-only MCP server exposing the kensho Japan TCG (Pokemon / trading card)
used-price dataset collected from suruga-ya.jp.

## Tools

| Tool | Description |
|---|---|
| `tcg_current_price(item)` | Latest used/new/list price snapshot (JPY) for an item |
| `tcg_price_history(item, limit=50)` | Price time series (oldest first) |
| `tcg_top_movers(direction, limit=10)` | Biggest `|delta JPY|` movers, optional up/down filter |

## Data

- Source: `data/accumulated.jsonl` (960 observations, snapshot 2026-09-21)
- Marketplace: suruga-ya.jp
- No network, no API key, no account required

## Data Source: Apify Store

The underlying dataset is also available as a managed Apify Actor:

- **surugaya-japan-hobby-prices** — [https://apify.com/atushi1841/acts/surugaya-japan-hobby-prices](https://apify.com/atushi1841/acts/surugaya-japan-hobby-prices)
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

## Data Source: Apify Store & Smithery Registry

This MCP server is available on:

- **Apify Store**: [TCG prices from suruga-ya.jp](https://apify.com/fruitful_quintessence/acts/surugaya-japan-hobby-prices) — TCG prices from suruga-ya.jp
- **Smithery Registry**: [Install via Smithery](https://server.smithery.ai/atushi1841/tcg-price-japan) — MCP server for AI agents

Install via Smithery:
```bash
npx @smithery/cli install atushi1841/tcg-price-japan --client claude
```

## MCP Registry

This server is registered on the official [MCP Registry](https://registry.modelcontextprotocol.io).
Find it via search: [tcg-price-japan](https://registry.modelcontextprotocol.io/v0/servers?search=io.github.atushi1841/tcg-price-japan)

## MCP 公式レジストリ登録済み

本サーバーはMCP公式レジストリに登録済みです。

- **Registry**: [MCP Registry](https://registry.modelcontextprotocol.io/v0/servers?search=io.github.atushi1841/tcg-price-japan)

```bash
# レジストリでの確認
curl -s "https://registry.modelcontextprotocol.io/v0.1/servers?search=atushi1841" | grep -o "\"io.github.atushi1841/tcg-price-japan\""
```

---
## Data & Store

- **Apify Store:** https://apify.com/fruitful_quintessence
- **Gumroad datasets:** https://atushi5.gumroad.com/l/kutuxe
