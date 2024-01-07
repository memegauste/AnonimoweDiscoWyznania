# settings.py
import sentry_sdk

sentry_sdk.init(
    dsn="https://b5b918f4bee4de0b41a0ef77423f1121@o4506530973417472.ingest.sentry.io/4506531034431488",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)