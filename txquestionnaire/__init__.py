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

    mm = metamodel_from_file(join(dirname(__file__), 'questionnaire.tx'))
    mm.register_obj_processors({'Question': multiline_text_processor,
                                'ChoiceOption': multiline_text_processor})
    return mm
