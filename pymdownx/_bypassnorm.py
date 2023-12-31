
"""
Bypass whitespace normalization.
pymdownx._bypassnorm
Strips `SOH` and `EOT` characters before whitespace normalization
allowing other extensions to then create preprocessors that stash HTML
with `SOH` and `EOT`  After whitespace normalization, all `SOH` and
`EOT` characters will be converted to the Python Markdown standard
`STX` and `ETX` convention since whitespace normalization usually
strips out the `STX` and `ETX` characters.
Copyright 2014 - 2018 Isaac Muse <isaacmuse@gmail.com>
"""

from markdown import Extension
from markdown.util import STX, ETX
from markdown.preprocessors import Preprocessor

SOH = '\u0001'  # start
EOT = '\u0004'  # end


class PreNormalizePreprocessor(Preprocessor):
    """Preprocessor to remove workaround symbols."""

    def run(self, lines):
        """Remove workaround placeholder markers before adding actual workaround placeholders."""

        source = '\n'.join(lines)
        source = source.replace(SOH, '').replace(EOT, '')
        return source.split('\n')


class PostNormalizePreprocessor(Preprocessor):
    """Preprocessor to clean up normalization bypass hack."""

    def run(self, lines):
        """Convert alternate placeholder symbols to actual placeholder symbols."""

        source = '\n'.join(lines)
        source = source.replace(SOH, STX).replace(EOT, ETX)
        return source.split('\n')


class BypassNormExtension(Extension):
    """Bypass whitespace normalization."""

    def __init__(self, *args, **kwargs):
        """Initialize."""

        self.inlinehilite = []
        self.config = {}
        super(BypassNormExtension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md):
        """Add extensions that help with bypassing whitespace normalization."""

        md.preprocessors.register(PreNormalizePreprocessor(md), "pymdownx-pre-norm-ws", 35)
        md.preprocessors.register(PostNormalizePreprocessor(md), "pymdownx-post-norm-ws", 29.9)


def makeExtension(*args, **kwargs):
    """Return extension."""

    return BypassNormExtension(*args, **kwargs)