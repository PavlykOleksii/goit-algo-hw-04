from pathlib import Path
import argparse
import shutil

def parse_args():
    parser = argparse.ArgumentParser(description="Рекурсивне сортування файлів за розширенням")
    
    parser.add_argument("source", help="Шлях до вихідної директорії")
    
    parser.add_argument("output", nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням: dist)")
    
    return parser.parse_args()

def copy_files_recursively(src: Path, dst: Path):
    try:
        for parent_dir_obj in src.iterdir():
            if parent_dir_obj.resolve() == dst.resolve():
                continue

            if parent_dir_obj.is_dir():
                copy_files_recursively(parent_dir_obj, dst)
            elif parent_dir_obj.is_file():
                ext = parent_dir_obj.suffix[1:].lower()

                if ext == "":
                    ext_dir = dst / "no_extension"
                else:
                    ext_dir = dst / ext

                ext_dir.mkdir(parents=True, exist_ok=True)

                dest_file = ext_dir / parent_dir_obj.name

                if dest_file.exists():
                    stem = parent_dir_obj.stem
                    suffix = parent_dir_obj.suffix
                    counter = 1

                    while dest_file.exists():
                        dest_file = ext_dir / f"{stem}_{counter}{suffix}"
                        counter += 1

                shutil.copy2(parent_dir_obj, dest_file)

    except PermissionError:
        print(f"Помилка доступу: {src}")
    except Exception as e:
        print(f"Помилка при обробці {src}: {e}")                      

if __name__ == "__main__":
    args = parse_args()
    source_dir = Path(args.source).resolve()
    output_dir = Path(args.output).resolve()
    if not source_dir.exists() or not source_dir.is_dir():
        print(f"Помилка: Вихідна директорія {source_dir} не існує або це не папка.")
        exit(1)
    
    print(f"Джерело: {source_dir}")
    print(f"Призначення: {output_dir}")
    copy_files_recursively(source_dir, output_dir)
    print("Копіювання та сортування завершено!")