import sys
import os
import traceback
print("Starting imports...", file=sys.stderr)
print(f"Python executable: {sys.executable}", file=sys.stderr)
print(f"Python path: {sys.path}", file=sys.stderr)

try:
    from mcp.client.streamable_http import streamablehttp_client
    from mcp.client.session import ClientSession
    print("MCP imported successfully", file=sys.stderr)
except ImportError as e:
    print(f"Failed to import MCP: {e}", file=sys.stderr)
    sys.exit(1)

class SheetsClient:
    def __init__(self, server_url="http://localhost:8000/mcp"):
        """Initialize the Sheets client."""
        print(f"Initializing client with server URL: {server_url}", file=sys.stderr)
        self.server_url = server_url
        self.session = None
        self.initialized = False

    async def initialize(self):
        """Initialize the client and list available tools."""
        try:
            print("Listing available tools...", file=sys.stderr)
            async with streamablehttp_client(self.server_url) as (read_stream, write_stream, _):
                self.session = ClientSession(read_stream, write_stream)
                tools_result = await self.session.list_tools()
                print("Available tools:", tools_result, file=sys.stderr)
                self.initialized = True
        except Exception as e:
            print(f"Error initializing client: {str(e)}", file=sys.stderr)
            traceback.print_exc()
            raise

    async def create_sheet(self, title: str) -> dict:
        """
        Create a new Google Sheet.
        
        Args:
            title: The title of the new spreadsheet
            
        Returns:
            dict: The response from the server containing the new spreadsheet details
        """
        if not self.initialized:
            await self.initialize()
        
        print(f"Calling create_sheet with title: {title}", file=sys.stderr)
        try:
            result = await self.session.call_tool("create_sheet", {"title": title})
            print(f"Sheet created successfully: {result}", file=sys.stderr)
            return result.result
        except Exception as e:
            print(f"Error creating sheet: {str(e)}", file=sys.stderr)
            traceback.print_exc()
            raise

    async def add_to_sheet(self, spreadsheet_id: str, range_name: str, values: list) -> dict:
        """
        Add data to a Google Sheet.
        
        Args:
            spreadsheet_id: The ID of the spreadsheet to update
            range_name: The A1 notation of the values to update (e.g., 'Sheet1!A1:B2')
            values: List of lists containing the values to add
            
        Returns:
            dict: The response from the server
        """
        if not self.initialized:
            await self.initialize()
        
        print(f"Calling add_to_sheet with spreadsheet_id: {spreadsheet_id}, range: {range_name}", file=sys.stderr)
        try:
            result = await self.session.call_tool("add_to_sheet", {
                "spreadsheet_id": spreadsheet_id,
                "range_name": range_name,
                "values": values
            })
            print(f"Data added successfully: {result}", file=sys.stderr)
            return result.result
        except Exception as e:
            print(f"Error adding data: {str(e)}", file=sys.stderr)
            traceback.print_exc()
            raise

async def main():
    """Example usage of the Sheets client."""
    # Create client
    client = SheetsClient()
    
    try:
        # Initialize the client
        await client.initialize()
        
        # Create a new sheet
        result = await client.create_sheet("Test Sheet")
        print("Sheet created:", result)
        
        # Add some data
        if "spreadsheetId" in result:
            values = [
                ["Name", "Age"],
                ["John", "30"],
                ["Jane", "25"]
            ]
            result = await client.add_to_sheet(result["spreadsheetId"], "Sheet1!A1:B3", values)
            print("Data added:", result)
    except Exception as e:
        print(f"Error in main: {str(e)}", file=sys.stderr)
        traceback.print_exc()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main()) 