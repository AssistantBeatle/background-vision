
class commands:
    mswordActivator = False
    browserActivator = False
    systemcommandsActivator = False
    systemcommands = [['open','msword'],['open','chrome'],['exit'],
    ['start','mousehover'],['stop','mousehover']]

    mswordcommands = [['save'],['select','all'],['write'],['read'],['bold'],
    ['italic'],['underline'],['centre','text'],['open','file'],
    ['copy'],['paste'],['close','exit','quit'],['decrease','font','size'],
    ['cut','text'],['deselect'],['remove','bold'],['remove','italic'],
    ['remove','underline'],['increase','font','size'],['type'],['undo'],['redo'],
    ['left','align','text'],['right','align','text'],['create','new','document'],
    ['split','document','window'],['remove','split','document','window'],
    ['print','document'],['double','underline'],['remove','double','underline'],
    ['apply','subscript'],['remove','subscript'],['apply','superscript'],
    ['remove','superscript'],['one','character','right'],['one','character','left'],
    ['one','word','left'],['one','word','right'],['one','paragraph','up'],
    ['one','paragraph','down'],['one','line','up'],['one','line','down'],
    ['go','to','end','of','line'],['go','to','beginning','of','line'],
    ['go','to','end','of','document'],['go','to','beginning','of','document'],
    ['delete','one','left','character'],['delete','one','right','character'],
    ['delete','one','left','word'],['delete','one','right','word'],
    ['close','msword'],['new','line'],['caps','lock']]

    browsercommands = [['write'],['open','new','window'],['open','new','incognito','window'],
    ['open','new','tab'],['reopen','last','closed','tab'],['jump','to','next','open','tab'],
    ['jump','to','previous','open','tab'],['minimize','current','window'],['close','current','window'],
    ['close','current','tab'],['quit','chrome'],['stop','loading','page'],['print','current','page'],
    ['save','current','page'],['reload','current','page'],['everything','on','page','bigger'],
    ['everything','on','page','smaller'],['everything','on','page','of','default','size'],
    ['delete','previous','word'],['go','to','top','of','page'],['go','to','end','of','page'],
    ['open','chrome','menu'],['open','find','bar'],['jump','to','next','match','of','find','bar','search'],
    ['jump','to','previous','match','of','find','bar','search'],['clear','browsing','data','option']]

    @staticmethod
    def activatesystemcommandset():
        commands.mswordActivator = False
        commands.browserActivator = False
        commands.systemcommandsActivator = True

    @staticmethod
    def activatemswordcommandset():
        commands.activatesystemcommandset()
        commands.systemcommandsActivator = False
        commands.mswordActivator = True

    @staticmethod
    def activatebrowsercommandset():
        commands.activatesystemcommandset()
        commands.systemcommandsActivator = False
        commands.browserActivator = True

    @staticmethod
    def givecommands():
        if commands.mswordActivator is True:
            return commands.mswordcommands
        elif commands.systemcommandsActivator is True:
            return commands.systemcommands
        elif commands.browserActivator is True:
            return commands.browsercommands
