__doc__ = '''Facts Capture'''

__version__ = "0.0.19"

from .executions import Execute_By_Login as capture
from .executions import Execute_By_Individual_Commands as capture_individual
from ._detection import quick_display
from ._cap_summary import LogSummary