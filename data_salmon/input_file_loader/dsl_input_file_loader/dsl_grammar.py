
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
    field_name = Regex("(?:\\w+)")
    strategy = Regex("(?:\\w+)")

    field_type = Choice(
        Keyword('string'),
        Keyword('int16'),
        Keyword('int32'),
        Keyword('int64'),
        Keyword('uint16'),
        Keyword('uint32'),
        Keyword('uint64')
    )

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

    START = Sequence(
        word,
        Token('{'),
        Repeat(field, mi=1),
        Token('}')
    )
