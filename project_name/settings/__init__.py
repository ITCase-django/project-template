# Copyright 2025 ITCase (info@itcase.pro)

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.absolute()

from .cache import *  # noqa
from .core import *  # noqa
from .logging import *  # noqa

from .filebrowser import *  # noqa
from .grappelli import *  # noqa
from .rest_framework import *  # noqa
from .rq import *  # noqa

from .project import *  # noqa

from .local import *  # noqa
