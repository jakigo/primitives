from maker.parameter_basket import get_parameter, set_parameter, add_parameter

def parameters(param):
    def explore(params_list):
        resp = {}
        for k, v in params_list.items():
            if type(v) != dict:
                resp[k] = add_parameter(k, v)
            else:
                resp[k] = explore(v)
        return resp

    def params(func):
        def inner(*args, **kwargs):
            obj = func(*args, **kwargs)
            inner_params = explore(param)
            obj._parameters = inner_params
            return obj
        return inner
    return params

def compare_dict(dictA, dictB):
    if dictA == None or dictB == None:
        return False
    if dictA.keys() != dictB.keys():
        return False

    for k, v in dictA.items():
        if type(v) == dict:
            if not compare_dict(dictA[k], dictB[k]):
                return False
        else:
            if v != dictB[k]:
                return False
    return True

class Component:
    def __init__(self):
        self._values_cache = self.fetch_parameters_values()
        
    def fetch_parameters_values(self):
        def extract_from(dictz):
            ret = {}
            for k, v in dictz:
                if type(v) != dict:
                    ret[k] = get_parameter(v)
                else:
                    ret[k] = extract_from(v)
            return ret
        return extract_from(self._parameters.items())      


    
    def eval(self):
        new_params = self.fetch_parameters_values()
        if compare_dict(self._values_cache, new_params):
            return self.mesh
        print("regen")
        self.mesh = self.create()
        self._values_cache = new_params
        
        return self.mesh





