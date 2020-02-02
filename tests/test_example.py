from os.path import join, dirname
from textx import metamodel_for_language


def test_example():
    mm = metamodel_for_language('questionnaire')
    questionnaire = mm.model_from_file(join(dirname(__file__), 'example.qus'))

    assert len(questionnaire.questions) == 5
    assert questionnaire.questions[2].text == 'Author name'
    assert questionnaire.questions[1].type.__class__.__name__ == 'Free'
    assert questionnaire.questions[0].type.__class__.__name__ == 'Choice'
    assert questionnaire.questions[4].text == \
        'This question is to test multiline feature and indenting.'
    opt = questionnaire.questions[4].type.options
    assert len(opt) == 2
    assert opt[0].num == 1
    assert opt[0].text == 'Working'
