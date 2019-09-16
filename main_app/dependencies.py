element = 'element'
property = 'property'
all_elements = ('single_link_node', 'double_link_list_node')
all_properties = ('head', 'list_size')

dependencies = {
    'properties': {
        'head': ('single_link_node', 'double_link_list_node',),
        'list_size': ('single_link_node', 'double_link_list_node',),
    },
    'methods': {
        'push_list': {
            element: ('single_link_node', 'double_link_list_node',),
            property: ('head',)
        },
        'pop_list': {
            element: ('single_link_node', 'double_link_list_node',),
            property: ('head',)
        },
        'peek_list': {
            element: ('single_link_node', 'double_link_list_node',),
            property: ('head',)
        },
        'is_empty_list': {
            element: ('single_link_node', 'double_link_list_node',),
            property: all_properties
        }
    }
}

# to search for dependencies of property
def checkProperty(property, data_structure, success, failure):
    if data_structure['element'] in dependencies['properities'][property]:
        return success
    else:
        return failure

# search for dependencies of method
def checkMethod(method, data_structure, success, failure):
    if data_structure['element'] in dependencies['methods'][method]['element'] and data_structure['property'] in dependencies['methods'][method]['property']:
        return success
    else:
        return failure