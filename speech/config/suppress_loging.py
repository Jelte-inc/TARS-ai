import os
import sys
from ctypes import cdll, CFUNCTYPE, c_char_p, c_int, c_void_p

# Keep a global reference so it isn't GC'd.
_ALSA_HANDLER = None

def suppress_alsa_errors():
    """Install a no-op ALSA error handler to silence libasound messages on Linux."""
    if not sys.platform.startswith('linux'):
        return

    # Optional: this only hides the pygame support prompt; harmless to keep.
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

    # Signature matches the fixed part of snd_lib_error_handler_t (varargs ignored).
    ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

    def _py_error_handler(filename, line, function, err, fmt):
        # Intentionally do nothing.
        return

    # Create the callback and keep it alive globally.
    global _ALSA_HANDLER
    _ALSA_HANDLER = ERROR_HANDLER_FUNC(_py_error_handler)

    try:
        asound = cdll.LoadLibrary('libasound.so.2')

        # Declare prototype explicitly to avoid default int conversions.
        asound.snd_lib_error_set_handler.argtypes = [ERROR_HANDLER_FUNC]
        # Function returns previous handler pointer; we don't use it.
        asound.snd_lib_error_set_handler.restype = c_void_p

        # Install our handler.
        asound.snd_lib_error_set_handler(_ALSA_HANDLER)
    except OSError:
        # libasound not present; nothing to suppress.
        pass
