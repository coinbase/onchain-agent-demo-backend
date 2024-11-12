# Onchain Agent Backend Demo

![Token-creation](https://github.com/user-attachments/assets/016c26cd-c599-4f7c-bafd-c8090069b53e)

A web app that enables onchain interactions through a conversational UI using AgentKit, a collaboration between [CDP SDK](https://docs.cdp.coinbase.com/) and [OnchainKit](https://onchainkit.xyz).

## Overview

This project features a Python backend designed to work seamlessly with CDP's AgentKit backend. Together, they enable the creation of an AI agent capable of performing onchain operations on Base. The agent uses GPT-4 for natural language understanding and AgentKit for onchain interactions.

## Modules

- The `agent` module contains functions for interacting with the onchain agent.
    - `initialize_agent` creates (or loads) an agent from CDP Wallet Data.
    - `run_agent` invokes the agent.
    - `handle_action_agent` handles agent actions - in our demo, we just save the addresses of deployed NFTs and ERC-20s to a SQLite database, but you can customize this behavior for your application.
- The `agent.custom_actions` module contains an example for adding custom actions to the agent.
    - `get_latest_block` is a custom action we've added that retrieves the latest Base Sepolia block information for the agent.
    - You can add additional custom actions to this module, following our example.

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

## Environment Setup

Create a `.env` file with the following variables:

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

## Agent Wallet

**Note**: when running your agent from the first time, the SDK will automatically generate a wallet for you. The wallet information will be logged to the console, and saved to the `wallets` table in the SQLite DB.

**Important**: This is for demo purposes, and we do not recommend this approach for a production application. Please save your wallet information somewhere safe.

Agents will by default be re-instantiated through the SQLite DB.

You can also instantiate your agent from the following environment variables.

```
CDP_WALLET_ID="",
CDP_WALLET_SEED=""
```

## API Usage

The application exposes a chat endpoint that accepts natural language commands for blockchain interactions:

```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"input": "deploy a new ERC-20 token", "conversation_id": 0}'
```


Retrieve a list of NFTs deployed by the agent:

```bash
curl http://localhost:5000/nfts 
```

Retrieve a list of ERC-20s deployed by the agent:

```bash
curl http://localhost:5000/tokens
```

## Deploying to Replit

- [Frontend Template](https://replit.com/@alissacrane1/onchain-agent-demo-frontend?v=1)
- [Backend Template](https://replit.com/@alissacrane1/onchain-agent-demo-backend?v=1)

Steps:
- Sign up for a Replit account, or login to your existing one.
- Navigate to the template links, and click `Use Template` on the top right hand side.
- Under `Secrets` in `Workspace Features`, add the environment variables below.
  - Tip: You can click `Edit as JSON` and copy the values below in.
- Click `Deploy` in the top right.
  - Tip: Deploy your backend first, as you'll need the deployment URL for the frontend's `NEXT_PUBLIC_API_URL` environment variable.

**Backend**
```
{
  "CDP_API_KEY_NAME": "get this from https://portal.cdp.coinbase.com/projects/api-keys",
  "CDP_API_KEY_PRIVATE_KEY": "get this from https://portal.cdp.coinbase.com/projects/api-keys",
  "OPENAI_API_KEY": "get this from https://platform.openai.com/api-keys",
  "NETWORK_ID": "base-sepolia"
}
```

**Important: Replit resets the SQLite template on every deployment, before sending funds to your agent or using it on Mainnet be sure to read [Agent Wallet](#agent-wallet) and save your wallet ID and seed in a safe place.**

**Frontend**
```
{
  "NEXT_PUBLIC_API_URL": "your backend deployment URL here"
}
```

## License

See [LICENSE.md](LICENSE.md) for details.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.
