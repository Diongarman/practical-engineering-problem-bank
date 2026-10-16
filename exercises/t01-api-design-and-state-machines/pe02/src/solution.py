"""PE02: complete the command adapter below, then write your own tests."""


class CommandAdapter:
    """Handle commands against an in-memory key-value store.

    Use one instance for a sequence of commands. Separate instances should
    have independent stores.

    Command format (defined in this exercise's README):
        {"op": "set", "key": "example", "value": 42}
        {"op": "get", "key": "example"}
        {"op": "delete", "key": "example"}

    Keys are non-empty strings. Reject missing or extra command fields.
    Supplied values are assumed JSON-compatible; None is a valid value.
    See README.md for the full contract and ordered input/output examples.
    """

    def __init__(self) -> None:
        """Initialise this adapter's empty store."""
        # TODO: Choose and initialise the instance state.
        raise NotImplementedError("Implement CommandAdapter.__init__")

    def handle(self, command: dict) -> dict:
        """Process a set, get, or delete command.

        Every response must contain exactly ok, value, and error fields.
        Success uses ok=True and error=None. Successful get returns the
        stored value; successful set/delete return value=None.
        Failure uses ok=False and value=None, with an error code below.
        Missing keys produce NOT_FOUND; malformed or unknown operations
        produce INVALID_COMMAND. Failed commands must leave state unchanged.
        """
        # TODO: Implement the command contract.
        raise NotImplementedError("Implement CommandAdapter.handle")
