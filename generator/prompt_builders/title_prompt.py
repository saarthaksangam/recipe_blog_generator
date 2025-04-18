from generator.prompt_builders import load_prompt_template

def build_title_prompt(filename: str) -> str:
    template = load_prompt_template("clean_title_prompt.md")
    return template.replace("{filename}", filename)
