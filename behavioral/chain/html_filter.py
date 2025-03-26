class HTMLFilter:
    def __init__(self, next_filter=None):
        self._next = next_filter

    def filter(self, text):
        cleaned = text.replace("<script>", "").replace("</script>", "")
        return self._next.filter(cleaned) if self._next else cleaned

class ProfanityFilter:
    def __init__(self, next_filter=None):
        self._next = next_filter

    def filter(self, text):
        cleaned = text.replace("плохое_слово", "***")
        return self._next.filter(cleaned) if self._next else cleaned


filter_chain = HTMLFilter(ProfanityFilter())
dirty_text = "<script>alert('плохое_слово')</script>"
clean_text = filter_chain.filter(dirty_text)
print(clean_text)  # "alert('***')"