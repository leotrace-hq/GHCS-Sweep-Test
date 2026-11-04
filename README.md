# GHCS-Sweep-Test

Deliberately vulnerable fixture for testing LeoPrevent's GitHub code scanning integration
(LEO-793). Do not deploy. CodeQL default setup and a Semgrep SARIF upload raise the alerts;
`/leoprevent:sweep github` judges them.

Planted on purpose:

| File | Expected | Why |
|---|---|---|
| `app/orders.py` `list_orders` | real | SQL built from a request parameter |
| `app/orders.py` `sorted_orders` | false positive | concatenated column comes from a fixed allowlist |
| `app/reports.py` `download` | real | path traversal through `os.path.join` |
| `app/reports.py` `archive` | real | shell command built from a request parameter |
| `app/cache.py` `cache_key` | false positive | MD5 as a cache key, not for security |
| `app/cache.py` `app.run(debug=True)` | real | Flask debug mode |
