from rest_framework.throttling import UserRateThrottle
class AliRateThrottle(UserRateThrottle):
    scope = 'ali'