from .en import Lang as LBase

class Lang(LBase):
    """ Thanks @luckydonald """
    lang = "de"
    start_message = "Dieser Bot zeigt dir das Sprachkennzeichen das dein Telegram an Bots sendet."
    part_of_luckydonaldsbots = "Teil des @luckydonaldsbots Netzwerkes."
    help_message = start_message + "\n\n" + part_of_luckydonaldsbots
    lang_response = "Dein Sprachkennzeichen ist '{lang}'."
# end class
