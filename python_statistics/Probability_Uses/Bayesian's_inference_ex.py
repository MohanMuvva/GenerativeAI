# Total number of cards in a standard deck
total_cards = 52

# Number of black kings in the deck
black_kings = 2  # King of Spades and King of Clubs

# Total number of black cards in the deck
black_cards = 26  # 13 Spades + 13 Clubs

# Prior probability of picking a black king
P_BK = black_kings / total_cards

# Likelihood of picking a black card given that it is a black king
P_BC_given_BK = 1  # If it's a black king, it's definitely a black card

# Total probability of picking a black card
P_BC = black_cards / total_cards

# Applying Bayes' theorem
P_BK_given_BC = (P_BC_given_BK * P_BK) / P_BC

# Print the result
print(f"The probability of picking a black king given that a black card was picked is: {P_BK_given_BC:.2f}")
