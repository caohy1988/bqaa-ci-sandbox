# bqaa-ci-sandbox

Sandbox repo demoing the CI quality gate from Medium post #2:
["Your Agent Events Table Is Also a Test Suite"](https://github.com/haiyuan-eng-google/bigquery-agent-analytics-blogpost/pull/17).

Every PR that touches `agents/**` or `prompts/**` runs
`bq-agent-sdk evaluate --exit-code` against the last 24 hours of
traces in a sandbox BigQuery dataset, fanned across four budgets
(latency, token usage, tool error rate, turn count). A red PR
status means at least one session blew a budget.

- **Workflow** — [`.github/workflows/evaluate_thresholds.yml`](.github/workflows/evaluate_thresholds.yml)
- **Baseline prompt** — [`prompts/calendar_assistant.txt`](prompts/calendar_assistant.txt)
- **Regressed prompt** — lives on the `regressed/verbose-prompt` branch; the PR opened from that branch is the one that's supposed to go red.

## How the sandbox is wired

Repository variables:
- `PROJECT_ID=test-project-0728-467323`
- `DATASET_ID=agent_analytics_demo`

Repository secret:
- `GCP_SA_KEY` — service account JSON with `bigquery.jobUser` + `bigquery.dataViewer` on the sandbox dataset.

The agent itself runs from the blog repo
[`bigquery-agent-analytics-blogpost`](https://github.com/haiyuan-eng-google/bigquery-agent-analytics-blogpost)
— `demo_calendar_assistant.py` for the baseline fleet and
`demo_calendar_assistant_regressed.py` for the regressed fleet.
This repo only contains the CI wiring; it doesn't run the agent.
