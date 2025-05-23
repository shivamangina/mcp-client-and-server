# Google Sheets MCP Client

This is an MCP (Model Context Protocol) client for interacting with the Google Sheets server. It provides a simple interface for creating and modifying Google Sheets.

## What is an MCP Client?

An MCP client is a program that:
1. Connects to an MCP server
2. Provides methods to call server tools
3. Handles communication between your code and the server
4. Processes responses and errors

In this case, the client allows you to:
- Create new Google Sheets
- Add data to existing sheets
- Handle authentication and errors

## Setup

1. Install dependencies:
```bash
uv pip install "mcp[cli]>=1.9.0"
```

2. Make sure the Google Sheets server is running:
```bash
cd ../mcp-server
uv run sheets_server.py
```

3. In a new terminal, run the client:
```bash
cd ../mcp-client
uv run sheets_client.py
```

## Usage

The client provides two main methods:

1. `create_sheet(title: str)`: Creates a new Google Sheet
   ```python
   client = SheetsClient()
   result = client.create_sheet("My New Sheet")
   spreadsheet_id = result['spreadsheetId']
   ```

2. `add_to_sheet(spreadsheet_id: str, range_name: str, values: list)`: Adds data to a sheet
   ```python
   values = [
       ["Name", "Age", "City"],
       ["John", "30", "New York"],
       ["Alice", "25", "London"]
   ]
   result = client.add_to_sheet(spreadsheet_id, "Sheet1!A1:C3", values)
   ```

## Example

The `main()` function in `sheets_client.py` shows a complete example:
1. Creates a new sheet
2. Adds sample data
3. Handles errors and responses

## Error Handling

The client includes error handling for:
- Connection issues
- Server errors
- Invalid responses
- Missing spreadsheet IDs

All errors are logged to stderr and returned in the response dictionary.

## Integration with AI Models

This client can be used by AI models (like Claude) to:
1. Create and modify Google Sheets
2. Process the responses
3. Handle any errors that occur

The client provides a clean interface for AI models to interact with Google Sheets through the MCP server.