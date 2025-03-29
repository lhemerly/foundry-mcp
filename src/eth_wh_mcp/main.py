from mcp.server.fastmcp import FastMCP
import subprocess

# Initialize the MCP server
mcp = FastMCP("FoundryServer")

@mcp.tool()
def create_project(project_name: str) -> str:
    """Creates a new Foundry project."""
    result = subprocess.run(["forge", "init", project_name], capture_output=True, text=True)
    return result.stdout or result.stderr

@mcp.tool()
def build_project(options: str = "") -> str:
    """
    Builds the current Foundry project with optional parameters.

    Parameters:
    - options (str): Additional options for the `forge build` command. Possible values include:
        * --names: Print compiled contract names.
        * --sizes: Print compiled non-test contract sizes, exiting with code 1 if any of them are above the size limit.
        * --skip: Skip compilation of non-essential contract directories like test or script (usage --skip test).
        * [PATHS]...: Build source files from specified paths.
        * --force: Clear the cache and artifacts folder and recompile.
        * --libraries: Set pre-linked libraries in the format <remapped path to lib>:<library name>:<address>.
        * --optimize: Activate the Solidity optimizer.
        * --optimizer-runs: Specify the number of optimizer runs.
        * --via-ir: Use the Yul intermediate representation compilation pipeline.
        * --revert-strings: Specify how to treat revert and require reason strings.
        * --use: Specify the solc version or path to a local solc.
        * --offline: Do not access the network.
        * --no-auto-detect: Do not auto-detect solc.
        * --ignored-error-codes: Ignore solc warnings by error code.
        * --extra-output: Include extra output in the contract's artifact.
        * --extra-output-files: Write extra output to separate files.
        * --evm-version: Specify the target EVM version.
        * --build-info: Generate build info files.
        * --build-info-path: Specify the output path for build info files.
        * --root: Specify the project's root path.
        * --contracts: Specify the contracts source directory.
        * --lib-paths: Specify the path to the library folder.
        * --remappings: Specify the project's remappings.
        * --cache-path: Specify the path to the compiler cache.
        * --config-path: Specify the path to the config file.
        * --hh/--hardhat: Convenience flag equivalent to passing --contracts contracts --lib-paths node-modules.
        * --out: Specify the project's artifacts directory.
        * --silent: Suppress all output.
        * --watch: Watch specific file(s) or folder(s) for changes.
        * --delay: Specify file update debounce delay.
        * --no-restart: Do not restart the command while it's running.
        * --run-all: Explicitly re-run the command on all files when a change is made.

    Returns:
    - str: The output of the `forge build` command.
    """
    command = ["forge", "build"] + options.split()
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout or result.stderr

