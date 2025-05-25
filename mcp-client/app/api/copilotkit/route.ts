import {
  CopilotRuntime,
  copilotRuntimeNextJSAppRouterEndpoint,
  langGraphPlatformEndpoint,
  LangChainAdapter
} from "@copilotkit/runtime";
import { NextRequest } from "next/server";
// @ts-ignore
import { ChatPerplexity } from "@langchain/community/chat_models/perplexity";

const serviceAdapter = new LangChainAdapter({
  chainFn: async ({ messages, tools }) => {
    // Your ChatPerplexity only supports invoke()
    return model.invoke(messages);
  },
});

const model = new ChatPerplexity({
  model: "llama-3.1-sonar-small-128k-online", // Use 'model' instead of 'modelName'
  temperature: 0,
});

const runtime = new CopilotRuntime({
  remoteEndpoints: [
    langGraphPlatformEndpoint({
      deploymentUrl: `${process.env.AGENT_DEPLOYMENT_URL || 'http://localhost:8123'}`,
      langsmithApiKey: process.env.LANGSMITH_API_KEY,
      agents: [
        {
          name: 'sample_agent',
          description: 'A helpful LLM agent.',
        }
      ]
    }),
  ],
});

export const POST = async (req: NextRequest) => {
  const { handleRequest } = copilotRuntimeNextJSAppRouterEndpoint({
    runtime,
    serviceAdapter,
    endpoint: "/api/copilotkit",
  });

  return handleRequest(req);
};