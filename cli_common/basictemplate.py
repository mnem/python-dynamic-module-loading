import re

def render_string_template(template_string, template_context):
    """Renders a template_string to a string, using the supplied
    template_context object to provide the values.

    The template string may contain replaceable values surrounded
    by double curly braces. For example:

        'Replace this: {{value_to_replace}}'

    When a replaceable value is discovered, it's name is used to
    look up the replacement value from template_context. For example,
    assume that the above string is rendered with the following
    dict as the template context:

        dict(value_to_replace='foo')

    This will return the string:

        'Replace this: foo'

    If the replaceable value is not found in the template_context
    it is simply omitted from the output string. Replaceable values
    may be named the same - all will be replaced. Values are
    converted to strings with the inbuilt str function before
    rendering.

    returns the rendered template as a string
    """
    rendered = ""
    section_start = 0
    template_item_matcher = r'{{(.*?)}}'
    matches = re.finditer(template_item_matcher, template_string, re.MULTILINE)
    for match_num, match in enumerate(matches):
        rendered += template_string[section_start:match.start()]
        section_start = match.end()
        replacement_key = match.group(1)
        if template_context.has_key(replacement_key):
            rendered += str(template_context[replacement_key])
    rendered += template_string[section_start:]
    return rendered

#######################################################
# Unit tests
import unittest

class BasicTemplateTests(unittest.TestCase):
    def test_empty_string(self):
        string = ''
        context = { 'item': 'test'}
        result = render_string_template(string, context)
        expected = ''
        self.assertEqual(expected, result)

    def test_empty_context(self):
        string = 'This is a {{item}}.'
        context = {}
        result = render_string_template(string, context)
        expected = 'This is a .'
        self.assertEqual(expected, result)

    def test_single_line_with_string(self):
        string = 'This is a {{item}}.'
        context = {'item': 'test'}
        result = render_string_template(string, context)
        expected = 'This is a test.'
        self.assertEqual(expected, result)

    def test_single_line_with_number(self):
        string = '{{item}} is the magic number.'
        context = {'item': 3}
        result = render_string_template(string, context)
        expected = '3 is the magic number.'
        self.assertEqual(expected, result)

    def test_single_line_with_duplicate_replacements(self):
        string = 'This is a {{item}}{{item}}{{item}}.'
        context = {'item': 'test'}
        result = render_string_template(string, context)
        expected = 'This is a testtesttest.'
        self.assertEqual(expected, result)

    def test_single_line_with_only_replacements(self):
        string = '{{item}}{{item}}{{item}}'
        context = {'item': 'test'}
        result = render_string_template(string, context)
        expected = 'testtesttest'
        self.assertEqual(expected, result)

    def test_single_line_with_only_missing_replacements(self):
        string = '{{item}}{{item}}{{item}}'
        context = {'itemx': 'test'}
        result = render_string_template(string, context)
        expected = ''
        self.assertEqual(expected, result)


    def test_multiple_line_replacements(self):
        string = 'See {{dog}} run.\nRun {{dog}} run.\nDid you see {{dog}} run?\n{{answer}}'
        context = {'dog': 'spot', 'answer': 'yes'}
        result = render_string_template(string, context)
        expected = 'See spot run.\nRun spot run.\nDid you see spot run?\nyes'
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
