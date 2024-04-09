""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.
'''

'''
# eng
_pad        = '_'
_punctuation = ';:,.!?¡¿—…"«»“” '
_letters = 'ྦཨའྟཟྕརཞདྫནླྡམཚཤཀྭཕྷཎངཐཝཊཧཱལུྨཆེྩོཛཁཉཌྙིབྗཏྱྐྥྤཙྣཅྒྲགྔསཡཇཔ'
_letters_ipa = "ɑɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼʴʰʱʲʷˠˤ˞↓↑→↗↘'̩'ᵻ"
'''

# tibetan_cleaners
_pad        = '_'
# _punctuation = ',.!?-~…'
_punctuation = ';:,.!?¡¿—…"«»“” '
_letters = 'AEINOQUabcdefghijklmnoprstuvwxyzʃʧ↓↑ '

# tibetan_cleaners2-phone
_pad        = '_'
# _punctuation = ',.!?-~…'
_punctuation = ';:,.!?¡¿—…"«»“” '
_letters = 'AEINOQUabcdefghijklmnopqrstuvwxyzʃʧ↓↑ '


# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters)

'''
# Export all symbols-old:
symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa)
'''

# Special symbol ids
SPACE_ID = symbols.index(" ")
