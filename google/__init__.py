"""Local stub of `google` package used for tests in the minimal branch.

This file provides a very small shim so tests that import
`google.auth.credentials.AnonymousCredentials` succeed when the
real `google` package is not installed in the minimal environment.
"""

__all__ = ["auth"]
