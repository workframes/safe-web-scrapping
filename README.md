# safe-web-scrapping

**NOTE: This module uses free proxies(https://www.sslproxies.org/), So your should use your own proxy using the param own_proxy**
**This module allows your scrap any website safely using proxies**

Example:
```py
# Example
import proxy_handler

proxy = proxy_handler.get_proxy()
request = proxy.proxy_request(url="https://www.roblox.com/home", request_type="get")
print(request)
```
