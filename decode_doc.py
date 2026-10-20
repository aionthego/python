import sys
import urllib.request
from html.parser import HTMLParser

# Ensure Windows console supports UTF-8 Unicode characters (like █ and ▀)
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


class DocTableParser(HTMLParser):
    """Parses HTML table rows and cells from published Google Docs."""

    def __init__(self):
        super().__init__()
        self.in_cell = False
        self.rows: list[list[str]] = []
        self.current_row: list[str] = []
        self.current_cell: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]):
        if tag == "tr":
            self.current_row = []
        elif tag in ("td", "th"):
            self.in_cell = True
            self.current_cell = []

    def handle_endtag(self, tag: str):
        if tag in ("td", "th"):
            self.in_cell = False
            self.current_row.append("".join(self.current_cell).strip())
        elif tag == "tr":
            if self.current_row:
                self.rows.append(self.current_row)

    def handle_data(self, data: str):
        if self.in_cell:
            self.current_cell.append(data)


def decode_secret_message(doc_url: str) -> None:
    """
    Fetches the published Google Doc from doc_url, parses the 2D grid coordinates,
    and prints the revealed secret message.
    """
    # 1. Fetch document content
    req = urllib.request.Request(
        doc_url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"},
    )
    with urllib.request.urlopen(req, timeout=15) as response:
        html_content = response.read().decode("utf-8")

    # 2. Extract table rows
    parser = DocTableParser()
    parser.feed(html_content)

    if not parser.rows:
        print("No table data found in the document.")
        return

    # 3. Dynamically identify columns (x, char, y)
    col_map: dict[str, int] = {}
    grid: dict[tuple[int, int], str] = {}

    for row in parser.rows:
        if not row:
            continue

        lower_cells = [cell.lower() for cell in row]

        # Check for header row
        if any("x" in c for c in lower_cells) and any("y" in c for c in lower_cells):
            for idx, cell in enumerate(lower_cells):
                if "x" in cell:
                    col_map["x"] = idx
                elif "y" in cell:
                    col_map["y"] = idx
                elif "char" in cell:
                    col_map["char"] = idx
            continue

        # Extract data row
        x_idx = col_map.get("x", 0)
        char_idx = col_map.get("char", 1)
        y_idx = col_map.get("y", 2)

        try:
            x = int(row[x_idx])
            char = row[char_idx]
            y = int(row[y_idx])
            grid[(x, y)] = char
        except (ValueError, IndexError):
            continue

    if not grid:
        print("No valid coordinate data could be parsed.")
        return

    # 4. Determine grid bounds
    max_x = max(x for x, y in grid.keys())
    max_y = max(y for x, y in grid.keys())

    # 5. Render and print the grid (Cartesian orientation: max_y down to 0)
    for y in range(max_y, -1, -1):
        line = "".join(grid.get((x, y), " ") for x in range(max_x + 1))
        print(line)


if __name__ == "__main__":
    doc_url = (
        "https://docs.google.com/document/d/e/"
        "2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
    )
    decode_secret_message(doc_url)
