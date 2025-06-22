import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable";

export default function Home() {
  return (
    <ResizablePanelGroup direction="horizontal" className="h-screen">
      <ResizablePanel className="h-screen" defaultSize={25}>
        <div className="flex items-center justify-center p-6">
          <span className="font-semibold">Chat History</span>
        </div>
      </ResizablePanel>
      <ResizableHandle />
      <ResizablePanel className="h-screen" defaultSize={50}>
        <div className="flex items-center justify-center p-6">
          <span className="font-semibold">chat</span>
        </div>
      </ResizablePanel>
      <ResizableHandle />

      <ResizablePanel defaultSize={30}>
        <ResizablePanelGroup direction="vertical">
          <ResizablePanel defaultSize={25}>
            <div className="flex h-full items-center justify-center p-6">
              <span className="font-semibold">Available Tools</span>
            </div>
          </ResizablePanel>
          <ResizableHandle />
          <ResizablePanel defaultSize={75}>
            <div className="flex h-full items-center justify-center p-6">
              <span className="font-semibold">Tool Invocations</span>
            </div>
          </ResizablePanel>
        </ResizablePanelGroup>
      </ResizablePanel>
      
    </ResizablePanelGroup>
  );
}
