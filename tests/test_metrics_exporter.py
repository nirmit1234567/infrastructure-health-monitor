
from prometheus_client import generate_latest

import metrics_exporter


def test_collect_metrics_updates_values():
    metrics_exporter.collect_metrics()

    assert 0 <= metrics_exporter.cpu_usage._value.get() <= 100
    assert 0 <= metrics_exporter.memory_usage._value.get() <= 100
    assert 0 <= metrics_exporter.disk_usage._value.get() <= 100


def test_metrics_are_exposed():
    metrics_exporter.collect_metrics()
    output = generate_latest().decode("utf-8")

    assert "system_cpu_usage_percent" in output
    assert "system_memory_usage_percent" in output
    assert "system_disk_usage_percent" in output
