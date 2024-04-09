import re



# get transfer
def process(text):
    # read lexicon
    wrd_to_phn = {}
    with open("/home1/cdl/vits-main/text/phonedic.txt", "r", encoding='utf-8') as lf:
        for line in lf:
            items = line.rstrip().split(" ")
            assert len(items) > 1, line
            assert items[0] not in wrd_to_phn, items
            wrd_to_phn[items[0]] = items[1:]
    # transform
    # phones_texts = {}

    items = text.strip().split()
    # words = []
    phones = []
    for w in items:
        if not (w in wrd_to_phn):
            continue
        else:
            # words.append(w)
            phones.extend(wrd_to_phn[w])

    str = " "
    text = str.join(phones)
    return text






def tibetan_to_ipa(text):
    text = re.sub(r'[、；：]', '，', text)
    text = re.sub(r'\s*，\s*', ', ', text)
    text = re.sub(r'\s*。\s*', '. ', text)
    text = re.sub(r'\s*？\s*', '? ', text)
    text = re.sub(r'\s*！\s*', '! ', text)
    text = re.sub(r'\s*$', '', text)
    # new
    text = re.sub(r'\s*-\s*', '', text)
    text = re.sub(r'\s*།\s*', '. ', text)
    text = re.sub(r'\s*  \s*', ' ', text)
    text = re.sub(r'\s*་\s*', ' ', text)
    text = process(text)
    text = re.sub(r'\s*  \s*', ' ', text)
    return text