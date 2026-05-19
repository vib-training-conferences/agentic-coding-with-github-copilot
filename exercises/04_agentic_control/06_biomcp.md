## Exercise 6: Connecting GitHub Copilot to BioMCP

BioMCP is a Model Context Protocol (MCP) server that connects AI assistants to leading public biomedical data sources (such as PubMed, ClinicalTrials.gov, and ClinVar). Connecting it allows Copilot to answer complex biomedical questions and retrieve relevant data directly in your editor.

***

### Step-by-Step Guide

1. **Install BioMCP**:
   Create a Python virtual environment and install the BioMCP CLI using `pip`.
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install biomcp-cli
   ```
   *(For other installation options, consult [biomcp.org](https://biomcp.org/).)*

2. **Configure the MCP Server in VS Code**:
   In VS Code, open your MCP settings `mcp.json` (`Cmd/Ctrl + Shift + P` > `MCP: Open User Configuration`) and add the BioMCP server to your configuration:
   ```json
    {
        "inputs": [],
        "servers": {
            "biomcp": {
                "type": "stdio",
                "command": "INSERT-PATH-TO-YOUR-WORKSPACE/.venv/bin/biomcp",
                "args": ["serve"]
            }
        }
    }
   ```

   >Make sure to replace the command path with the actual path to your `biomcp` executable.

3. **Verify the Connection**:
    After saving the configuration, you should see a notification confirming that the BioMCP server is connected. You can also check if the biomcp server is listed in the MCP servers panel (`Cmd/Ctrl + Shift + P` > `MCP: List Servers`). Click on the BioMCP server to see its status and logs. If necessary, click "Start Server" to launch it.

4. **Experiment**:
   With the connection established, you can ask Copilot to perform biomedical research, retrieve gene information, or aggregate clinical data directly alongside your code! Ask questions like: "What are the latest clinical trials for Alzheimer's disease?" or "Summarize the findings of the latest research on BRCA1 gene mutations." See how Copilot uses BioMCP to fetch and summarize relevant biomedical data in real-time.