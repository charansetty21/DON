from dataclasses import dataclass


@dataclass
class Plan:
    action: str
    tool: str = None
    arguments: dict = None


@dataclass
class ToolCall:
    tool: str
    arguments: dict