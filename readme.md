
## create/ update requirements.txt

```sh
# all packages from environment
pip freeze > requirements.txt

# or use pipreqs that install only used packaqes from scripts
pip install pipreqs
pipreqs main.py
```

## CIcls

see [main.yml](./.github/workflows/main.yml)