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

# if data_structure['element'] in dependences['properities'][some_prop]:
#     return 'That Property Can be added to this Data Structure!' 
# else:
#     return 'Sorry, that Property Can\'t Be added to this Data Structure!'

# search for dependencies of method
# if data_structure['element'] in dependences['methods'][some_method]['element'] and data_structure['property'] in dependences['methods'][some_method]['property']:
#     return 'That Property Can be added to this Data Structure!'
# else:
#     return 'Sorry, that Property Can\'t Be added to this Data Structure!'