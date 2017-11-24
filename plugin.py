import supybot.conf as conf
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('OpsPing')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


class OpsPing(callbacks.Plugin):
    """Plugin for ops pinging message per channel"""

    def ops(self, irc, msg, args, text):
        """takes a string to ping ops with

        Pings all ops in the current channel.
        """
        channel = msg.args[0]
        opslist = self.registryValue('opslist', channel)
        if not opslist:
            irc.error('no list of ops to ping configured for this channel.')
            return

        message = ', '.join(opslist)
        if text:
            message = '{} - {}'.format(message, text)
        irc.reply(message, prefixNick=False)
    ops = wrap(ops, [optional('text')])


Class = OpsPing


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
