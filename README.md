# bqaa-ci-sandbox

Sandbox repo behind the CI evidence in two Medium posts:

- **Post #2** — *[Track Every AI Agent Interaction with One CLI Flag](https://medium.com/google-cloud/track-every-ai-agent-interaction-with-one-cli-flag-cae20ffa5100)* — the budget-based gate (`bq-agent-sdk evaluate --exit-code` on latency, token usage, tool error rate, turn count).
- **Post #3** — *[Scalable LLM-as-Judge: Automating Agent Evaluation Directly in BigQuery](https://medium.com/google-cloud/scalable-llm-as-judge-automating-agent-evaluation-directly-in-bigquery-302ca4acf19f)* — the same workflow, extended with `LLMAsJudge.faithfulness(strict=True)` to catch the things a budget can't (hallucinations, off-topic answers, ungrounded claims). The red GHA run referenced in post #3 came from this repo.

Every PR that touches `agents/**` or `prompts/**` runs `bq-agent-sdk evaluate --exit-code` against the last 24 hours of traces in a sandbox BigQuery dataset. A red PR status means at least one session blew a budget or failed a judge.

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
