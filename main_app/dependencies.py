element = 'element'
property = 'property'
all_elements = 'single_link_node', 'double_link_list_node'
all_properties = 'head', 'list_size'

dependencies = {
    'properties': {
        'head': 'single_link_node', 'double_link_list_node',
        'list_size': 'single_link_node', 'double_link_list_node',
    },
    'methods': {
        'push_list': {
            element: 'single_link_node', 'double_link_list_node',
            property: 'head',
        },
        'pop_list': {
            element: 'single_link_node', 'double_link_list_node',
            property: 'head',
        },
        'peek_list': {
            element: 'single_link_node', 'double_link_list_node',
            property: 'head',
        }
        is_empty_list: {
            element: 'single_link_node', 'double_link_list_node',
            propery: all_properties
        }
    }
}

# to search for dependencies of property
# TODO make iterable
# dependences['properities'][some_prop].get(data_structure['element'], 'That Property Can\'t Be added to this Data Structure!')
# dependences['methods'][some_method]['element'].get(data_structure['element'], 'That Method Can\'t Be added to this Data Structure!')
# dependences['methods'][some_method]['property'].get(data_structure['property'], 'That Method Can\'t Be added to this Data Structure!')