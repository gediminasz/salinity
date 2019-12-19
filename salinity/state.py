import salt.output
import salt.state

import salinity.pillar
from salinity.opts import build_opts


def show_highstate(args):
    opts = build_opts(args)

    result = {
        minion_id: compile_highstate({**opts, "id": minion_id})
        for minion_id in args.minion_id
    }

    salt.output.display_output(result, out="yaml", opts=opts)


def compile_highstate(opts):
    return salt.state.HighState(opts).compile_highstate()
