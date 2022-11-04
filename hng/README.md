# Console App to populate csv with SHA256

This is a console app take a `.csv`, and generate a CHIP-0007 compatible json, and then calculates the sha256 of the json file and append it to each line in the csv (as a filename.output.csv)
The `csv` used has been included in the `csv` folder as `hng.csv` 
the generated `csv` is also saved in the current folder as `filename.output.csv`.

### Sample Reference
- [Chip-0007 JSON Schema Example](https://github.com/Chia-Network/chips/blob/main/assets/chip-0007/example.json)

## How to run the app

- Clone the repository
- `cd` into the root directory where the `file.py ` is present.
- Install python3
- Then run the secript by running `python file.py` in the terminal.
- A filename.output.csv will be generated(Which is the final result)