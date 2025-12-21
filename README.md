# Project Setup (LangChain + LangGraph with uv)

This repository uses **uv** to manage dependencies and run a local LangGraph development server. It also includes Jupyter tooling for fast experimentation (agents, tools, RAG, etc.).

## Requirements

- Python 3.11+
- uv installed

## Install core dependencies

```bash
uv add langgraph langchain langchain-openai
```

## Install the LangGraph CLI (development)

Add the LangGraph CLI as a dev dependency. The `inmem` extra enables an in-memory backend that is great for local testing.

```bash
uv add "langgraph-cli[inmem]" --dev
```

## Add Jupyter (development)

We use Jupyter for exploration and prototyping.

```bash
uv add ipykernel --dev
```

## Run the agent (dev server)

Start the LangGraph development server:

```bash
uv run langgraph dev
```

## Project structure

The project uses a clean `src/` layout so the codebase stays organized as it grows.

```text
.
```
