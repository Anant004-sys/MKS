from fastmcp import FastMCP

mcp = FastMCP("MKS-PMAP-MCP")

# Health check
@mcp.tool()
def health() -> dict:
    return {"status": "ok", "service": "MKS-PMAP-MCP"}

# Simple math action
@mcp.tool()
def add(a: float, b: float) -> float:
    return a + b


@mcp.tool()
def calculate_total_amount(
    unit_price: float,
    quantity: int,
    tax_percent: float = 0
) -> dict:
    """
    Calculate total amount including tax.
    """
    base_amount = unit_price * quantity
    tax_amount = base_amount * (tax_percent / 100)
    total_amount = base_amount + tax_amount

    return {
        "base_amount": base_amount,
        "tax_amount": tax_amount,
        "total_amount": total_amount
    }


app = mcp.http_app()
