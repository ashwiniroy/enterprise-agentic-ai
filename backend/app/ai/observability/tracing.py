from azure.monitor.opentelemetry import configure_azure_monitor

from app.core.config import settings


def configure_tracing():
    connection_string = (
        settings.applicationinsights_connection_string
    )

    if not connection_string:
        print(
            "Application Insights connection string "
            "not configured. Tracing disabled."
        )
        return

    configure_azure_monitor(
        connection_string=connection_string
    )

    print(
        "Azure Application Insights "
        "OpenTelemetry tracing configured."
    )