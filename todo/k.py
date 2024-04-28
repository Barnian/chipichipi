class TestClass:
    def __init__(self, t: str):
        self.type = t

    def __str__(self):
        return f"TestClass(\"{self.type}\")"

    def __repr__(self):
        return str(self)


# будем искать до dog (dog -> kotik), doggo (doggo -> koshka)
dict_replace = {'dog': 'kotik',
                'doggo': 'koshka'}

lst = [TestClass('cat'),
       TestClass('cot'),
       TestClass('kote'),
       TestClass('dog'),
       TestClass('kot'),
       TestClass('doggo')]

lst_parts = []
print(lst)
while lst:
    print("=" * 20)
    index, elem = next(filter(lambda elem_with_index: elem_with_index[1].type in ('dog', 'doggo'), enumerate(lst)), None)
    # тоже самое в этом примере было бы
    # index, elem = next(filter(lambda elem_with_index: elem_with_index[1].type in dict_replace, enumerate(lst)), None)
    lst_parts.append(list(map(lambda x: TestClass(dict_replace[elem.type]), lst[:index])) + [lst[index]])
    # или без пересоздания экземляров
    # for i, x in enumerate(lst[:index]):
    #     lst[i].type = dict_replace[elem.type]
    # lst_parts.append(lst[:index + 1])
    lst = lst[index + 1:]
print(*lst_parts, sep='\n')



