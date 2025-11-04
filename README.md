# 🧮 ccwc — Python `wc` Clone

`ccwc` is a command-line utility written in Python using [Typer](https://typer.tiangolo.com/).
It replicates the functionality of the classic Unix `wc` (word count) command, allowing you to count lines, words, bytes, and characters in files or from standard input.

---

## 🚀 Installation

```bash
pip install .
```

## 🧰 Usage

**Count lines in a file**
```bash
ccwc -l test.txt
```
**Count words in a file**
```bash
ccwc -w test.txt
```
**Count characters in a file**
```bash
ccwc -m test.txt
```
**Count bytes in a file**
```bash
ccwc -c test.txt
```