@mcp.tool()
def test_project(options: str = "") -> str:
    """
    Runs the project's tests with optional parameters.

    Parameters:
    - options (str): Additional options for the `forge test` command. Possible values include:
        * --match-test: Only run test functions matching the specified regex pattern.
        * --no-match-test: Only run test functions that do not match the specified regex pattern.
        * --match-contract: Only run tests in contracts matching the specified regex pattern.
        * --no-match-contract: Only run tests in contracts that do not match the specified regex pattern.
        * --match-path: Only run tests in source files matching the specified glob pattern.
        * --no-match-path: Only run tests in source files that do not match the specified glob pattern.
        * --debug: Run a test in the debugger.
        * --gas-report: Print a gas report.
        * --allow-failure: Exit with code 0 even if a test fails.
        * --fail-fast: Stop running tests after the first failure.
        * --etherscan-api-key: Use Etherscan for trace decoding when --fork-url is set.
        * --fork-url: Fetch state over a remote endpoint instead of starting from an empty state.
        * --fork-block-number: Fetch state from a specific block number over a remote endpoint.
        * --no-storage-caching: Disable the use of RPC caching.
        * --verbosity: Set verbosity levels (e.g., -v, -vv, -vvv).
        * --sender: Specify the address executing tests.
        * --initial-balance: Set the initial balance of deployed contracts.
        * --ffi: Enable the FFI cheatcode.
        * --base-fee: Set the base fee in a block (in wei).
        * --block-base-fee-per-gas: Set the base fee per gas in a block.
        * --block-coinbase: Set the coinbase of the block.
        * --block-difficulty: Set the block difficulty.
        * --block-gas-limit: Set the block gas limit.
        * --block-number: Set the block number.
        * --block-timestamp: Set the block timestamp (in seconds).
        * --chain-id: Set the chain ID.
        * --gas-limit: Set the block gas limit.
        * --gas-price: Set the gas price (in wei).
        * --tx-origin: Set the transaction origin.
        * --force: Clear the cache and artifacts folder and recompile.
        * --libraries: Set pre-linked libraries in the format <remapped path to lib>:<library name>:<address>.
        * --optimize: Activate the Solidity optimizer.
        * --optimizer-runs: Specify the number of optimizer runs.
        * --via-ir: Use the Yul intermediate representation compilation pipeline.
        * --revert-strings: Specify how to treat revert and require reason strings.
        * --use: Specify the solc version or path to a local solc.
        * --offline: Do not access the network.
        * --no-auto-detect: Do not auto-detect solc.
        * --ignored-error-codes: Ignore solc warnings by error code.
        * --extra-output: Include extra output in the contract's artifact.
        * --extra-output-files: Write extra output to separate files.
        * --evm-version: Specify the target EVM version.
        * --build-info: Generate build info files.
        * --build-info-path: Specify the output path for build info files.
        * --root: Specify the project's root path.
        * --contracts: Specify the contracts source directory.
        * --lib-paths: Specify the path to the library folder.
        * --remappings: Specify the project's remappings.
        * --cache-path: Specify the path to the compiler cache.
        * --config-path: Specify the path to the config file.
        * --hh/--hardhat: Convenience flag equivalent to passing --contracts contracts --lib-paths node-modules.
        * --out: Specify the project's artifacts directory.
        * --silent: Suppress all output.
        * --watch: Watch specific file(s) or folder(s) for changes.
        * --delay: Specify file update debounce delay.
        * --no-restart: Do not restart the command while it's running.
        * --run-all: Explicitly re-run the command on all files when a change is made.
        * --list: List tests instead of running them.
        * --json: Print the deployment information as JSON.

    Returns:
    - str: The output of the `forge test` command.
    """
    command = ["forge", "test"] + options.split()
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout or result.stderr

@mcp.tool()
def clone_contract(contract_address: str, root: str = "", chain_id: str = "", etherscan_api_key: str = "", no_remappings_txt: bool = False, no_commit: bool = False, no_git: bool = False, quiet: bool = False) -> str:
    """Clones a contract from Etherscan with specified options."""
    command = ["forge", "clone", contract_address]

    if root:
        command.append(root)
    if chain_id:
        command.extend(["--chain", chain_id])
    if etherscan_api_key:
        command.extend(["--etherscan-api-key", etherscan_api_key])
    if no_remappings_txt:
        command.append("--no-remappings-txt")
    if no_commit:
        command.append("--no-commit")
    if no_git:
        command.append("--no-git")
    if quiet:
        command.append("--quiet")

    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout or result.stderr

@mcp.tool()
def run_script(script_name: str) -> str:
    """Runs a script in the current Foundry project."""
    result = subprocess.run(["forge", "script", script_name], capture_output=True, text=True)
    return result.stdout or result.stderr

