# 1. Install dependencies
# pip install fastapi uvicorn pydantic

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

# Create FastAPI app
app = FastAPI()

# 2. Define expected JSON structure using Pydantic
class Indicator(BaseModel):
    name: str
    params: Dict[str, float]  # e.g., {"fastperiod": 12, "slowperiod": 26, ...}
    buy_logic: str             # e.g., "macd_cross_up"
    sell_logic: str            # e.g., "macd_cross_down"

class StrategyInput(BaseModel):
    symbol: str
    start_date: str
    end_date: str
    indicators: List[Indicator]
    combine_logic: str         # "AND" or "OR"

# 3. Sample endpoint to receive and print input
@app.post("/run_backtest")
async def run_backtest(data: StrategyInput):
    # Print received data for now
    print("Symbol:", data.symbol)
    print("Start Date:", data.start_date)
    print("End Date:", data.end_date)
    print("Combine Logic:", data.combine_logic)
    print("Indicators:")
    for ind in data.indicators:
        print("- Name:", ind.name)
        print("  Params:", ind.params)
        print("  Buy Logic:", ind.buy_logic)
        print("  Sell Logic:", ind.sell_logic)

    # For now, just return the parsed data back
    return {"status": "received", "data": data.dict()}

# 4. Run this with: 
# uvicorn backtest_api_sample:app --reload
