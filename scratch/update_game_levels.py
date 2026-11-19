import re

new_vocab = '''
  telugu: [
    { emoji: '🐶', variants: [{ native: 'కుక్క', english: 'Dog' }, { native: 'మంచి కుక్క', english: 'Good Dog' }, { native: 'వేగవంతమైన కుక్క', english: 'Fast Dog' }, { native: 'చిన్న కుక్క', english: 'Small Dog' }] },
    { emoji: '🐱', variants: [{ native: 'పిల్లి', english: 'Cat' }, { native: 'అందమైన పిల్లి', english: 'Beautiful Cat' }, { native: 'చిన్న పిల్లి', english: 'Small Cat' }, { native: 'తెల్ల పిల్లి', english: 'White Cat' }] },
    { emoji: '🐘', variants: [{ native: 'ఏనుగు', english: 'Elephant' }, { native: 'పెద్ద ఏనుగు', english: 'Big Elephant' }, { native: 'నల్ల ఏనుగు', english: 'Black Elephant' }] },
    { emoji: '🦁', variants: [{ native: 'సింహం', english: 'Lion' }, { native: 'పెద్ద సింహం', english: 'Big Lion' }, { native: 'క్రూరమైన సింహం', english: 'Fierce Lion' }] },
    { emoji: '🐦', variants: [{ native: 'పిట్ట', english: 'Bird' }, { native: 'అందమైన పిట్ట', english: 'Beautiful Bird' }, { native: 'చిన్న పిట్ట', english: 'Small Bird' }] },
    { emoji: '🐟', variants: [{ native: 'చేప', english: 'Fish' }, { native: 'ఈత కొట్టే చేప', english: 'Swimming Fish' }, { native: 'చిన్న చేప', english: 'Small Fish' }] },
    { emoji: '🐴', variants: [{ native: 'గుర్రం', english: 'Horse' }, { native: 'వేగవంతమైన గుర్రం', english: 'Fast Horse' }, { native: 'తెల్ల గుర్రం', english: 'White Horse' }] },
    { emoji: '🐻', variants: [{ native: 'ఎలుగుబంటి', english: 'Bear' }, { native: 'పెద్ద ఎలుగుబంటి', english: 'Big Bear' }] },
    { emoji: '🐰', variants: [{ native: 'కుందేలు', english: 'Rabbit' }, { native: 'వేగవంతమైన కుందేలు', english: 'Fast Rabbit' }, { native: 'తెల్ల కుందేలు', english: 'White Rabbit' }] },
    { emoji: '🐒', variants: [{ native: 'కోతి', english: 'Monkey' }, { native: 'చిన్న కోతి', english: 'Small Monkey' }] },
    { emoji: '🐮', variants: [{ native: 'ఆవు', english: 'Cow' }, { native: 'మంచి ఆవు', english: 'Gentle Cow' }, { native: 'తెల్ల ఆవు', english: 'White Cow' }] },
    { emoji: '🐐', variants: [{ native: 'మేక', english: 'Goat' }, { native: 'చిన్న మేక', english: 'Small Goat' }] },
    { emoji: '🦌', variants: [{ native: 'జింక', english: 'Deer' }, { native: 'అందమైన జింక', english: 'Beautiful Deer' }] },
    { emoji: '🐅', variants: [{ native: 'పులి', english: 'Tiger' }, { native: 'వేగవంతమైన పులి', english: 'Fast Tiger' }] },
    { emoji: '🦆', variants: [{ native: 'బాతు', english: 'Duck' }, { native: 'తెల్ల బాతు', english: 'White Duck' }] },
    { emoji: '📚', variants: [{ native: 'పుస్తకం', english: 'Book' }, { native: 'మంచి పుస్తకం', english: 'Good Book' }, { native: 'కొత్త పుస్తకం', english: 'New Book' }] },
    { emoji: '🏠', variants: [{ native: 'ఇల్లు', english: 'House' }, { native: 'అందమైన ఇల్లు', english: 'Beautiful House' }, { native: 'పెద్ద ఇల్లు', english: 'Big House' }] },
    { emoji: '🏫', variants: [{ native: 'బడి', english: 'School' }, { native: 'పెద్ద బడి', english: 'Big School' }] },
    { emoji: '🚗', variants: [{ native: 'కారు', english: 'Car' }, { native: 'వేగవంతమైన కారు', english: 'Fast Car' }, { native: 'ఎర్రని కారు', english: 'Red Car' }] },
    { emoji: '🌳', variants: [{ native: 'చెట్టు', english: 'Tree' }, { native: 'పచ్చని చెట్టు', english: 'Green Tree' }, { native: 'పెద్ద చెట్టు', english: 'Big Tree' }] },
    { emoji: '🌺', variants: [{ native: 'పువ్వు', english: 'Flower' }, { native: 'అందమైన పువ్వు', english: 'Beautiful Flower' }, { native: 'ఎర్రని పువ్వు', english: 'Red Flower' }] },
    { emoji: '☀️', variants: [{ native: 'సూర్యుడు', english: 'Sun' }, { native: 'ప్రకాశవంతమైన సూర్యుడు', english: 'Bright Sun' }] },
    { emoji: '🌙', variants: [{ native: 'చంద్రుడు', english: 'Moon' }, { native: 'అందమైన చంద్రుడు', english: 'Beautiful Moon' }] },
    { emoji: '🖊️', variants: [{ native: 'కలం', english: 'Pen' }, { native: 'కొత్త కలం', english: 'New Pen' }] },
    { emoji: '🍎', variants: [{ native: 'యాపిల్', english: 'Apple' }, { native: 'తీపి యాపిల్', english: 'Sweet Apple' }] },
    { emoji: '🍌', variants: [{ native: 'అరటిపండు', english: 'Banana' }, { native: 'తీపి అరటిపండు', english: 'Sweet Banana' }] },
    { emoji: '💧', variants: [{ native: 'నీళ్ళు', english: 'Water' }, { native: 'చల్లని నీళ్ళు', english: 'Cool Water' }, { native: 'మంచి నీళ్ళు', english: 'Clean Water' }] },
    { emoji: '🚆', variants: [{ native: 'రైలు', english: 'Train' }, { native: 'వేగవంతమైన రైలు', english: 'Fast Train' }] },
    { emoji: '💵', variants: [{ native: 'డబ్బులు', english: 'Money' }, { native: 'కొత్త డబ్బులు', english: 'New Money' }] },
    { emoji: '⏰', variants: [{ native: 'గడియారం', english: 'Clock' }, { native: 'గుండ్రని గడియారం', english: 'Round Clock' }] },
    { emoji: '🚲', variants: [{ native: 'సైకిల్', english: 'Bicycle' }, { native: 'చిన్న సైకిల్', english: 'Small Bicycle' }] },
    { emoji: '✈️', variants: [{ native: 'విమానం', english: 'Airplane' }, { native: 'వేగవంతమైన విమానం', english: 'Fast Airplane' }] },
    { emoji: '⚽', variants: [{ native: 'బంతి', english: 'Ball' }, { native: 'గుండ్రని బంతి', english: 'Round Ball' }] },
    { emoji: '⭐', variants: [{ native: 'నక్షత్రం', english: 'Star' }, { native: 'ప్రకాశవంతమైన నక్షత్రం', english: 'Bright Star' }] },
    { emoji: '🌧️', variants: [{ native: 'వర్షం', english: 'Rain' }, { native: 'చల్లని వర్షం', english: 'Cool Rain' }] },
    { emoji: '🌊', variants: [{ native: 'సముద్రం', english: 'Sea' }, { native: 'పెద్ద సముద్రం', english: 'Big Sea' }] },
    { emoji: '⛰️', variants: [{ native: 'కొండ', english: 'Mountain' }, { native: 'ఎత్తైన కొండ', english: 'Tall Mountain' }] }
  ],
  malayalam: [
    { emoji: '🐶', variants: [{ native: 'പട്ടി', english: 'Dog' }, { native: 'നല്ല പട്ടി', english: 'Good Dog' }, { native: 'വേഗമുള്ള പട്ടി', english: 'Fast Dog' }, { native: 'ചെറിയ പട്ടി', english: 'Small Dog' }] },
    { emoji: '🐱', variants: [{ native: 'പൂച്ച', english: 'Cat' }, { native: 'സുന്ദരമായ പൂച്ച', english: 'Beautiful Cat' }, { native: 'ചെറിയ പൂച്ച', english: 'Small Cat' }, { native: 'വെള്ള പൂച്ച', english: 'White Cat' }] },
    { emoji: '🐘', variants: [{ native: 'ആന', english: 'Elephant' }, { native: 'വലിയ ആന', english: 'Big Elephant' }, { native: 'കറുത്ത ആന', english: 'Black Elephant' }] },
    { emoji: '🦁', variants: [{ native: 'സിംഹം', english: 'Lion' }, { native: 'വലിയ സിംഹം', english: 'Big Lion' }, { native: 'ശക്തമായ സിംഹം', english: 'Strong Lion' }] },
    { emoji: '🐦', variants: [{ native: 'കിളി', english: 'Bird' }, { native: 'സുന്ദരമായ കിളി', english: 'Beautiful Bird' }, { native: 'ചെറിയ കിളി', english: 'Small Bird' }] },
    { emoji: '🐟', variants: [{ native: 'മീൻ', english: 'Fish' }, { native: 'നീന്തുന്ന മീൻ', english: 'Swimming Fish' }, { native: 'ചെറിയ മീൻ', english: 'Small Fish' }] },
    { emoji: '🐴', variants: [{ native: 'കുതിര', english: 'Horse' }, { native: 'വേഗമുള്ള കുതിര', english: 'Fast Horse' }, { native: 'വെള്ള കുതിര', english: 'White Horse' }] },
    { emoji: '🐻', variants: [{ native: 'കരടി', english: 'Bear' }, { native: 'വലിയ കരടി', english: 'Big Bear' }] },
    { emoji: '🐰', variants: [{ native: 'മുയൽ', english: 'Rabbit' }, { native: 'വേഗമുള്ള മുയൽ', english: 'Fast Rabbit' }, { native: 'വെള്ള മുയൽ', english: 'White Rabbit' }] },
    { emoji: '🐒', variants: [{ native: 'കുരങ്ങ്', english: 'Monkey' }, { native: 'ചെറിയ കുരങ്ങ്', english: 'Small Monkey' }] },
    { emoji: '🐮', variants: [{ native: 'പശു', english: 'Cow' }, { native: 'നല്ല പശു', english: 'Gentle Cow' }, { native: 'വെള്ള പശു', english: 'White Cow' }] },
    { emoji: '🐐', variants: [{ native: 'ആട്', english: 'Goat' }, { native: 'ചെറിയ ആട്', english: 'Small Goat' }] },
    { emoji: '🦌', variants: [{ native: 'മാൻ', english: 'Deer' }, { native: 'സുന്ദരമായ മാൻ', english: 'Beautiful Deer' }] },
    { emoji: '🐅', variants: [{ native: 'പുലി', english: 'Tiger' }, { native: 'വേഗമുള്ള പുലി', english: 'Fast Tiger' }] },
    { emoji: '🦆', variants: [{ native: 'താറാവ്', english: 'Duck' }, { native: 'വെള്ള താറാവ്', english: 'White Duck' }] },
    { emoji: '📚', variants: [{ native: 'പുസ്തകം', english: 'Book' }, { native: 'നല്ല പുസ്തകം', english: 'Good Book' }, { native: 'പുതിയ പുസ്തകം', english: 'New Book' }] },
    { emoji: '🏠', variants: [{ native: 'വീട്', english: 'House' }, { native: 'സുന്ദരമായ വീട്', english: 'Beautiful House' }, { native: 'വലിയ വീട്', english: 'Big House' }] },
    { emoji: '🏫', variants: [{ native: 'സ്കൂൾ', english: 'School' }, { native: 'വലിയ സ്കൂൾ', english: 'Big School' }] },
    { emoji: '🚗', variants: [{ native: 'കാർ', english: 'Car' }, { native: 'വേഗമുള്ള കാർ', english: 'Fast Car' }, { native: 'ചുവന്ന കാർ', english: 'Red Car' }] },
    { emoji: '🌳', variants: [{ native: 'മരം', english: 'Tree' }, { native: 'പച്ച മരം', english: 'Green Tree' }, { native: 'വലിയ മരം', english: 'Big Tree' }] },
    { emoji: '🌺', variants: [{ native: 'പൂവ്', english: 'Flower' }, { native: 'സുന്ദരമായ പൂവ്', english: 'Beautiful Flower' }, { native: 'ചുവന്ന പൂവ്', english: 'Red Flower' }] },
    { emoji: '☀️', variants: [{ native: 'സൂര്യൻ', english: 'Sun' }, { native: 'തിളങ്ങുന്ന സൂര്യൻ', english: 'Bright Sun' }] },
    { emoji: '🌙', variants: [{ native: 'ചന്ദ്രൻ', english: 'Moon' }, { native: 'സുന്ദരമായ ചന്ദ്രൻ', english: 'Beautiful Moon' }] },
    { emoji: '🖊️', variants: [{ native: 'പേന', english: 'Pen' }, { native: 'പുതിയ പേന', english: 'New Pen' }] },
    { emoji: '🍎', variants: [{ native: 'ആപ്പിൾ', english: 'Apple' }, { native: 'മധുരമുള്ള ആപ്പിൾ', english: 'Sweet Apple' }] },
    { emoji: '🍌', variants: [{ native: 'പഴം', english: 'Banana' }, { native: 'മധുരമുള്ള പഴം', english: 'Sweet Banana' }] },
    { emoji: '💧', variants: [{ native: 'വെള്ളം', english: 'Water' }, { native: 'തണുത്ത വെള്ളം', english: 'Cool Water' }, { native: 'ശുദ്ധമായ വെള്ളം', english: 'Clean Water' }] },
    { emoji: '🚆', variants: [{ native: 'തീവണ്ടി', english: 'Train' }, { native: 'വേഗമുള്ള തീവണ്ടി', english: 'Fast Train' }] },
    { emoji: '💵', variants: [{ native: 'പണം', english: 'Money' }, { native: 'പുതിയ പണം', english: 'New Money' }] },
    { emoji: '⏰', variants: [{ native: 'ഘടികാരം', english: 'Clock' }, { native: 'വട്ട ഘടികാരം', english: 'Round Clock' }] },
    { emoji: '🚲', variants: [{ native: 'സൈക്കിൾ', english: 'Bicycle' }, { native: 'ചെറിയ സൈക്കിൾ', english: 'Small Bicycle' }] },
    { emoji: '✈️', variants: [{ native: 'വിമാനം', english: 'Airplane' }, { native: 'വേഗമുള്ള വിമാനം', english: 'Fast Airplane' }] },
    { emoji: '⚽', variants: [{ native: 'പന്ത്', english: 'Ball' }, { native: 'വട്ട പന്ത്', english: 'Round Ball' }] },
    { emoji: '⭐', variants: [{ native: 'നക്ഷത്രം', english: 'Star' }, { native: 'തിളങ്ങുന്ന നക്ഷത്രം', english: 'Bright Star' }] },
    { emoji: '🌧️', variants: [{ native: 'മഴ', english: 'Rain' }, { native: 'തണുത്ത മഴ', english: 'Cool Rain' }] },
    { emoji: '🌊', variants: [{ native: 'കടൽ', english: 'Sea' }, { native: 'വലിയ കടൽ', english: 'Big Sea' }] },
    { emoji: '⛰️', variants: [{ native: 'മല', english: 'Mountain' }, { native: 'വലിയ മല', english: 'Big Mountain' }] }
  ]
};
'''

file_path = r"c:\Users\dines\Downloads\Deebak Client\utils\gameLevels.ts"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace aliases VOCAB_ITEMS.telugu = VOCAB_ITEMS.tamil; VOCAB_ITEMS.malayalam = VOCAB_ITEMS.tamil;
# and close VOCAB_ITEMS object properly
old_alias = """// Aliases
VOCAB_ITEMS.telugu = VOCAB_ITEMS.tamil;
VOCAB_ITEMS.malayalam = VOCAB_ITEMS.tamil;"""

if "VOCAB_ITEMS.telugu = VOCAB_ITEMS.tamil;" in content:
    content = content.replace("  ]\n};", "  ]," + new_vocab)
    content = content.replace(old_alias, "// Clean native vocabulary per language")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated utils/gameLevels.ts with native Telugu and Malayalam items!")
