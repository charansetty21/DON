from brain.tools.base import Tool
from datetime import datetime


class TimeTool(Tool):
    name = "time"
    description = "Returns current system time"

    def run(self, **kwargs):
        return datetime.now().strftime("%H:%M:%S")