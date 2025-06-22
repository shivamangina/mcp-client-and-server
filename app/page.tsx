export default function Home() {
  return (
    <div className="min-h-screen">
      <div className="flex">
        <div className="w-1/4 bg-gray-50 h-screen">
          <div className="flex flex-col p-4 h-[5vh]">Logo</div>
          <div className="flex flex-col justify-between h-[95vh]">
            <div className="flex flex-col p-4">Chat History</div>
            <div className="flex flex-col p-4">Profile</div>
          
          </div>
        
        
        
        </div>
        <div className="w-1/2 h-screen">Main Content</div>
        <div className="w-1/4 bg-gray-50 h-screen">
          <div className="flex flex-col p-4"> Available Tools</div>
          </div>
          
         
      </div>
    
        
       

       
     
     
    </div>
  );
}
