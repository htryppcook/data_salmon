
from pyleri import (
    Grammar,
    Keyword,
    Regex,
    Sequence,
    Choice,
    Repeat,
    Token,
    Optional,
    List,
    THIS,
    Prio)

class DSLGrammar(Grammar):
    numeric = Regex("[0-9]+(\.[0-9]+)?")
    quoted_string = Regex("(\"[^\"\\\\]*(?:\\\\.[^\"\\\\]*)*\")")
    word = Regex("(?:\\w+)")

    field_types = (
        'string', 'int16', 'int32', 'int64', 'uint16', 'uint32', 'uint64')
    field_type = Choice(*([Keyword(x) for x in [field_types]]))
    field_name = word
    strategy = word
    strategy_arguments = List(Choice(numeric, quoted_string))

    field = Sequence(
        field_type,
        field_name,
        Token('='),
        strategy,
        Token('('),
        strategy_arguments,
        Token(')')
    )

    dataset = Keyword('dataset')
    dataset_name = word

    dataset_definition = Sequence(
        dataset,
        dataset_name,
        Token('{'),
        Repeat(field, mi=1),
        Token('}')
    )

    START = dataset_definition
