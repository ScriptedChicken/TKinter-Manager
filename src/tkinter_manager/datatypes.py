from typing import Union, List, Dict
from .label_manager import LabelManager
from .button_manager import ButtonManager
from .dropdown_manager import DropdownManager
from .text_input_manager import TextInputManager
from .layout_manager import LayoutManager
from .progress_bar_manager import ProgressBarManager
from .container_manager import ContainerManager

InputValue = Union[str | int | float]
Dimension = Union[int | float]
LayoutSchema = List[List[str]]
ManagerElement = Union[
    LabelManager,
    ButtonManager,
    DropdownManager,
    TextInputManager,
    LayoutManager,
    ProgressBarManager,
    ContainerManager,
]
ElementsDict = Dict[str, ManagerElement]
Hook = Union[function | None]
Number = Union[int | float]
