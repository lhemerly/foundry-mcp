# 🧠 Ethereum Foundry MCP Project

This project is a Model Context Protocol (MCP) server designed to interact with Ethereum Foundry tools. It provides a set of tools and utilities to manage Foundry projects, run tests, build contracts, and more.

---

## 📂 Project Structure

```
pyproject.toml       # Project configuration file
README.md            # Project documentation
uv.lock              # Dependency lock file
LLM/                 # Documentation and SDK usage
src/eth_wh_mcp/      # Source code for the MCP server
```

---

## 🚀 Features

- **Create Foundry Projects**: Initialize new Foundry projects.
- **Build Contracts**: Compile Solidity contracts with various options.
- **Run Tests**: Execute tests with detailed configuration.
- **Inspect Contracts**: Retrieve ABI, bytecode, and other metadata.
- **Run Scripts**: Execute Solidity scripts.
- **Start Local Nodes**: Launch Anvil or Chisel for local Ethereum development.
- **Advanced Cast Commands**: Execute Ethereum-related commands using `cast`.

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Ensure Foundry tools (`forge`, `cast`, `anvil`, etc.) are installed and available in your PATH.

---

## 🏗️ Usage

### Running the MCP Server

To start the MCP server:
```bash
python src/eth_wh_mcp/main.py
```

### Available Tools

The following tools are available in the MCP server:

- **create_project**: Initialize a new Foundry project.
- **build_project**: Build the current Foundry project.
- **test_project**: Run tests in the Foundry project.
- **clone_contract**: Clone a contract from Etherscan.
- **run_script**: Execute a Solidity script.
- **run_cast_command**: Run a `cast` command.
- **start_anvil_with_options**: Start the Anvil local Ethereum node.
- **start_chisel_with_options**: Start the Chisel Solidity REPL.
- **inspect_contract**: Inspect contract metadata.
- **snapshot_project**: Create a gas usage snapshot.
- **coverage_project**: Display test coverage.

---

## 📖 Documentation

### MCP Python SDK

Refer to the [LLM/python-mcp-sdk.md](LLM/python-mcp-sdk.md) file for detailed usage of the MCP Python SDK, including server construction, tools, prompts, and context handling.

---

## 🧪 Development

### Local Debugging

Run the MCP server in development mode:
```bash
mcp dev src/eth_wh_mcp/main.py --with-editable .
```

### Runtime Execution

To execute the server:
```bash
python src/eth_wh_mcp/main.py
```

---

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.