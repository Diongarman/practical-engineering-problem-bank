"""PE02: complete the command adapter below, then write your own tests."""


class CommandAdapter:
    """Handle commands against an in-memory key-value store.

    Use one instance for a sequence of commands. Separate instances should
    have independent stores.

    Suggested command format (a scaffold convention, not a workbook rule):
        {"op": "set", "key": "example", "value": 42}
        {"op": "get", "key": "example"}
        {"op": "delete", "key": "example"}

    Document your choices for valid keys/values, extra fields, and the
    response value of successful set/delete operations in NOTES.md.
    """

    def __init__(self) -> None:
        """Initialise this adapter's empty store."""
        # TODO: Choose and initialise the instance state.
        raise NotImplementedError("Implement CommandAdapter.__init__")

    def handle(self, command: dict) -> dict:
        """Process a set, get, or delete command.

        Every response must contain ok, value, and error fields.
        Missing keys produce NOT_FOUND; malformed or unknown operations
        produce INVALID_COMMAND. Failed commands must leave state unchanged.
        """
        # TODO: Implement the command contract.
        raise NotImplementedError("Implement CommandAdapter.handle")
