def _update(s, data):
        s.update([data['source'], data['target']])
        return s


def edgelist_to_nodes(edge_list):
    return reduce(lambda acc, data: _update(acc, data), edge_list, set())


def collapse_node(e, namespace):
    edge = dict.copy(e)
    if edge['source'].find(namespace) > -1:
        edge['source'] = namespace
    elif edge['target'].find(namespace) > -1:
        edge['target'] = namespace
    return edge


def filter_nodes(edge_list, term):
    return filter(lambda x: (x['source'].find(term) + x['target'].find(term)) == -2, edge_list)
