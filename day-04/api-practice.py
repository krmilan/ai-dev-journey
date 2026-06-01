import requests
import json

# Hit a free public API — no key needed
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# Every API response has a status code
print(f"Status code: {response.status_code}")  # 200 = success

# The actual data
data = response.json()  # automatically parses JSON for you
print(f"\nPost title: {data['title']}")
print(f"Post body: {data['body'][:100]}...")  # first 100 chars

# Now fetch multiple posts
response2 = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = response2.json()

print(f"\nTotal posts fetched: {len(posts)}")
print("\nFirst 3 post titles:")
for post in posts[:3]:
    print(f"  - {post['title']}")