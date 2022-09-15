from code import cli, config
from code.columns.Sym import Sym


cli_object = cli.Cli()
the = cli_object
config.the["nums"] = cli_object.the['nums']
print(cli_object.the)


if __name__ == '__main__':
    symObj = Sym()
    symObj.add("a")
    symObj.add("a")
    symObj.add("a")
    symObj.add("a")
    symObj.add("b")
    symObj.add("b")
    symObj.add("c")
    print(symObj.mid())
    symObj.div()
