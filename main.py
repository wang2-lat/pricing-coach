import typer
from rich.console import Console
from rich.panel import Panel
from pricing import generate_pricing_strategies
from timing import evaluate_timing
from negotiation import get_negotiation_scripts

app = typer.Typer(help="A CLI tool that helps entrepreneurs confidently price and monetize their products")
console = Console()

@app.command()
def pricing(
    product_type: str = typer.Option(..., "--type", "-t", help="Product type (saas/physical/service/digital)"),
    cost: float = typer.Option(..., "--cost", "-c", help="Base cost per unit/month"),
    competitor_price: float = typer.Option(None, "--competitor", "-p", help="Competitor average price")
):
    """Generate 3-5 pricing strategies based on product type, cost, and competitor analysis"""
    console.print(Panel.fit("💰 Pricing Strategy Generator", style="bold blue"))
    strategies = generate_pricing_strategies(product_type, cost, competitor_price)
    
    for i, strategy in enumerate(strategies, 1):
        console.print(f"\n[bold cyan]Strategy {i}: {strategy['name']}[/bold cyan]")
        console.print(f"Price: ${strategy['price']:.2f}")
        console.print(f"Rationale: {strategy['rationale']}")
        console.print(f"Target: {strategy['target']}")

@app.command()
def timing(
    maturity: str = typer.Option(..., "--maturity", "-m", help="Product maturity (mvp/beta/stable/mature)"),
    user_count: int = typer.Option(..., "--users", "-u", help="Current active user count"),
    engagement: str = typer.Option(..., "--engagement", "-e", help="User engagement level (low/medium/high)")
):
    """Evaluate product maturity and user stickiness to recommend optimal monetization timing"""
    console.print(Panel.fit("⏰ Monetization Timing Evaluator", style="bold green"))
    result = evaluate_timing(maturity, user_count, engagement)
    
    console.print(f"\n[bold]Recommendation: {result['recommendation']}[/bold]")
    console.print(f"\nReadiness Score: {result['score']}/100")
    console.print(f"\nAnalysis:\n{result['analysis']}")
    console.print(f"\n[yellow]Action Items:[/yellow]")
    for item in result['action_items']:
        console.print(f"  • {item}")

@app.command()
def negotiate(
    scenario: str = typer.Option(..., "--scenario", "-s", help="Scenario (discount/free-trial/price-objection)")
):
    """Get negotiation scripts for handling price objections, discount requests, and free trial demands"""
    console.print(Panel.fit("💬 Negotiation Script Library", style="bold magenta"))
    scripts = get_negotiation_scripts(scenario)
    
    console.print(f"\n[bold cyan]Scenario: {scripts['scenario']}[/bold cyan]")
    console.print(f"\n[yellow]Opening Response:[/yellow]\n{scripts['opening']}")
    console.print(f"\n[yellow]Value Reinforcement:[/yellow]\n{scripts['value']}")
    console.print(f"\n[yellow]Alternative Offer:[/yellow]\n{scripts['alternative']}")
    console.print(f"\n[green]Key Principles:[/green]")
    for principle in scripts['principles']:
        console.print(f"  • {principle}")

if __name__ == "__main__":
    app()
