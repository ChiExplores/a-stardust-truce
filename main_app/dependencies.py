element = 'element'
property = 'property'
all_elements = ('single-link-node','double-link-list-node')
all_properties = ('list-head','list-size', 'list-tail')
all_methods = ('list-push','list-pop','list-peek','list-is-empty', 'list-enqueue', 'list-dequeue')

dependencies = {
    'properties': {
        'list-head': ['single-link-node', 'double-link-list-node',],
        'list-size': ['single-link-node', 'double-link-list-node',],
        'list-tail': ['single-link-node', 'double-link-list-node',],
    },
    'methods': {
        'list-push': {
            element: ['single-link-node', 'double-link-list-node',],
            property: ['list-head',]
        },
        'list-pop': {
            element: ('single-link-node', 'double-link-list-node',),
            property: ('list-head',)
        },
        'list-peek': {
            element: ('single-link-node', 'double-link-list-node',),
            property: ('list-head',)
        },
        'list-is-empty': {
            element: ('single-link-node', 'double-link-list-node',),
            property: all_properties
        },
        'list-enqueue': {
            element: {'single-link-node', 'double-link-list-node',},
            property: {'list-tail',}
        },
        'list-dequeue': {
            element: {'single-link-node', 'double-link-list-node',},
            property: {'list-head',}
        },
    }
}

# to search for dependencies of property
def checkProperty(property, element):
    if element in dependencies['properties'][property]:
        return True
    else:
        return False

# search for dependencies of method
def checkMethod(method, element, property):
    if element in dependencies['methods'][method]['element'] and property in dependencies['methods'][method]['property']:
        return True
    else:
        return False

