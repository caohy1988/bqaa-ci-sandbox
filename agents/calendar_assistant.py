"""Calendar-Assistant baseline agent.

This file exists so PRs touching `agents/**` or `prompts/**` trigger
the quality-gate workflow. The actual demo agent lives in the
bigquery-agent-analytics-blogpost repo at demo_calendar_assistant.py
(baseline) and demo_calendar_assistant_regressed.py (regressed).

The sandbox CI workflow reads the last 24 hours of production traces
from the configured BigQuery dataset and evaluates them against four
deterministic budgets. Whether a PR to this file passes or fails is
driven entirely by what the demo agent emitted to BigQuery, not by
anything in this file.
"""

# Path the sandbox agent reads its instruction from. Baseline is
# deliberately two-sentence-short; the regressed variant lives on
# a separate branch and adds a policy block plus few-shot examples.
PROMPT_PATH = "prompts/calendar_assistant.txt"
