from scanner import GitHubScanner
from evaluator import AtlasROIEngine
from generator import ProposalGenerator

def run_atlas_cycle(token, search_query):
    print("🚀 Starting Atlas Bounty Cycle...")
    
    scanner = GitHubScanner(token)
    evaluator = AtlasROIEngine()
    generator = ProposalGenerator()
    
    # 1. Discovery
    candidates = scanner.search_bounties(search_query)
    print(f"🔍 Found {len(candidates)} candidates.")
    
    for item in candidates:
        # Simplified ROI check for POC
        # In a real scenario, we'd use LLM to extract 'payout' from body
        payout = 100 # Mock payout for POC
        tokens_est = 10000
        
        result = evaluator.evaluate_task(payout, tokens_est)
        
        if result["decision"] == "PROCEED":
            print(f"✅ High ROI Target Found: {item['title']}")
            proposal = generator.generate(
                item['title'], 
                item['body'], 
                payout, 
                ["Optimize core logic", "Implement strict typing", "Add comprehensive tests"]
            )
            print("--- PROPOSAL GENERATED ---")
            print(proposal)
            print("---------------------------")

if __name__ == "__main__":
    # This is a POC. Token would normally be in .env
    MY_TOKEN = "your_token_here" 
    run_atlas_cycle(MY_TOKEN, "label:bounty is:open language:TypeScript")