@mcp.tool()
def run_cast_command_with_options(command: str, options: str = "") -> str:
    """
    Executes a Cast command with optional parameters.

    Parameters:
    - command (str): The Cast command to execute. Possible commands include:
        * General Commands: help, completions
        * Chain Commands: chain-id, chain, client
        * Transaction Commands: publish, receipt, send, call, rpc, tx, run, estimate, access-list, logs
        * Block Commands: find-block, gas-price, block-number, basefee, block, age
        * Account Commands: balance, storage, proof, nonce, code, codesize
        * ENS Commands: lookup-address, resolve-name, namehash
        * Etherscan Commands: etherscan-source
        * ABI Commands: abi-encode, 4byte, 4byte-calldata, 4byte-event, calldata, decode-abi, decode-calldata, pretty-calldata, selectors, upload-signature
        * Conversion Commands: format-bytes32-string, from-bin, from-fixed-point, from-utf8, from-wei, parse-bytes32-address, parse-bytes32-string, to-ascii, to-base, to-bytes32, to-dec, to-fixed-point, to-hex, to-hexdata, to-int256, to-rlp, to-uint256, to-unit, to-wei, shl, shr
        * Utility Commands: address-zero, sig, sig-event, keccak, compute-address, create2, interface, index, concat-hex, max-int, min-int, max-uint, to-check-sum-address
        * Wallet Commands: wallet, wallet new, wallet address, wallet sign, wallet vanity, wallet verify
    - options (str): Additional options for the Cast command. Possible options include:
        * -V, --version: Print version info and exit.
        * -h, --help: Prints help information.

    Returns:
    - str: The output of the Cast command.
    """
    full_command = ["cast"] + command.split() + options.split()
    result = subprocess.run(full_command, capture_output=True, text=True)
    return result.stdout or result.stderr

@mcp.tool()
def start_anvil_with_options(options: str = "") -> str:
    """
    Starts the Anvil local Ethereum node with optional parameters.

    Parameters:
    - options (str): Additional options for the `anvil` command. Possible values include:
        * --accounts: Set the number of accounts (default: 10).
        * --auto-impersonate: Enable autoImpersonate on startup.
        * --block-time: Block time in seconds for interval mining.
        * --balance: Set the balance of the accounts (default: 10000).
        * --derivation-path: Set the derivation path of the child key to be derived (default: m/44’/60’/0’/0/).
        * --hardfork: Choose the EVM hardfork to use (default: latest).
        * --init: Initialize the genesis block with the given genesis.json file.
        * --mnemonic: BIP39 mnemonic phrase used for generating accounts.
        * --no-mining: Disable auto and interval mining, and mine on demand instead.
        * --order: How transactions are sorted in the mempool (default: fees).
        * --port: Port number to listen on (default: 8545).
        * --steps-tracing: Enable steps tracing used for debug calls returning geth-style traces.
        * --ipc: Starts an IPC endpoint at the given PATH argument or the default path.
        * --silent: Don’t print anything on startup.
        * --timestamp: Set the timestamp of the genesis block.
        * --disable-default-create2-deployer: Disables deploying the default CREATE2 factory when running Anvil without forking.
        * --fork-url: Fetch state over a remote endpoint instead of starting from an empty state.
        * --fork-block-number: Fetch state from a specific block number over a remote endpoint.
        * --fork-transaction-hash: Fetch state from a specific transaction hash over a remote endpoint.
        * --retries: Number of retry requests for spurious networks (default: 5).
        * --timeout: Timeout in ms for requests sent to remote JSON-RPC server in forking mode (default: 45000).
        * --compute-units-per-second: Sets the number of assumed available compute units per second for this provider (default: 330).
        * --no-rate-limit: Disables rate limiting for this node’s provider.
        * --no-storage-caching: Disables RPC caching; all storage slots are read from the endpoint.
        * --base-fee: The base fee in a block.
        * --chain-id: The chain ID (default: 31337).
        * --code-size-limit: EIP-170: Contract code size limit in bytes (default: ~25kb).
        * --gas-limit: The block gas limit.
        * --gas-price: The gas price.
        * --allow-origin: Set the CORS allow_origin (default: *).
        * --no-cors: Disable CORS.
        * --host: The IP address the server will listen on.
        * --config-out: Writes output of anvil as JSON to a user-specified file.
        * --prune-history: Don’t keep full chain history.

    Returns:
    - str: The output of the `anvil` command.
    """
    command = ["anvil"] + options.split()
    result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return "Anvil started with the specified options. Check the terminal for logs."

