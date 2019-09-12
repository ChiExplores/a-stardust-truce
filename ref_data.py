class User:
    __def__(self, name: str):
        self.name = name

class Data_Structure:
    __def__(self, name: str, aggregate: dict, description: str):
        self.name = name
        self.description = description
        self.__get_properties__():
            pass
        self.__get_methods__():
            pass
        self.__get_js__():
            pass
        self.__get_py__():
            pass
        self.data_aggregate = data_aggregate

class Data_Aggregate:
    __def__(self, name: str, type: str, dimension: int, code_block: dict, resource: dict):
        # type selected from tuple ('node', 'block')
        self.name = name
        self.type = type
        self.dimension = dimension
        self.code_block = code_block
        self.resource = resource

class Property:
    __def__(self, name: str, type: str, code_block: dict, resource: dict):
        # type selected from tuple ('int', 'str', 'float', 'var')
        self.name = name
        self.type = type
        self.code_block = code_block
        self.resource = resource

class Method:
    __def__(self, name: str, code_block: dict, resource: dict):
        self.name = name
        self.code_block = code_block
        self.resource = resource

class Code_Block:
    __def__(self, python: str, javascript: str):
        self.python = python
        self.javascript = javascript

class Resource:
    __def__(self, description: str, img_url: str):
        self.description = description
        self.img_url = img_url

# instantiations with reference to missing entity arguments
single_link_node = Data_Aggregate('Singly Linked Node', 'node', 1) # code_block, resource
head = Property('Head', 'var') # code_block, resource
list_size = Property('List Size', 'int') # code_block, resource
initialize = Method('Initialize') # code_block, resource
push = Method('Push') # code_block, resource
pop = Method('Pop') # code_block, resource
peek = Method('Peek') # code_block, resource
is_empty = Method('Is Empty') # code_block, resource
stack_list = Structure('Stack - List', single_link_node, 'Linked List Implementation of Data Stack')

# dependency tuples for each method and property model eg
push.agg_dependency = 'single_link_node', 'double_link_node'
push.prop_dependency = 'head', 'last'

# join table representations
data_structure_property = {Stack: head, Stack: list_size}
data_structure_method = {Stack: initialize, Stack: push, Stack: pop, Stack: peek, Stack: is_empty}