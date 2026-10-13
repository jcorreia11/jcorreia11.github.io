# Personal Website

## Citation utilities

The Python scripts in `utils/` are managed with [uv](https://docs.astral.sh/uv/).

```bash
uv sync                                  # create .venv and install dependencies
cd utils && uv run python scopus.py      # or google_scholar.py / web_of_science.py
```
