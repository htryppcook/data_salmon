
import random

class ChoiceMethod:
    @classmethod
    def value_choice(cls, field):
        def value_generator():
            while True:
                yield field.value
        return value_generator

    @classmethod
    def random_choice(cls, field):
        def random_choice_generator():
            length = len(field.choices)
            while length == len(field.choices):
                yield random.choice(field.choices)
            raise StopIteration()
        return random_choice_generator

    @classmethod
    def ordered_choice(cls, field):
        def ordered_generator():
            index = 0
            length = len(field.choices)
            while length == len(field.choices):
                yield field.choices[index]
                index += 1
                if index >= length:
                    index = 0
            raise StopIteration()
        return ordered_generator

    @classmethod
    def check_min_max(cls, field):
        if field.min == None or field.max == None:
            raise ValueError('Missing value: min={}, max={}'.format(
                field.min, field.max))

        if field.min > field.max:
            raise ValueError('Min is larger than max! min={}, max={}'.format(
                field.min, field.max))

    @classmethod
    def check_increment(cls, field):
        if field.increment == None:
            raise ValueError(
                'Missing value: increment={}'.format(field.increment))

    @classmethod
    def incremental_range(cls, field):
        cls.check_min_max(field)
        cls.check_increment(field)

        def incremental_generator():
            index = field.min
            while True:
                yield index
                index += field.increment
                if field.increment >= 0:
                    if index >= field.max:
                        index = field.min
                else:
                    if index <= field.min:
                        index = field.max - 1
        return incremental_generator

    @classmethod
    def random_range(cls, field):
        cls.check_min_max(field)

        def random_range_generator():
            while True:
                yield random.randrange(field.min, field.max)
        return random_range_generator

    @classmethod
    def evaluate_choice_method(cls, choice_method):
        if choice_method == 'value':
            return cls.value_choice
        elif choice_method == 'random_choice':
            return cls.random_choice
        elif choice_method == 'ordered_choice':
            return cls.ordered_choice
        elif choice_method == 'incremental_range':
            return cls.incremental_range
        elif choice_method == 'random_range':
            return cls.random_range
        else:
            raise NotImplementedError(
                "'{}' is not a valid choice method.".format(choice_method))
