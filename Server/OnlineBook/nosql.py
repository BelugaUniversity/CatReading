import redis

r = redis.Redis(host="120.77.38.20", port="6379")
r.set('age', '10')
print(r.get('age'))

