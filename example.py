# Example
import proxy_handler

proxy = proxy_handler.get_proxy()
request = proxy.proxy_request(url="https://www.roblox.com/home", request_type="get")
print(request)
