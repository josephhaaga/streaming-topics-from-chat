from nltk import word_tokenize, pos_tag, RegexpParser, ne_chunk, tree


def get_entities_by_type(sent):
    """Returns a map of entities sorted by type."""
    pos_tagged_tokens = pos_tag(word_tokenize(sent))
    chunk_tree = ne_chunk(pos_tagged_tokens)
    entities = [x for x in chunk_tree if type(x) == tree.Tree]

    entities_by_label = {}
    for entity in entities:
        entity_type = entity.label()
        if entity_type not in entities_by_label:
            entities_by_label[entity_type] = []
        entities_by_label[entity_type] += [entity]

    return entities_by_label


