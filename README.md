# Pricing Coach

A CLI tool that helps entrepreneurs confidently price and monetize their products.

## Problem

Entrepreneurs often struggle with:
- Not knowing how to price their products
- Being afraid to charge and losing users
- Getting pressured into discounts
- Missing the right timing to monetize

## Features

1. **Pricing Strategy Generator** - Generate 3-5 pricing strategies based on product type, cost, and competitor analysis
2. **Monetization Timing Evaluator** - Assess product maturity and user engagement to recommend optimal charging timing
3. **Negotiation Script Library** - Get proven scripts for handling price objections, discount requests, and free trial demands

## Installation


## Usage

### Generate Pricing Strategies


Options:
- `--type, -t`: Product type (saas/physical/service/digital)
- `--cost, -c`: Base cost per unit/month
- `--competitor, -p`: Competitor average price (optional)

### Evaluate Monetization Timing


Options:
- `--maturity, -m`: Product maturity (mvp/beta/stable/mature)
- `--users, -u`: Current active user count
- `--engagement, -e`: User engagement level (low/medium/high)

### Get Negotiation Scripts


Options:
- `--scenario, -s`: Scenario type (discount/free-trial/price-objection)

## Examples


## Tech Stack

- Python 3.8+
- Typer (CLI framework)
- Rich (terminal formatting)
pip install -r requirements.txt
python main.py pricing -t saas -c 10 -p 49
python main.py timing -m beta -u 500 -e high
python main.py negotiate -s discount