import sys
import os
import requests
import dotenv
import tempfile

dotenv.load_dotenv() # Load environment variables from .env file

try:
    from mcp.server.fastmcp import FastMCP
    print("MCP imported successfully", file=sys.stderr)
except ImportError as e:
    print(f"Failed to import MCP: {e}", file=sys.stderr)
    sys.exit(1)

print("Starting Text Audio Server...", file=sys.stderr)

# Create an MCP server
mcp = FastMCP("Text Audio Server")

@mcp.tool()
def generate_audio(text: str) -> dict:
    """
    Converts text to speech using the Eleven Labs API and returns the path to the generated audio file.

    Args:
        text: The text to convert to speech.

    Returns:
        dict: A dictionary containing the path to the audio file or an error message.
    """
    print(f"Generating audio for text: {text[:50]}...", file=sys.stderr) # Print first 50 chars of text

    elevenlabs_api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not elevenlabs_api_key:
        return {"error": "ELEVENLABS_API_KEY environment variable not set."}

    # --- Eleven Labs API Configuration ---
    # You may need to adjust the voice_id and model_id based on your Eleven Labs account and desired voice.
    voice_id = "pNInz6obpgDQGcFmaJgB" # Example: Rachel voice ID - replace with your desired voice ID
    model_id = "eleven_monolingual_v1" # Example model ID - replace if you use a different model
    api_url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": elevenlabs_api_key
    }

    data = {
        "text": text,
        "model_id": model_id,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status() # Raise an exception for bad status codes

        # Save the audio to a temporary file
        # Use delete=False so the file persists after this function returns
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        with open(temp_file.name, 'wb') as f:
            f.write(response.content)
        
        audio_file_path = temp_file.name
        print(f"Audio generated successfully and saved to {audio_file_path}", file=sys.stderr)

        # --- Google Sheets Integration Placeholder ---
        # You would add code here to interact with your sheets_server.py
        # to store the audio_file_path or the audio content in Google Sheets.
        # This might involve calling a tool on the sheets_server.
        # Example (assuming sheets_server has an add_audio_link tool):
        # sheets_server_tool = mcp.get_tool("Sheets Server", "add_audio_link")
        # sheets_server_tool(sheet_name="YourSheet", row_id="some_id", audio_link=audio_file_path)
        # --- End Placeholder ---

        return {"audio_file_path": audio_file_path}

    except requests.exceptions.RequestException as e:
        print(f"Error calling Eleven Labs API: {str(e)}", file=sys.stderr)
        return {"error": f"Eleven Labs API error: {str(e)}"}
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}", file=sys.stderr)
        return {"error": f"An unexpected error occurred: {str(e)}"}

if __name__ == "__main__":
    print("Starting MCP server...", file=sys.stderr)
    # Ensure you have the necessary libraries installed:
    # uv pip install --system fastmcp requests python-dotenv
    mcp.run() 