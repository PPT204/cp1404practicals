from __future__ import annotations
from dataclasses import dataclass
from datetime import date

@dataclass(order=True)
class Project:
    # Order by priority
    priority: int
    start_date: date
    name: str
    cost_estimate: float
    completion: int  # 0..100

    def is_complete(self) -> bool:
        return self.completion >= 100

    def update(self, *, completion: int | None = None, priority: int | None = None) -> None:
        if completion is not None:
            self.completion = max(0, min(100, int(completion)))
        if priority is not None:
            self.priority = int(priority)

    def format_line(self) -> str:
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.completion}%")
