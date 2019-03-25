def degrees(d):
    """Convert degrees to radians.

    Arguments:
    d -- Angle in degrees.
    """
    import math
    return d / 180 * math.pi

class EasyGameError(Exception):
    """All exceptions raised from this module are of this type."""
    pass

class _Context:
    _win = None
    _events = []

_ctx = _Context()

class CloseEvent:
    """Happens when user clicks the X button on the window."""
    pass

_symbol_dict = None

def _symbol_to_string(key):
    global _symbol_dict
    import pyglet
    if _symbol_dict is None:
        _symbol_dict = {
            pyglet.window.key.A: 'A',
            pyglet.window.key.B: 'B',
            pyglet.window.key.C: 'C',
            pyglet.window.key.D: 'D',
            pyglet.window.key.E: 'E',
            pyglet.window.key.F: 'F',
            pyglet.window.key.G: 'G',
            pyglet.window.key.H: 'H',
            pyglet.window.key.I: 'I',
            pyglet.window.key.J: 'J',
            pyglet.window.key.K: 'K',
            pyglet.window.key.L: 'L',
            pyglet.window.key.M: 'M',
            pyglet.window.key.N: 'N',
            pyglet.window.key.O: 'O',
            pyglet.window.key.P: 'P',
            pyglet.window.key.Q: 'Q',
            pyglet.window.key.R: 'R',
            pyglet.window.key.S: 'S',
            pyglet.window.key.T: 'T',
            pyglet.window.key.U: 'U',
            pyglet.window.key.V: 'V',
            pyglet.window.key.W: 'W',
            pyglet.window.key.X: 'X',
            pyglet.window.key.Y: 'Y',
            pyglet.window.key.Z: 'Z',
            pyglet.window.key._0: '0',
            pyglet.window.key._1: '1',
            pyglet.window.key._2: '2',
            pyglet.window.key._3: '3',
            pyglet.window.key._4: '4',
            pyglet.window.key._5: '5',
            pyglet.window.key._6: '6',
            pyglet.window.key._7: '7',
            pyglet.window.key._8: '8',
            pyglet.window.key._9: '9',

            pyglet.window.key.SPACE: 'SPACE',
            pyglet.window.key.ENTER: 'ENTER',
            pyglet.window.key.BACKSPACE: 'BACKSPACE',
            pyglet.window.key.ESCAPE: 'ESCAPE',
            pyglet.window.key.LEFT: 'LEFT',
            pyglet.window.key.RIGHT: 'RIGHT',
            pyglet.window.key.UP: 'UP',
            pyglet.window.key.DOWN: 'DOWN',

            pyglet.window.mouse.LEFT: 'LEFT',
            pyglet.window.mouse.RIGHT: 'RIGHT',
            pyglet.window.mouse.MIDDLE: 'MIDDLE',
        }
    if key not in _symbol_dict:
        return None
    return _symbol_dict[key]

class KeyDownEvent:
    """Happens when user pressed a key on the keyboard.

    Fields:
    key -- String representation of the pressed key.
           These are: 'A' ... 'Z',
                      '0' ... '9',
                      'SPACE', 'ENTER', 'BACKSPACE', 'ESCAPE',
                      'LEFT', 'RIGHT', 'UP, 'DOWN'.
    """
    def __init__(self, key):
        self.key = key

class KeyUpEvent:
    """Happens when user releases a key on the keyboard.

    Fields:
    key -- String representation of the released key.
           These are: 'A' ... 'Z',
                      '0' ... '9',
                      'SPACE', 'ENTER', 'BACKSPACE', 'ESCAPE',
                      'LEFT', 'RIGHT', 'UP, 'DOWN'.
    """
    def __init__(self, key):
        self.key = key

class TextEvent:
    """Happens when user types a text on the keyboard.

    Fields:
    text -- A string containing the typed text.
    """
    def __init__(self, text):
        self.text = text

class MouseMoveEvent:
    """Happens when user moves the mouse.

    Fields:
    x  -- The current X coordinate of the mouse.
    y  -- The current Y coordinate of the mouse.
    dx -- Difference from the previous X coordinate.
    dy -- Difference from the previous Y coordinate.
    """
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

class MouseDownEvent:
    """Happens when user presses a mouse button.

    Fields:
    x      -- The current X coordinate of the mouse.
    y      -- The current Y coordinate of the mouse.
    button -- String representation of the pressed button.
              These are: 'LEFT', 'RIGHT', 'MIDDLE'.
    """
    def __init__(self, x, y, button):
        self.x = x
        self.y = y
        self.button = button

class MouseUpEvent:
    """Happens when user releases a mouse button.

    Fields:
    x      -- The current X coordinate of the mouse.
    y      -- The current Y coordinate of the mouse.
    button -- String representation of the released button.
              These are: 'LEFT', 'RIGHT', 'MIDDLE'.
    """
    def __init__(self, x, y, button):
        self.x = x
        self.y = y
        self.button = button

