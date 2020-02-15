# Questionnaire DSL

A DSL for describing questionnaires with a simple terminal interpreter.

Example:
```
Q[type]: Project type
1[lang]. Language project
2[gen]. Generator project

Q[type=lang, extension]: File extension (e.g. "*.que"):
___ /\*\.[a-z0-9]+/

Q[package]: Package name
___ /[a-z][a-z0-9_]*$/

Q: Author name
___

Q: Author email
___

Q: This question is to
   test multiline feature and indenting.
   1. Working
   2. Not working.
      This is also to test multiline in choices.
```

Each question is of the form `Q:` or `Q[<comma separated terms>]`. If `[]` with
terms is given, each term is either a question ID or a boolean expression of the
form `<lhs>=<rhs>` where `<lhs>` is a reference to previous question ID while
`<rhs>` is a value of the previous question which must be satisfied for this
question to be used. This is handy if the questions that follows depends on the
answer. See `File extension` question above which is asked only for language
projects (thus `type=lang`, the `type` is a reference to the previous question).

The type of the question is either free-form (specified by `___`) or choice if
enumerated options are given.

Both question and option can span multiple lines (like in the last question).

For free-form question an optional regular expression can be given inside `//`
(see `Package name` above). This regex is an input validator.

This package provides an interpreter of the questionnaire
`txquestionnaire.questionnaire_interpreter(model, data=None)` which accepts the
model created by parsing of questionnaire description using this language and
optionally a dictionary of default answers keyed by either question ID if given
or question number. The interpreter will run the questionnaire on the console
and return a dictionary of collected data. The values for options are ordinal
numbers or IDs if given (like in `Project type` above -- `lang`, `gen`).

Please see
[tests](https://github.com/textX/textx-lang-questionnaire/tree/master/tests) for
the detailed usage.
