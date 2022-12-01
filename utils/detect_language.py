from typing import Optional

from googletrans import Translator


class DetectLanguage:
    DEFAULT = 'uz'

    def __init__(self, sentences: Optional[str]) -> Optional[None]:
        self.translator = Translator()
        self.sentences = sentences

    @property
    def get_language(self) -> Optional[str]:
        return self.translator.translate(self.sentences).src

    def is_language(self, lang: Optional[str] = DEFAULT):
        if self.get_language != lang:
            return False
        return True
