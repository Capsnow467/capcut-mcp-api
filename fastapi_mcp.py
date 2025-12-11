from fastapi import FastAPI

class FastApiMCP:
    """Minimal FastAPI MCP wrapper for CapCut MCP compatibility"""
    
    def __init__(self, app: FastAPI):
        self.app = app
    
    def mount(self):
        """Mount MCP endpoints - placeholder implementation"""
        @self.app.get("/mcp/health")
        async def health_check():
            return {"status": "ok", "service": "capcut-mcp"}
        
        @self.app.get("/mcp/info")
        async def mcp_info():
            return {
                "name": "CapCut MCP",
                "version": "1.0.0",
                "protocol": "mcp"
            }
