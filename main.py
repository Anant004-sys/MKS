from fastapi import FastAPI
from fastmcp import FastMCP

mcp = FastMCP("MKS-PAMP-MCP")

@mcp.tool()
def add(a: float, b: float) -> float:
    return a + b

@mcp.tool()
def calculate_total_amount(unit_price: float, quantity: int, tax_percent: float = 0) -> dict:
    base_amount = unit_price * quantity
    tax_amount = base_amount * (tax_percent / 100)
    total_amount = base_amount + tax_amount
    return {
        "base_amount": base_amount,
        "tax_amount": tax_amount,
        "total_amount": total_amount
    }

# Create a normal web app wrapper
app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "service": "MKS-PMAP-MCP", "mcp": "/mcp"}

@app.get("/health")
def health_http():
    return {"status": "ok", "service": "MKS-PMAP-MCP"}

# Mount MCP endpoints under /mcp
app.mount("/mcp", mcp.http_app())
