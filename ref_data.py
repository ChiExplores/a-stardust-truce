

class User:
    def __init__(self, name: str):
        self.name = name

class Data_Aggregate:
    def __init__(self, name: str, type: str, dimension: int, code_block: dict, resource: dict):
        # type selected from tuple ('node', 'block')
        self.name = name
        self.type = type
        self.dimension = dimension
        self.code_block = code_block
        self.resource = resource

class Data_Structure:
    def __init__(self, name: str, data_aggregate: Data_Aggregate, description: str):
        self.name = name
        self.description = description
        self.data_aggregate = data_aggregate
    def __get_properties__(self):
        pass
    def __get_methods__(self):
        pass
    def __get_js__(self):
        pass
    def __get_py__(self):
        pass

class Property:
    def __init__(self, name: str, type: str, code_block: dict, resource: dict):
        # type selected from tuple ('int', 'str', 'float', 'var')
        self.name = name
        self.type = type
        self.code_block = code_block
        self.resource = resource

class Method:
    def __init__(self, name: str, code_block: dict, resource: dict):
        self.name = name
        self.code_block = code_block
        self.resource = resource

class Code_Block:
    def __init__(self, python: str, javascript: str):
        self.python = python
        self.javascript = javascript

class Resource:
    def __init__(self, description: str, img_url: str):
        self.description = description
        self.img_url = img_url

# instantiations with reference to missing entity arguments
single_link_node = Data_Aggregate('Singly Linked Node', 'node', 1, None, None) # code_block, resource
head = Property('Head', 'var', None, None) # code_block, resource
list_size = Property('List Size', 'int', None, None) # code_block, resource
initialize = Method('Initialize', None, None) # code_block, resource
push = Method('Push', None, None) # code_block, resource
pop = Method('Pop', None, None) # code_block, resource
peek = Method('Peek', None, None) # code_block, resource
is_empty = Method('Is Empty', None, None) # code_block, resource
stack_list = Data_Structure('Stack - List', single_link_node, 'Linked List Implementation of Data Stack')

# dependency tuples for each method and property model eg
# push.agg_dependency = 'single_link_node', 'double_link_node'
# push.prop_dependency = 'head', 'last'

# join table representations
data_structure_property = {stack_list: head, stack_list: list_size}
data_structure_method = {stack_list: initialize, stack_list: push, stack_list: pop, stack_list: peek, stack_list: is_empty}