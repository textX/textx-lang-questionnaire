import re
from os.path import join, dirname
from textx import language, metamodel_from_file


@language('questionnaire', '*.qus')
def questionnaire():
    "A language for definition of simple questionnaires"
    def multiline_text_processor(o):
        """
        Processor for objects having multiline `text` field.
        """
        o.text = ' '.join(o.text)
        return o

    def free_type_question(o):
        "Strip slashes from regex"
        if o.regex:
            o.regex = o.regex[1:-1]

    mm = metamodel_from_file(join(dirname(__file__), 'questionnaire.tx'))
    mm.register_obj_processors({'Question': multiline_text_processor,
                                'Free': free_type_question,
                                'ChoiceOption': multiline_text_processor})
    return mm


def questionnaire_interpret(model, data=None):
    """
    Interprets Questionnaire model asking question and collecting answers from
    terminal.

    `data` contains initial/default answers.
    """

    data = data or {}

    for qid, question in enumerate(model.questions):
        qid = question.qid or qid
        qtype = question.type.__class__.__name__

        print(question.text)
        if qtype == 'Choice':
            for option in question.type.options:
                print(option.num, '. ', option.text)

        default = data.get(qid, None)
        while True:
            ans = input('{}> '.format(
                default if default is not None else '')) or default

            if ans == 'quit':
                return data

            if qtype == 'Free' and question.type.regex:
                if not re.match(question.type.regex, ans):
                    print(f'Invalid input. '
                          f'Should match "{question.type.regex}"')
                    continue
            elif qtype == 'Choice':
                try:
                    ans = int(ans)
                except ValueError:
                    print('Invalid input. Should be a number.')
                    continue
                if ans not in [o.num for o in question.type.options]:
                    print('Invalid input. Should be a number [{}-{}]'.format(
                        question.type.options[0].num,
                        question.type.options[-1].num))
                    continue
            break

        data[qid] = ans

    return data