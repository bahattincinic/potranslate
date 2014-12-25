import goslate
import polib
import os

from clint.textui import colored, puts, prompt, progress
from clint.textui.validators import RegexValidator, ValidationError


class PoFileValidator(object):
    message = 'Enter a valid path.'

    def __call__(self, value):
        try:
            if not os.path.isfile(value):
                raise IOError()
            polib.pofile(value)
        except IOError:
            raise ValidationError(self.message)
        return value


def main():
    gs = goslate.Goslate()
    puts(colored.green('PO File translation with GoogleTranslate', bold=True))
    path = prompt.query('POFile Path: ', validators=[PoFileValidator()])
    po = polib.pofile(path)
    target_language = prompt.query('Target Language: ',
                                   validators=[RegexValidator(r'.+')])
    source_language = prompt.query('Source Language: ',
                                   validators=[RegexValidator(r'.+')])

    for entry in progress.bar(po, expected_size=len(po)):
        translate = gs.translate(entry.msgid, target_language,
                                 source_language)
        entry.msgstr = translate
    po.save()
    puts(colored.green('%s saved' % path))

if __name__ == '__main__':
    main()
