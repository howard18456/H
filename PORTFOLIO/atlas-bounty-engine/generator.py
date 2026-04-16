class ProposalGenerator:
    """
    Generates professional, high-conversion technical proposals.
    """
    def __init__(self, atlas_persona="Senior Autonomous Engineer"):
        self.persona = atlas_persona

    def generate(self, issue_title, issue_body, payout, solution_points):
        template = f"""
## 🚀 Professional Proposal: {issue_title}

I have analyzed the requirements for this task and identified a high-impact implementation path. Instead of a basic fix, I propose a robust architectural approach.

### 🛠 Technical Solution
{self._format_points(solution_points)}

### 📦 Deliverables
- Production-ready implementation of the above logic.
- Comprehensive test suite (Unit + Integration).
- Technical documentation for maintainers.

### 💰 Commercial Proposal
- **Fixed Price**: ${payout} USD
- **Timeline**: 3-5 Days
- **Value**: This implementation focuses on long-term maintainability and zero-regression, ensuring that the feature doesn't just work, but scales.

I am a {self.persona}. If this approach aligns with your goals, I can start immediately.
"""
        return template.strip()

    def _format_points(self, points):
        return "\n".join([f"- {p}" for p in points])
