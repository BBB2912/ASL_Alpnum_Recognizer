from wordPromoter import Trie  # Import the trie instance

def get_suggestions(input_prefix, context):
    return [word for word, rank in Trie.suggest(input_prefix, context)]

if __name__ == "__main__":
    # Example usage
    input_prefix = "a"
    context = "I am learning about"
    print(get_suggestions(input_prefix,context))