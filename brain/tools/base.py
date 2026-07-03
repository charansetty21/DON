class Tool:
    """
    Base interface for all DON tools.
    """

    name: str
    description: str

    def run(self, **kwargs):
        raise NotImplementedError