from igraph import Graph as IGraph


def edgelist_to_igraph(edgelist):
    raw = map(lambda x: [x['source'], x['target'], int(x['weight'])], edgelist)
    return IGraph.TupleList(raw, weights=True, directed=True, vertex_name_attr='label')


def _update(s, data):
    s.update([data['source'], data['target']])
    return s


def edgelist_to_nodes(edgelist):
    return reduce(lambda acc, data: _update(acc, data), edgelist, set())


def collapse_node(e, namespace):
    edge = dict.copy(e)
    if edge['source'].find(namespace) > -1:
        edge['source'] = namespace
    elif edge['target'].find(namespace) > -1:
        edge['target'] = namespace
    return edge


def filter_nodes(edgelist, term):
    return filter(lambda x: (x['source'].find(term) + x['target'].find(term)) == -2, edgelist)
