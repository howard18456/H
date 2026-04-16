import json
import math

class AtlasROIEngine:
    """
    Core decision engine for the Autonomous Bounty Hunter.
    Calculates whether a task is worth the token cost based on 
    the Atlas ROI Matrix.
    """
    def __init__(self, token_price_usd=0.00001, profit_margin_threshold=0.5):
        self.token_price_usd = token_price_usd
        self.profit_margin_threshold = profit_margin_threshold

    def evaluate_task(self, payout_usd, estimated_tokens):
        """
        Formula: Profit = Payout - (Token_Cost * 1.5)
        Risk factor 1.5 accounts for iterations and debugging.
        """
        token_cost = estimated_tokens * self.token_price_usd
        adjusted_cost = token_cost * 1.5
        profit = payout_usd - adjusted_cost
        
        margin = profit / payout_usd if payout_usd > 0 else -1
        
        return {
            "payout": payout_usd,
            "cost": adjusted_cost,
            "profit": profit,
            "margin": margin,
            "decision": "PROCEED" if margin >= self.profit_margin_threshold else "DISCARD"
        }

# --- POC Test Case ---
if __name__ == "__main__":
    engine = AtlasROIEngine()
    
    # Case 1: High value, low cost (The Dream)
    print(f"S-Tier Task: {engine.evaluate_task(300, 50000)}") 
    
    # Case 2: Low value, high cost (The Trap)
    print(f"C-Tier Task: {engine.evaluate_task(5, 100000)}")
