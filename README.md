### This is a Python script that calls a sqlite3 database and is instrumented using the `@newrelic.agent.background_task()` decorator.

In the `newrelic.ini` config file:

```
[newrelic]
startup_timeout = 10.0
```
