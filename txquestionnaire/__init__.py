from os.path import join, dirname
from textx import language, metamodel_from_file


@language('questionnaire', '*.qus')
def questionnaire():
    "A language for definition of simple questionnaires"
    def question_processor(q):
        """
        Processor for Question objects.
        """
        q.text = ' '.join(q.text)
        return q

    mm = metamodel_from_file(join(dirname(__file__), 'questionnaire.tx'))
    mm.register_obj_processors({'Question': question_processor})
    return mm
