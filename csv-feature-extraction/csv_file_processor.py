from pathlib import Path
from typing import Any, Callable

from tqdm import tqdm

file_types = ('.csv',)
file_types += tuple(map(str.upper, file_types))

class CSVFileProcessor:
    def __init__(self, csv_dir: Path, process_fn: Callable[[Path], Any]):
        self.csv_dir = csv_dir
        self.extraction_fn = process_fn
        self.files = self.feature_files(csv_dir)

    def feature_files(self, csv_dir: Path) -> list[Path]:
        return [p for p in csv_dir.rglob("./**/*") if p.suffix in file_types]

    def process(self):
        for file in tqdm(self.files):
            result = self.extraction_fn(file)
            if result is not None:
                yield((file, result))
            else:
                print(f"Error processing {file}")