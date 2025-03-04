def introspection_info(obj):
    obj_type = type(obj).__name__

    attributes = dir(obj)

    metod = [metod for metod in attributes if callable(getattr(obj, metod))]

    module = obj.__class__.__module__

    info = {'type': obj_type, 'attributes': attributes, 'metod': metod, 'module': module}
    
    return info


number_info = introspection_info(42)
print(number_info)

string_info = introspection_info('Hello')
print(string_info)

list_info = introspection_info([1, 20, 4.0, 'word'])
print(list_info)
