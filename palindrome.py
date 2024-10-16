
from collections import deque

def main():
    test_string("Test string this is") # expected to be False
    test_string("qwertytrewq") # expected to be True
    test_string("abccba") # expected to be True
    test_string("a") # expected to be True, it's still a palindrome
    test_string("a b c") # expected to be false
    test_string("   ") # expected to be false


def test_string(text: str):
    print(f"Testing string \'{text}\'")
    print("Is this string a palindrome: ", is_palindrome(text), "\n")


def is_palindrome(text: str):
    cleared_text = prepare_text(text)
    if len(cleared_text) == 0:
        # we cannot consider empty string as palindrome
        return False

    text_deque = deque(cleared_text)

    # note condition here, this way we automatically handle case 
    # when text has odd length, we just consided that last symbol (originally center symbol of text)
    # is equal to itself
    while len(text_deque) > 1:
        start = text_deque.popleft()
        end = text_deque.pop()

        if (start != end):
            # this can't be palindrome
            return False
        
        # otherwize let's check next symbols from both sides

    # so if we here - it means all symbols from both sides were the same
    return True


# convert to lowercase + get rid of spaces
def prepare_text(text: str):
    return text.lower().replace(" ", "")


if __name__ == "__main__":
    main()