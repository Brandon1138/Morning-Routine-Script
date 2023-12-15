import webbrowser
import os

# URLs to open in Microsoft Edge
urls = [
    "https://chat.openai.com/",   # ChatGPT
    "https://www.daily.dev/",           # Daily.dev
    "https://www.leetcode.com/",        # LeetCode
    "https://www.github.com/",          # GitHub
]

# Open URLs in Microsoft Edge
for url in urls:
    webbrowser.open_new_tab(url)

# Launch Microsoft To Do
os.startfile("ms-todo:")
# Launch Outlook
os.startfile("outlookcal:")
# Launch Spotify
os.startfile("spotify:")

