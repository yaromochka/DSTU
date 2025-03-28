from PythonLang.MethodsOfProgramming.Lections.BST.core.Tree import BST


def main() -> None:
    tree = BST()
    tree.insert(50)
    tree.insert(30)
    tree.insert(70)
    tree.insert(20)
    tree.insert(40)
    tree.insert(60)
    tree.insert(80)

    print("Обход in-order:", tree.inorder())

    print("Поиск 40:", tree.search(40) is not None)
    print("Поиск 100:", tree.search(100) is not None)

    tree.delete(50)
    print("После удаления 50:", tree.inorder())


if __name__ == "__main__":
    main()