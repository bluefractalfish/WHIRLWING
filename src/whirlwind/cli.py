
from typing import List, Optional

from rich.console import Console
from rich.panel import Panel
from rich.text import Text


console = Console()


def main(argv: Optional[List[str]] = None) -> int:
    title = Text("WHIRLWIND", style="bold cyan")
    message = Text("hello world", style="bold white")

    console.print(
        Panel.fit(
            message,
            title=title,
            border_style="cyan",
        )
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

