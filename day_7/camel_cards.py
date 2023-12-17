# Rank order the cards based on their strength

    # Rules: (Strength)
        # ^  Five of a kind - AAAAA - All matching TYPE
        # |  Four of a kind - AAJAA - 4 matching TYPE
        # |  Full house     - AAA22 - 3 matching TYPE 2 matching TYPES
        # |  Thre of a Kind - AAA23 - 3 matching TYPE 2 non matching TYPES
        # |  Two Pair       - AA223 - 2 matching TYPE 2 matching TYPES 1 non match
        # |  One Pair       - AA234 - 1 matching >TYPE 3 non matching TYPE
        # V  High Card      - A2345 - None matching TYPE

    # < A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2 >
    # Second Ordering: 
        # IF TYPE match:
            # Compare n... cards
                # Highest initial card wins
                # e.g Five of a kind #1 -> AAAAA
                    # beats Five of a kind #2 -> KKKKK


with open('input.txt', 'r') as file_input:
    camel_cards = file_input.read()

# camel_card_mapping = {
#     'A' : 13,
#     'K' : 12,
#     'Q' : 11,
#     'J' : 10,
#     'T' : 9,
#     '9' : 8,
#     '8' : 7,
#     '7' : 6,
#     '6' : 5,
#     '5' : 4,
#     '4' : 3,
#     '3' : 2,
#     '2' : 1
#  }

# for card in camel_cards:
#     for type in card[:5]:
#         print(type)