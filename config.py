import supybot.conf as conf
import supybot.registry as registry
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('OpsPing')
except:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified themself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('OpsPing', True)


OpsPing = conf.registerPlugin('OpsPing')
conf.registerChannelValue(OpsPing, 'opslist',
    registry.SpaceSeparatedListOfStrings('', """Contains the list of ops in the
                                                current channel"""))

# This is where your configuration variables (if any) should go.  For example:
# conf.registerGlobalValue(OpsPing, 'someConfigVariableName',
#     registry.Boolean(False, _("""Help for someConfigVariableName.""")))


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
