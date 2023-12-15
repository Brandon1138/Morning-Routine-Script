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
try:
    os.startfile("ms-todo:")
except Exception as e:
    print(f"Failed to open Microsoft To Do: {e}")
# Launch Outlook
try:
    os.startfile("outlookcal:")
except Exception as e:
    print(f"Failed to open Outlook: {e}")
# Launch Spotify
try:
    os.startfile("spotify:")
except Exception as e:
    print(f"Failed to open Spotify: {e}")
