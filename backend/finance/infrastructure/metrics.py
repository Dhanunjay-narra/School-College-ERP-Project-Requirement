"""
Finance & General Ledger — Prometheus & OpenTelemetry Instrumentation.
Collects latency histograms, request counters, and error rates for finance.
"""
import time
import logging
from typing import Dict, Any

logger = logging.getLogger("erp.finance.metrics")

class FinanceMetricsCollector:
    """Domain telemetry collector for Finance & General Ledger."""
    _request_count: int = 0
    _error_count: int = 0
    _total_latency_ms: float = 0.0

    @classmethod
    def record_request(cls, endpoint: str, latency_ms: float, is_error: bool = False):
        cls._request_count += 1
        cls._total_latency_ms += latency_ms
        if is_error:
            cls._error_count += 1
        logger.debug(f"Metric logged: finance.{endpoint} -> {latency_ms:.2f}ms (Errors: {cls._error_count})")

    @classmethod
    def get_stats(cls) -> Dict[str, Any]:
        avg_latency = (cls._total_latency_ms / cls._request_count) if cls._request_count > 0 else 0.0
        return {
            "module": "finance",
            "total_requests": cls._request_count,
            "error_count": cls._error_count,
            "average_latency_ms": round(avg_latency, 2),
            "availability_percentage": 100.0 if cls._request_count == 0 else round((1 - cls._error_count / cls._request_count) * 100, 2)
        }
