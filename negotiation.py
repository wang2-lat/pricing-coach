def get_negotiation_scripts(scenario: str):
    """Provide negotiation scripts for common pricing objections"""
    
    scripts = {
        'discount': {
            'scenario': 'Customer Requesting Discount',
            'opening': "I appreciate you're budget-conscious. Let me ask - what specific outcomes are you hoping to achieve with our product?",
            'value': "Our pricing reflects the ROI our customers see. On average, clients save 10x our annual cost through [specific benefit]. Would a payment plan make this more manageable?",
            'alternative': "I can't reduce the price, but I can add [extra feature/extended trial/priority support] to increase your value at the same investment.",
            'principles': [
                "Never discount more than 10% without getting something in return",
                "Reframe from price to value and ROI",
                "Offer payment plans instead of discounts",
                "Bundle additional value rather than cutting price"
            ]
        },
        'free-trial': {
            'scenario': 'Customer Demanding Extended Free Trial',
            'opening': "I understand you want to be certain before committing. What specific concerns do you need to resolve during the trial?",
            'value': "Our standard trial is designed to show value quickly. Most customers see results within [X days]. What if we schedule a check-in call on day 3 to ensure you're getting value?",
            'alternative': "Instead of extending the free trial, I can offer a 30-day money-back guarantee. This way you're protected but we're both committed to making it work.",
            'principles': [
                "Free trials should be short (7-14 days) to create urgency",
                "Offer money-back guarantee instead of longer trials",
                "Provide onboarding support to accelerate value realization",
                "Set clear success metrics for the trial period"
            ]
        },
        'price-objection': {
            'scenario': 'Customer Says "Too Expensive"',
            'opening': "I hear you. Help me understand - compared to what? What alternatives are you considering?",
            'value': "Let's break down the cost. At $X per month, that's $Y per day. How much time/money does [problem] currently cost you daily?",
            'alternative': "If budget is the constraint right now, we have a starter plan at [lower price] with core features. You can upgrade as you grow.",
            'principles': [
                "Never defend your price - ask questions instead",
                "Break down cost to daily/per-user amounts",
                "Compare to cost of NOT solving the problem",
                "Offer tiered pricing, not discounts"
            ]
        }
    }
    
    return scripts.get(scenario.lower(), {
        'scenario': 'Unknown Scenario',
        'opening': 'Please specify: discount, free-trial, or price-objection',
        'value': '',
        'alternative': '',
        'principles': []
    })
