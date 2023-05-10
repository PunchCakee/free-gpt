from gpt4free import you
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.pretty import pprint

console = Console()

def get_output(input: str) -> str:
    res = you.Completion.create(prompt=input)
    return res.text



while True:
    try:
        inp = Prompt.ask("Enter a prompt -> ")

        if inp == "":
            print("\nhm it looks like you didnt input anything!")
        else:
            console.print(Markdown(get_output(inp)))
            console.print('\n')
    except KeyboardInterrupt:
        console.print("\nThank you for using gpt-4 free chat come again :)")
        exit()