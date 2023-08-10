from fake_useragent import UserAgent

ua = UserAgent()
# Get a random browser user-agent string
print(ua.random)
print(ua.chrome)
print("=" * 30)
for u in range(10):
    print(ua.random)
