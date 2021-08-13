parameters_list = {}
parameters_from_file = {}
def add_parameter(name, start_value):
    global parameters_list
    global parameters_from_file
    global load

    number = max([int(x.split("_")[1]) for x in parameters_list.keys() if name in x] + [-1]) + 1
    key = f"{name}_{number}"
    parameters_list[key] = parameters_from_file.get(key, start_value)
    return key

def get_parameter(name):
    global parameters_list
    return parameters_from_file.get(name,parameters_list[name])

def set_parameter(name, value):
    global parameters_list
    parameters_list[name] = value

def save_parameters():
    global parameters_list
    with open("parameters.json","w") as f:
        import json
        f.write(json.dumps(parameters_list, indent=4, sort_keys=True))

def load_parameters():
    global parameters_from_file
    try:
        with open("parameters.json","r") as f:
            import json
            parameters_from_file_now = json.loads(f.read())
            if parameters_from_file_now == parameters_from_file:
                return False
            else:
                parameters_from_file = parameters_from_file_now
                return True
    except:
        parameters_from_file = {}
        return True

