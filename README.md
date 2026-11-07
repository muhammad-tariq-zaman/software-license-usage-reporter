# software-license-usage-reporter

Report licence usage per product — used versus owned, as a percentage, highest first — and flag any product used beyond its licence count.

## How to run

```sh
python3 main.py licences.csv
```

## Example output

```
EditorPro: OVERUSED (12/10 used, 120%)
ViewerLite: OK (4/10 used, 40%)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
