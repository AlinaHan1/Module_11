def introspection_info(obj):
    obj_type = type(obj).__name__
    print(f'Type: {obj_type}')
    attributes_obj = dir(obj)
    print(f'Attributes: {attributes_obj}')
    methods = [method for method in attributes_obj if callable(getattr(obj, method))]
    print(f'Methods: {methods}')
    module = obj.__class__.__module__
    return f'Module: {module}'
    # info = {'type': obj_type, 'attributes': attributes_obj, 'methods': methods, 'module': module}
    # return info


number_info = introspection_info(42)
print(number_info)
string_info = introspection_info('my string')
print(string_info)


class House:
    house_history = []

    def __new__(cls, *args):
        cls.house_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


h1 = introspection_info(House('ЖК Эльбрус', 10))
print(h1)
