from pymemcache.client.base import Client

# Replace 'memcached' with the hostname or IP address of your Memcached container
memcache_host = "memcachedcontainer"
memcache_port = 11211

# Create a client to connect to Memcached
cached_obj = Client((memcache_host, memcache_port))

# print("cached_obj", cached_obj)
# # Set a key-value pair in Memcached
# cached_obj.set('my_key', 'my_value')

# print("keys set")
# # Get the value for a key from Memcached
# value = cached_obj.get('my_key')
# print("my_value:" , value)  # Output: b'my_value'