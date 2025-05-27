# mcp-client and server

build a multi agent human in the loop to make youtube shorts. 
using mcp servers and client

```
uv init
uv run main.py -m sonar-pro -p system_prompt.md -k $PPLX_API_KEY -j "i want to research about etf market in india"

```

<!--  -->

These are the agents:

- script writer
- storyboard artist
- audio agent
- video agent
- yt publisher agent

Reference: 
https://modelcontextprotocol.io/introduction
https://ai-sdk.dev/docs/introduction
https://github.com/wjayesh/mahilo

next steps: 

 - create all the servers required for the application
 - create a cli client and test the servers
 - create a react client for the application using ai/react