@mcp.tool()
def start_chisel_with_options(options: str = "") -> str:
    """
    Starts the Chisel Solidity REPL with optional parameters.

    Parameters:
    - options (str): Additional options for the `chisel` command. Possible values include:
        * list: Displays all cached sessions stored in ~/.foundry/cache/chisel.
        * load <id>: Launches the REPL and loads the corresponding session if a cached session with id = <id> exists.
        * view <id>: Displays the source code of the session’s REPL contract if a cached session with id = <id> exists.
        * clear-cache: Deletes all cache files within the ~/.foundry/cache/chisel directory. These sessions are unrecoverable.

    Returns:
    - str: The output of the `chisel` command.
    """
    command = ["chisel"] + options.split()
    result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return "Chisel started with the specified options. Check the terminal for logs."

@mcp.tool()
def inspect_contract(contract_name: str, field: str, options: str = "") -> str:
    """
    Inspects a smart contract and retrieves specialized information based on the specified field.

    Parameters:
    - contract_name (str): The name of the contract to inspect.
    - field (str): The field to inspect. Possible values include:
        * abi
        * bytecode (b/bytes/bytecode)
        * deployedBytecode (deployedBytecode/deployed_bytecode/deployed-bytecode/deployedbytecode/deployed)
        * assembly (assembly/asm)
        * asmOptimized (asmOptimized/assemblyOptimized/assemblyoptimized/assembly_optimized/asmopt/assembly-optimized/asmo/asm-optimized/asmoptimized/asm_optimized)
        * methods (methods/methodidentifiers/methodIdentifiers/method_identifiers/method-identifiers/mi)
        * gasEstimates (gasEstimates/gas/gas_estimates/gas-estimates/gasestimates)
        * storageLayout (storageLayout/storage_layout/storage-layout/storagelayout/storage)
        * devdoc (devdoc/dev-doc/devDoc)
        * ir
        * ir-optimized (ir-optimized/irOptimized/iroptimized/iro/iropt)
        * metadata (metadata/meta)
        * userdoc (userdoc/userDoc/user-doc)
        * ewasm (ewasm/e-wasm)
        * errors
        * events
    - options (str): Additional options for the `forge inspect` command. Possible values include:
        * --json: Format output as JSON.
        * --force: Clear the cache and artifacts folder and recompile.
        * --libraries: Set pre-linked libraries in the format <remapped path to lib>:<library name>:<address>.
        * --optimize: Activate the Solidity optimizer.
        * --optimizer-runs: Specify the number of optimizer runs.
        * --via-ir: Use the Yul intermediate representation compilation pipeline.
        * --revert-strings: Specify how to treat revert and require reason strings.
        * --use: Specify the solc version or path to a local solc.
        * --offline: Do not access the network.
        * --no-auto-detect: Do not auto-detect solc.
        * --ignored-error-codes: Ignore solc warnings by error code.
        * --extra-output: Include extra output in the contract's artifact.
        * --extra-output-files: Write extra output to separate files.
        * --evm-version: Specify the target EVM version.
        * --build-info: Generate build info files.
        * --build-info-path: Specify the output path for build info files.
        * --root: Specify the project's root path.
        * --contracts: Specify the contracts source directory.
        * --lib-paths: Specify the path to the library folder.
        * --remappings: Specify the project's remappings.
        * --cache-path: Specify the path to the compiler cache.
        * --config-path: Specify the path to the config file.
        * --hh/--hardhat: Convenience flag equivalent to passing --contracts contracts --lib-paths node-modules.
        * --out: Specify the project's artifacts directory.
        * --silent: Suppress all output.
        * --watch: Watch specific file(s) or folder(s) for changes.
        * --delay: Specify file update debounce delay.
        * --no-restart: Do not restart the command while it's running.
        * --run-all: Explicitly re-run the command on all files when a change is made.

    Returns:
    - str: The output of the `forge inspect` command.
    """
    command = ["forge", "inspect", contract_name, field] + options.split()
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout or result.stderr

