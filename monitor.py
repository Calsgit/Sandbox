class Monitor:
    """Defines a monitor and its width and height in pixels."""

    def __init__(self, model="Monitor", width=0, height=0):
        """
        Model: string, name of monitor
        Width: int, width in pixels
        Height: int, height in pixels
        """
        self.model = model
        self.width = width
        self.height = height

    def get_resolution(self):
        """Return a tuple of monitor width and height."""
        return self.width, self.height

    def get_total_pixels(self):
        """Calculate how many pixels are on monitor."""
        return self.width * self.height

    def __eq__(self, other):
        """Check whether parsed object has the same monitor dimensions as this one."""
        return self.get_resolution() == (other.width, other.height)
