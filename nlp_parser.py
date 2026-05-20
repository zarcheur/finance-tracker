import spacy

nlp = spacy.load('en_core_web_sm')

INCOME_VERBS = ["receive", "get", "earn", "gain", "collect"]
EXPENSE_VERBS = ["spend", "pay", "buy", "purchase", "use"]

CATEGORIES = {
    "allowance": ["parent", "mom", "dad", "family", "allowance"],
    "food": ["food", "lunch", "dinner", "breakfast", "snack", "drink", "cafe", "restaurant"],
    "transport": ["fare", "jeep", "bus", "grab", "tric", "tricycle", "train", "lrt", "transport", "ride"],
    "shopping": ["bought", "shop", "mall", "store", "online"],
    "bills": ["bill", "electric", "water", "wifi", "internet", "rent"],
}

def extract_amount(doc):
    for token in doc:
        if token.pos_ == "NUM":
            try:
                return float(token.text)
            except ValueError:
                continue
    return None

def extract_type(doc):
    for token in doc:
        if token.lemma_ in INCOME_VERBS:
            return "income"
        elif token.lemma_ in EXPENSE_VERBS:
            return "expense"
    return "unknown"

def extract_category(doc):
    for token in doc:
        for category, keywords in CATEGORIES.items():
            if token.lemma_ in keywords:
                return category
    return "general"


def parse_expense(text):
    doc = nlp(text)

    amount = extract_amount(doc)
    transaction_type = extract_type(doc)
    category = extract_category(doc)

    return {
        "amount": amount,
        "type": transaction_type,
        "category": category,
        "description": text
    }


if __name__ == "__main__":
    test = "I paid 25 pesos to parents"
    result = parse_expense(test)
    print(result)