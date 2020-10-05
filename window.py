
"""
Window module.
Contains a Window class that inherits from
pySimpleGUI.Window that refreshs on update
and can be styled on instantiation.
"""

from datetime import datetime
from typing import Tuple

import PySimpleGUI as sg


class Window(sg.Window):
    """
    Window class. Inherits from PySimpleGui.Window.
    
    Parameters
    ----------
    theme : `str`
        String containing a valid PySimpleGUI theme.

    justify : `str`
        String containing a position for text justifying (e.g left).

    font : Tuple[`str`, `int`]
        Tuple containing a font title and it size.

    button : Tuple[`str`, `str`]
        Tuple containing primary and secondary color for buttons.
    """
    def __init__(self,
                 theme: str,
                 justify: str,
                 font: Tuple[str, int],
                 button: Tuple[str, str]) -> None:

        sg.theme(theme)
        sg.set_options(font=font,
                       button_color=button,
                       text_justification=justify)

        self.layout = [[sg.Frame('', [
            # Search button
            [sg.Text('       URL'),
             sg.InputText(size=(85, 0),
                          key='url'),
             sg.Button('    GO    ', key='search')],
            
            # Folder browse button
            [sg.Text('  Output'),
             sg.InputText(size=(85, 0),
                          key='path', 
                          disabled=True),
             sg.FolderBrowse('BROWSE')],

            # Information interface
            [sg.Text('\nTitle:', size=(90, 0), key='title')],
            [sg.Text('Author:', size=(90,0), key='author')],
            [sg.Text('Length:\n', size=(90, 0), key='length')],
            [sg.Text('Status:')],

            # Status field
            [sg.Multiline(key='status', size=(100, 15), disabled=True)],

            # Download button
            [sg.Text(' Streams'),
             sg.Combo(values='',
                      size=(20, 0),
                      key='stream',
                      readonly=True),
             sg.Button('Download')]
        ])]]

        super().__init__(title='YTDownloader 0.5                        ',
                         layout=self.layout,
                         icon='icon.ico')

        self.content = ''

    def update(*args, **kwargs) -> None:
        """Read self to actually update the window content"""
        super().update(*args, **kwargs)
        self.read(timeout=0.1)

    def s_append(self, content: str) -> None:
        """Receives content and appends it to the status field"""
        now = datetime.now().strftime('%H:%M:%S')
        self.content = f'[{now}] {content}\n\n' + self.content
        self['status'].update(self.content)
        self.read(timeout=0.1)

    def update_header(self,
                      title : str = '',
                      author: str = '',
                      length: str = '') -> None:
        """Used to easily update header with current video info"""
        self['title'].update(title)
        self['author'].update(author)
        self['length'].update(length)

    @property
    def is_closed(self):
        return sg.WINDOW_CLOSED
