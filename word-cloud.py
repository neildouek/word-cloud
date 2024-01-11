from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Initial list of words related to platform engineering
words = [
    # Original list of words...
]

# Additional keywords from Humaintec
additional_words = [
    # Additional list of words...
]

# New words to include
new_words = ["Sustainability", "Scalability", "DevSecOps", "Cloud Native", "Gen AI"]

# Combining all lists and ensuring no duplicates
combined_words = list(set(words + additional_words + new_words))

# Adding extra emphasis on "Platform" and "Engineering"
enhanced_words = combined_words + ["Platform"] * 10 + ["Engineering"] * 10

# Create a word cloud with the enhanced list
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(" ".join(enhanced_words))

# Display the word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
