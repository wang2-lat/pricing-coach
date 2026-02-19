def evaluate_timing(maturity: str, user_count: int, engagement: str):
    """Evaluate optimal timing for monetization based on product and user metrics"""
    
    # Calculate readiness score
    maturity_scores = {'mvp': 20, 'beta': 40, 'stable': 70, 'mature': 90}
    engagement_scores = {'low': 20, 'medium': 60, 'high': 90}
    
    maturity_score = maturity_scores.get(maturity.lower(), 40)
    engagement_score = engagement_scores.get(engagement.lower(), 40)
    
    # User count factor (logarithmic scale)
    if user_count < 100:
        user_score = 30
    elif user_count < 1000:
        user_score = 60
    else:
        user_score = 90
    
    total_score = int((maturity_score * 0.4) + (engagement_score * 0.4) + (user_score * 0.2))
    
    # Generate recommendation
    if total_score >= 70:
        recommendation = "START MONETIZING NOW"
        analysis = "Your product shows strong signals for monetization. Users are engaged and the product is stable enough to justify payment."
        action_items = [
            "Launch with a clear pricing page this week",
            "Offer grandfathered pricing to existing users (20% lifetime discount)",
            "Set up payment infrastructure (Stripe/Paddle)",
            "Create upgrade prompts for free users"
        ]
    elif total_score >= 50:
        recommendation = "PREPARE FOR MONETIZATION (2-4 weeks)"
        analysis = "You're close but need to strengthen a few areas before charging. Focus on increasing engagement and stability."
        action_items = [
            "Add 2-3 high-value features users are requesting",
            "Improve onboarding to boost engagement",
            "Survey users about willingness to pay",
            "Test pricing page with 'Coming Soon' badge"
        ]
    else:
        recommendation = "BUILD MORE VALUE FIRST (1-3 months)"
        analysis = "Charging now risks losing your early users. Focus on product-market fit and engagement before monetization."
        action_items = [
            "Conduct user interviews to understand core value",
            "Improve core features based on usage data",
            "Grow to at least 500 active users",
            "Achieve 40%+ weekly active user rate"
        ]
    
    return {
        'recommendation': recommendation,
        'score': total_score,
        'analysis': analysis,
        'action_items': action_items
    }
