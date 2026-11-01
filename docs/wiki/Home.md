# Poem PIN Extractor — Project Wiki

A deterministic text transformation. For each line at index i, it reads the word at word index i and appends that word's length; if the word does not exist, it appends 0. This is not a security PIN generator.

## Quick start

```bash
python main.py
```
Open `index.html` for the browser demonstration. Text is processed locally in the browser.

## Key repository references

- [Source repository](https://github.com/aKmsdfhjb/poem-pin-extractor)
- [README](https://github.com/aKmsdfhjb/poem-pin-extractor#readme)
- [Architecture](Architecture.md)

## Scope and limitations

This wiki describes the repository as it exists today. A working static page does not imply that a Python API, model inference service, database, payment integration or external provider has also been deployed. Check the repository README and Actions history before treating a feature as production-ready.

## Documentation maintenance

Update this page when the implementation, dependencies, model artifacts or deployment architecture changes. Keep credentials, private user data and unlicensed datasets out of the repository.

- [Video production brief](https://github.com/aKmsdfhjb/poem-pin-extractor/blob/main/docs/video/production-brief.md)
