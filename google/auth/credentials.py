"""Minimal stub for `google.auth.credentials` used by tests.

Only provides `AnonymousCredentials` used by the tests to construct a
credentials-like object; it intentionally does not attempt to implement
real authentication logic.
"""


class AnonymousCredentials:
    """Stand-in credentials for tests."""

    def __init__(self) -> None:  # pragma: no cover - trivial stub
        """Create a minimal anonymous credentials instance for tests."""