@mcp.tool()
def snapshot_project(options: str = "") -> str:
    """
    Creates a snapshot of each test's gas usage with optional parameters.

    Parameters:
    - options (str): Additional options for the `forge snapshot` command. Possible values include:
        * --asc: Sort results by gas used (ascending).
        * --desc: Sort results by gas used (descending).
        * --min: Only include tests that used more gas than the given amount.
        * --max: Only include tests that used less gas than the given amount.
        * --tolerance: Tolerates gas deviations up to the specified percentage (0-100).
        * --diff: Output a diff against a pre-existing snapshot.
        * --check: Compare against a pre-existing snapshot, exiting with code 1 if they do not match.
        * --snap: Specify the output file for the snapshot. Default: .gas-snapshot.
        * --match-test: Only run test functions matching the specified regex pattern.
        * --no-match-test: Only run test functions that do not match the specified regex pattern.
        * --match-contract: Only run tests in contracts matching the specified regex pattern.
        * --no-match-contract: Only run tests in contracts that do not match the specified regex pattern.
        * --match-path: Only run tests in source files matching the specified glob pattern.
        * --no-match-path: Only run tests in source files that do not match the specified glob pattern.
        * --debug: Run a test in the debugger.
        * --gas-report: Print a gas report.
        * --allow-failure: Exit with code 0 even if a test fails.
        * --fail-fast: Stop running tests after the first failure.
        * --etherscan-api-key: Use Etherscan for trace decoding when --fork-url is set.
        * --fork-url: Fetch state over a remote endpoint instead of starting from an empty state.
        * --fork-block-number: Fetch state from a specific block number over a remote endpoint.
        * --no-storage-caching: Disable the use of RPC caching.
        * --verbosity: Set verbosity levels (e.g., -v, -vv, -vvv).
        * --sender: Specify the address executing tests.
        * --initial-balance: Set the initial balance of deployed contracts.
        * --ffi: Enable the FFI cheatcode.
        * --base-fee: Set the base fee in a block (in wei).
        * --block-base-fee-per-gas: Set the base fee per gas in a block.
        * --block-coinbase: Set the coinbase of the block.
        * --block-difficulty: Set the block difficulty.
        * --block-gas-limit: Set the block gas limit.
        * --block-number: Set the block number.
        * --block-timestamp: Set the block timestamp (in seconds).
        * --chain-id: Set the chain ID.
        * --gas-limit: Set the block gas limit.
        * --gas-price: Set the gas price (in wei).
        * --tx-origin: Set the transaction origin.
        * --force: Clear the cache and artifacts folder and recompile.
        * --libraries: Set pre-linked libraries in the format <remapped path to lib>:<library name>:<address>.
        * --optimize: Activate the Solidity optimizer.
        * --optimizer-runs: Specify the number of optimizer runs.
        * --via-ir: Use the Yul intermediate representation compilation pipeline.
        * --revert-strings: Specify how to treat revert and require reason strings.
        * --use: Specify the solc version or path to a local solc.
        * --offline: Do not access the network.
        * --no-auto-detect: Do not auto-detect solc.
        * --ignored-error-codes: Ignore solc warnings by error code.
        * --extra-output: Include extra output in the contract's artifact.
        * --extra-output-files: Write extra output to separate files.
        * --evm-version: Specify the target EVM version.
        * --build-info: Generate build info files.
        * --build-info-path: Specify the output path for build info files.
        * --root: Specify the project's root path.
        * --contracts: Specify the contracts source directory.
        * --lib-paths: Specify the path to the library folder.
        * --remappings: Specify the project's remappings.
        * --cache-path: Specify the path to the compiler cache.
        * --config-path: Specify the path to the config file.
        * --hh/--hardhat: Convenience flag equivalent to passing --contracts contracts --lib-paths node-modules.
        * --out: Specify the project's artifacts directory.
        * --silent: Suppress all output.
        * --watch: Watch specific file(s) or folder(s) for changes.
        * --delay: Specify file update debounce delay.
        * --no-restart: Do not restart the command while it's running.
        * --run-all: Explicitly re-run the command on all files when a change is made.

    Returns:
    - str: The output of the `forge snapshot` command.
    """
    command = ["forge", "snapshot"] + options.split()
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout or result.stderr

