# Instructions

We can add the next line for add dependencies

uv add langgraph langchain langchain-openai

# Langgraph CLI

In this part we should add the langgraph cli, but we can add a flag to run as development mode.

uv add "langgraph-cli[inmem]" --dev

# Jupyter

Also in our project is need to add jupyter as development mode for explore all AI agents, tools, rag, etc.

uv add ipykernel --dev

# Run the agent

The followinf part is for run our agent

uv run langgraph dev

# Project Structure

I've made a clean folder structure, creating folders, lik notebooks, into src: agents and api. Agents for createt multiple agents. It is important
to inform to pyproject.toml this structre, adding the followind:

[tool.setuptools.packages.find]
where = ["src"]
include = ["*"]

# Install the project

uv pip install -e .
