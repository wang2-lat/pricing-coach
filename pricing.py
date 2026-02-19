def generate_pricing_strategies(product_type: str, cost: float, competitor_price: float = None):
    """Generate pricing strategies based on product type and cost structure"""
    strategies = []
    
    # Cost-plus pricing
    strategies.append({
        'name': 'Cost-Plus (Safe Start)',
        'price': cost * 2.5,
        'rationale': 'Standard 2.5x markup ensures profitability while staying conservative',
        'target': 'Risk-averse customers who value stability'
    })
    
    # Value-based pricing
    value_multiplier = {'saas': 5, 'physical': 3, 'service': 4, 'digital': 6}.get(product_type.lower(), 4)
    strategies.append({
        'name': 'Value-Based (Premium)',
        'price': cost * value_multiplier,
        'rationale': f'Price reflects customer value, not just cost. {product_type.capitalize()} typically supports {value_multiplier}x markup',
        'target': 'Customers focused on ROI and outcomes'
    })
    
    # Competitive pricing
    if competitor_price:
        strategies.append({
            'name': 'Competitive Match',
            'price': competitor_price * 0.95,
            'rationale': '5% below competitor to capture market share while maintaining perceived quality',
            'target': 'Price-sensitive customers comparing options'
        })
        
        strategies.append({
            'name': 'Premium Positioning',
            'price': competitor_price * 1.3,
            'rationale': '30% premium signals superior quality and exclusive positioning',
            'target': 'Status-conscious buyers seeking best-in-class'
        })
    
    # Penetration pricing
    strategies.append({
        'name': 'Market Penetration',
        'price': cost * 1.8,
        'rationale': 'Lower margin to rapidly acquire customers and build market share',
        'target': 'Early adopters and volume buyers'
    })
    
    return strategies[:5]
