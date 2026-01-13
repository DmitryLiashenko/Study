#!/usr/bin/env bash
set -euo pipefail
python -m src.main --input data/companies.csv --output output/results.csv --concurrency 20 --timeout 25 --max-pages 6
