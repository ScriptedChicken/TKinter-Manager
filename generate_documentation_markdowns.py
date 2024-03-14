from pathlib import Path
from os.path import join


def create_markdown(module_name: str, origin_dir: str, docs_dir: str) -> None:
    markdown_name = module_name.replace(".py", ".md")
    markdown_path = join(docs_dir, markdown_name)
    python_path = join(origin_dir, module_name)
    with open(markdown_path, "w") as file:
        file.write(f"::: {python_path}")


def return_clean_name(name: str) -> str:
    parts_capitalised = [
        part.capitalize() for part in name.replace(".md", "").split("_")
    ]
    return " ".join(parts_capitalised)


def generate_documentation_markdowns(module_name):
    src_path = Path(".\src")
    docs_path = Path(".\docs")
    markdown_name_list = []

    for path in src_path.glob("**/*.py"):
        path_str = str(path)
        if "__" not in path_str:
            path_parts = path_str.split("\\")
            markdown_name = path_parts[-1].replace(".py", ".md")
            markdown_path = join(".", "docs", markdown_name)
            python_import_str = ".".join(path_parts).replace(".py", "")

            with open(markdown_path, "w") as file:
                file.write(f"::: {python_import_str}")

            markdown_name_list.append(markdown_name)

    with open(join(".", "docs", "index.md"), "w") as file:
        text = f"# {module_name}\n\n"
        for name in markdown_name_list:
            text += f"[{return_clean_name(name)}]({name})        \n"
        file.write(text)


generate_documentation("TKinter Manager")
