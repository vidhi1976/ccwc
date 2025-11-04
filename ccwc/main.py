import typer
import sys

app = typer.Typer(add_completion=False)

def count_bytes(data: bytes) -> int:
    return len(data)

def count_lines(data: bytes) -> int:
    return data.count(b'\n')

def count_words(data: bytes) -> int:
    return len(data.split())

def count_chars(data: bytes) -> int:
    return len(data.decode('utf-8', errors='ignore'))

@app.command()
def ccwc(
    file: str = typer.Argument(None, help="File path (optional, read from stdin if not provided)"),
    count_bytes_flag: bool = typer.Option(False, "-c", "--bytes", help="Count bytes"),
    count_words_flag: bool = typer.Option(False, "-w", "--words", help="Count words"),
    count_lines_flag: bool = typer.Option(False, "-l", "--lines", help="Count lines"),
    count_chars_flag: bool = typer.Option(False, "-m", "--chars", help="Count characters"),
):
    
    if file is None:
        data = sys.stdin.buffer.read()
    else:
        with open(file, "rb") as f:
            data = f.read()

    if count_bytes_flag:
        typer.echo(count_bytes(data))
    elif count_words_flag:
        typer.echo(count_words(data))
    elif count_lines_flag:
        typer.echo(count_lines(data))
    elif count_chars_flag:
        typer.echo(count_chars(data))
    else:
        typer.echo(f"{count_lines(data)} {count_words(data)} {count_bytes(data)}")

if __name__ == "__main__":
    app()