def open_window(title, width, height, fps=60):
    """Opens a window with the specified parameters. Only one window can be open at any time.

    Arguments:
    title  -- Text at the top of the window.
    width  -- Width of the window in pixels.
    height -- Height of the window in pixels.
    fps    -- Maximum number of frames per second. (Defaults to 60.)
    """
    global _ctx
    import pyglet
    if _ctx._win is not None:
        raise EasyGameError('window already open')
    _ctx._win = pyglet.window.Window(caption=title, width=width, height=height)
    pyglet.clock.set_fps_limit(fps)
    _ctx._win.switch_to()

    @_ctx._win.event
    def on_close():
        global _ctx
        _ctx._events.append(CloseEvent())

    @_ctx._win.event
    def on_key_press(symbol, modifiers):
        global _ctx
        key = _symbol_to_string(symbol)
        if key is None:
            return
        _ctx._events.append(KeyDownEvent(key))

    @_ctx._win.event
    def on_key_release(symbol, modifiers):
        global _ctx
        key = _symbol_to_string(symbol)
        if key is None:
            return
        _ctx._events.append(KeyUpEvent(key))

    @_ctx._win.event
    def on_text(text):
        global _ctx
        _ctx._events.append(TextEvent(text))

    @_ctx._win.event
    def on_mouse_motion(x, y, dx, dy):
        global _ctx
        _ctx._events.append(MouseMoveEvent(x, y, dx, dy))

    @_ctx._win.event
    def on_mouse_press(x, y, symbol, modifiers):
        global _ctx
        button = _symbol_to_string(symbol)
        if button is None:
            return
        _ctx._events.append(MouseDownEvent(x, y, button))

    @_ctx._win.event
    def on_mouse_release(x, y, symbol, modifiers):
        global _ctx
        button = _symbol_to_string(symbol)
        if button is None:
            return
        _ctx._events.append(MouseUpEvent(x, y, button))

def close_window():
    """Closes the window. Raises an exception if no window is open."""
    global _ctx
    if _ctx._win is None:
        raise EasyGameError('window not open')
    _ctx._win.close()
    _ctx._win = None

def poll_events():
    """Returns a list of events that happened since the last call to this function."""
    global _ctx
    import pyglet
    if _ctx._win is None:
        raise EasyGameError('window not open')
    _ctx._events = []
    _ctx._win.dispatch_events()
    return list(_ctx._events)

def next_frame():
    """Shows the content of the window and waits until it's time for the next frame."""
    global _ctx
    import pyglet
    if _ctx._win is None:
        raise EasyGameError('window not open')
    _ctx._win.flip()
    pyglet.clock.tick()

def fill(r, g, b):
    """Fills the whole window with a single color.
    
    The r, g, b components of the color should be between 0 and 1.
    """
    global _ctx
    import pyglet
    pyglet.gl.glClearColor(r, g, b, 1)
    _ctx._win.clear()

class _Image:
    def __init__(self, img):
        import pyglet
        self._img = img
        self._sprite = pyglet.sprite.Sprite(img)

    @property
    def width(self):
        return self._img.width

    @property
    def height(self):
        return self._img.height

    @property
    def center(self):
        return (self._img.width//2, self._img.height//2)

def load_image(path):
    """Loads an image from the specified path. PNG, JPEG, and many more formats are supported.

    Arguments:
    path -- Path to the image file. (For example 'images/crying_baby.png'.)
    """
    import pyglet
    return _Image(pyglet.resource.image(path))

def load_sheet(path, frame_width, frame_height):
    """Loads an sprite sheet from the specified path and slices it into frames of the specified size.

    Returns the list of images corresponding to the individual slices.

    Arguments:
    path         -- Path to the sprite sheet.
    frame_width  -- Width of a single frame.
    frame_height -- Height of a single frame.
    """
    import pyglet
    img = pyglet.resource.image(path)
    frames = []
    for x in map(lambda i: i * frame_width, range(img.width // frame_width)):
        for y in map(lambda i: i * frame_height, range(img.height // frame_height)):
            frames.append(img.get_region(x, y, frame_width, frame_height))
    return frames

def draw_image(image, position=(0, 0), anchor=None, rotation=0, scale=1):
    """Draws an image to the window.

    Arguments:
    image    -- The image to draw. (Obtained from load_image or load_sheet)
    position -- Anchor's position on the screen. (Defaults to 0, 0.)
    anchor   -- Anchor's position relative to the bottom-left corner of the image. (Defaults to the center.)
    rotation -- Rotation of the image around the anchor in radians. (Defaults to 0.)
    scale    -- Scale of the image around the anchor. (Defaults to 1.)
    """
    import math
    if anchor is None:
        anchor = image.center
    image._img.anchor_x, image._img.anchor_y = anchor
    image._sprite.update(
        x=position[0],
        y=position[1],
        rotation=-rotation/math.pi*180,
        scale=scale,
    )
    image._sprite.draw()
