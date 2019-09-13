dependencies = {
    properties: {
        head: 'single_link_node', 'double_link_list_node',
        list_size: 'single_link_node', 'double_link_list_node',
    },
    methods: {
        push_list: {
            element: 'single_link_node', 'double_link_list_node',
            property: 'head',
        },
    }
}

# to search for dependencies of property
# dependences['properities'][some_prop].get(data_structure['element'], 'That Property Can\'t Be added to this Data Structure!')
# dependences['methods'][some_method]['element'].get(data_structure['element'], 'That Method Can\'t Be added to this Data Structure!')
# dependences['methods'][some_method]['property'].get(data_structure['property'], 'That Method Can\'t Be added to this Data Structure!')