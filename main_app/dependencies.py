element = 'element'
property = 'property'
all_elements = ('single-link-node','double-link-list-node')
all_properties = ('list-head','list-size')
all_methods = ('push-list','pop-list','peek-list','is-empty-list')

dependencies = {
    'properties': {
        'list-head': ('single-link-node', 'double-link-list-node',),
        'list-size': ('single-link-node', 'double-link-list-node',),
    },
    'methods': {
        'push-list': {
            element: ('single-link-node', 'double-link-list-node',),
            property: ('list-head',)
        },
        'pop-list': {
            element: ('single-link-node', 'double-link-list-node',),
            property: ('list-head',)
        },
        'peek-list': {
            element: ('single-link-node', 'double-link-list-node',),
            property: ('list-head',)
        },
        'is-empty-list': {
            element: ('single-link-node', 'double-link-list-node',),
            property: all_properties
        }
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
    if element in dependencies['methods'][method]['element'] and data_structure['property'] in dependencies['methods'][method]['property']:
        return True
    else:
        return True