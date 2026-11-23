# warehouse-analytics

An analytics platform for a simulated spare parts warehouse for trucks, cars and commercial vehicles.

Warehouses produce a lot of data – picks, errors, stock movements – but it is rarely used to improve daily work.
This project generates realistic warehouse data and analyzes it to make order picking faster and more reliable.

## Planned features
- Validate and parse storage location codes (e.g. `A-03-12-2`)
- Generate realistic synthetic warehouse data
- KPIs: picks per hour, error rate, lead time
- ABC/XYZ analysis of spare parts
- Dashboard for warehouse KPIs
- Demand forecasting for spare parts

## Setup

Requirements: [uv](https://docs.astral.sh/uv/)

```bash
git clone https://github.com/Matthias146/warehouse-analytics.git
cd warehouse-analytics
uv sync
```

## Running tests and linting

```bash
uv run pytest
uv run ruff check
```
