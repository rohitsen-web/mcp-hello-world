# MCP Hello World

A minimal MCP (Model Context Protocol) server in Python.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python server.py
```

## Test with MCP Inspector

```bash
mcp dev server.py
```

This opens a browser UI where you can call the `say_hello` tool interactively.

## What's happening

- `FastMCP` creates an MCP server
- `@mcp.tool()` exposes a Python function as a tool an LLM can call
- The server communicates over stdio (default), which is how most MCP clients connect

## Updated via Kong + Zuma RDPS

## Updated via Kong + Zuma RDPS - With Policy Active

## Addd lines as part of Kong RDPS Testing

> Tip: You can extend this server by adding more `@mcp.tool()` decorated functions.

> Note: MCP servers can also expose resources and prompts, not just tools.

## Updated via Kong + Zuma RDPS - Write Blocked Test

## Updated by Kong + Zuma RDPS governance - 2025-07-14
