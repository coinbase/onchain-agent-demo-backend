# Onchain Agent Backend Demo

<img width="1512" alt="Screenshot 2024-11-07 at 9 26 56 AM" src="https://github.com/user-attachments/assets/f67a3472-dad1-46ad-869d-22a9cb97ceaa">


A web app that enables onchain interactions through a conversational UI using AgentKit, a collaboration between [CDP SDK](https://docs.cdp.coinbase.com/) and [OnchainKit](https://onchainkit.xyz).

## Overview

This project combines a Next.js frontend with a Python backend to create an AI agent capable of performing onchain operations on Base. The agent uses GPT-4 for natural language understanding and AgentKit for onchain interactions.

## Key Features

- **AI-Powered Chat Interface**: Interactive chat interface for natural language interactions onchain
- **Onchain Operations**: Ability to perform various blockchain operations through Agentkit:
  - Deploy and interact with ERC-20 tokens
  - Create and manage NFTs
  - Check wallet balances
  - Request funds from faucet
- **Real-time Updates**: Server-Sent Events (SSE) for streaming responses
- **Multi-language Support**: Built-in language selector for internationalization
- **Responsive Design**: Modern UI built with Tailwind CSS
- **Wallet Integration**: Secure wallet management through CDP Agentkit

## Tech Stack

- **Backend**: Python with Flask
- **AI/ML**: LangChain, GPT-4
- **Blockchain**: Coinbase Developer Platform (CDP) Agentkit

## Prerequisites

- [Rust](https://www.rust-lang.org/tools/install)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Bun](https://bun.sh) for package management

## Environment Setup

Create a `.env.local` file with the following variables:

```bash
CDP_API_KEY_NAME= # Create an API key at https://portal.cdp.coinbase.com/projects/api-keys
CDP_API_KEY_PRIVATE_KEY="" # Create an API key at https://portal.cdp.coinbase.com/projects/api-keys
OPENAI_API_KEY= # Get an API key from OpenAI - https://platform.openai.com/docs/quickstart
NETWORK_ID=base-sepolia
```

## Installation

1. Install dependencies:
```bash
poetry install
```

2. Start the development server:
```bash
poetry run python index.py
```

This will start the Python backend server.

## API Usage

The application exposes a chat endpoint that accepts natural language commands for blockchain interactions:

```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"input": "deploy a new ERC-20 token", "conversation_id": 0}'
```

## License

See [LICENSE.md](LICENSE.md) for details.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.
