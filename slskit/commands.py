import sys

import salt.output
from salt.fileserver import Fileserver

from . import pillar, state
from .opts import Config


def highstate(config: Config):
    highstate = state.show_highstate(config)

    output = {minion_id: result.value for minion_id, result in highstate.items()}
    _display_output(output, config)

    if not all(r.valid for r in highstate.values()):
        sys.exit(1)


def pillars(config: Config):
    result = pillar.items(config)
    _display_output(result, config)

    if any("_errors" in pillar for pillar in result.values()):
        sys.exit(1)


def refresh(config: Config):
    Fileserver(config.opts).update()


def _display_output(output: dict, config: Config):
    salt.output.display_output(output, out="yaml", opts=config.opts)