@mcp.tool()
def coverage_project(options: str = "") -> str:
    """
    Displays which parts of your code are covered by tests with optional parameters.

    Parameters:
    - options (str): Additional options for the `forge coverage` command. Possible values include:
        * --report: Specify the report type for coverage. Can be used multiple times. Options include:
            - summary: Outputs a chart showing the percentage of code covered by tests (default).
            - lcov: Creates a lcov.info file containing coverage data in the root of the project.
            - debug: Outputs lines describing the location of uncovered code.
        * --ir-minimum: Run the coverage with via-ir enabled for the minimum amount of optimization necessary.
        * --no-match-coverage: Exclude paths and contracts from the coverage report. Example: "(script|Foo|Bar)".

    Returns:
    - str: The output of the `forge coverage` command.
    """
    command = ["forge", "coverage"] + options.split()
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout or result.stderr

@mcp.tool()
def run_script_with_options(path: str, options: str = "") -> str:
    """
    Runs a smart contract as a script, building transactions that can be sent on-chain with optional parameters.

    Parameters:
    - path (str): The path to the script to run.
    - options (str): Additional options for the `forge script` command. Possible values include:
        * --broadcast: Broadcasts the transactions.
        * --debug: Open the script in the debugger. Takes precedence over broadcast.
        * --gas-estimate-multiplier: Multiply all gas estimates by a relative percentage (default: 130).
        * --json: Output results in JSON format.
        * --legacy: Use legacy transactions instead of EIP1559 ones.
        * --resume: Resume submitting transactions that failed or timed-out previously.
        * --sig: Specify the function signature to call in the contract (default: run()).
        * --skip-simulation: Skip on-chain simulation.
        * --skip: Skip compilation of non-essential contract directories like test or script.
        * --non-interactive: Remove interactive prompts for contracts near the EIP-170 size limit.
        * --slow: Ensure a transaction is sent only after the previous one is confirmed.
        * --target-contract: Specify the name of the contract to run.
        * --priority-gas-price: Set the priority gas price for EIP1559 transactions.
        * --with-gas-price: Set the gas price for broadcasted transactions.
        * --chain: Specify the Etherscan chain.
        * --etherscan-api-key: Provide the Etherscan API key.
        * --verify: Verify contracts found in the receipts.
        * --verifier: Specify the verification provider (default: etherscan).
        * --verifier-url: Provide the verifier URL for submitting verification requests.
        * --delay: Set a timeout between attempts (default: 3 seconds).
        * --retries: Set the number of retry attempts (default: 15).
        * --force: Clear the cache and artifacts folder and recompile.
        * --libraries: Set pre-linked libraries in the format <remapped path to lib>:<library name>:<address>.
        * --optimize: Activate the Solidity optimizer.
        * --optimizer-runs: Specify the number of optimizer runs.
        * --via-ir: Use the Yul intermediate representation compilation pipeline.
        * --revert-strings: Specify how to treat revert and require reason strings.
        * --use: Specify the solc version or path to a local solc.
        * --offline: Do not access the network.
        * --no-auto-detect: Do not auto-detect solc.
        * --ignored-error-codes: Ignore solc warnings by error code.
        * --extra-output: Include extra output in the contract's artifact.
        * --extra-output-files: Write extra output to separate files.
        * --evm-version: Specify the target EVM version.
        * --build-info: Generate build info files.
        * --build-info-path: Specify the output path for build info files.
        * --root: Specify the project's root path.
        * --contracts: Specify the contracts source directory.
        * --lib-paths: Specify the path to the library folder.
        * --remappings: Specify the project's remappings.
        * --cache-path: Specify the path to the compiler cache.
        * --config-path: Specify the path to the config file.
        * --hh/--hardhat: Convenience flag equivalent to passing --contracts contracts --lib-paths node-modules.
        * --out: Specify the project's artifacts directory.
        * --silent: Suppress all output.
        * --watch: Watch specific file(s) or folder(s) for changes.
        * --delay: Specify file update debounce delay.
        * --no-restart: Do not restart the command while it's running.
        * --run-all: Explicitly re-run the command on all files when a change is made.
        * Wallet Options: Includes options for raw, keystore, hardware, and remote wallets.
        * EVM Options: Includes options for RPC URL, fork URL, verbosity, sender, initial balance, and more.

    Returns:
    - str: The output of the `forge script` command.
    """
    command = ["forge", "script", path] + options.split()
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout or result.stderr

if __name__ == "__main__":
    mcp.run()