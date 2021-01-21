import json
from flask import request, _request_ctx_stack
from functools import wraps
from jose import jwt
from urllib.request import urlopen


# https://alsahmou.us.auth0.com/authorize?audience=coffee&response_type=token&client_id=qR6a8wUOJcesYoP2KcbBqF3yZ8e2edd2&redirect_uri=https://127.0.0.1:8100/login-results
# live results https://127.0.0.1:8100/login-results#access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlRySFZvdDM4X2hGeEQ4dzlTQkx0SSJ9.eyJpc3MiOiJodHRwczovL2Fsc2FobW91LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA5YTI0OTUxODUzYjAwNmEwMGE0MzkiLCJhdWQiOiJjb2ZmZWUiLCJpYXQiOjE2MTEyNDQxMTAsImV4cCI6MTYxMTI1MTMxMCwiYXpwIjoicVI2YTh3VU9KY2VzWW9QMktjYkJxRjN5WjhlMmVkZDIiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbXX0.xdD6o4tammcgMao5AYTpr8Vcd8UE9_VkSY0G4ma7E3qvaCw5CMTqeO1AJNgfm4_Xo-VGEaSwl_XMIcN55PrS24i2zEH9vzAjmpf-EPLQ4iE5cRFTrKMsTUNHMXs8XaduRSuy2nwOKtC1nGaOWV3RXH4kNTyMm8_0qkqiM_2lStZOntPKaxeq1GHtAdr1yKYuEERwNpaoD09Gja1hVlKTbGhy-Wql03e9p0uDx3pd7KeibloujAiLv7EOkzL400qz1AT0ukSBSUEGHGJlVshY4kL1OL2yGjlkZe0DBCSrJivIjFzEjwyYxFvhmukkJrtUoc0ogrmCSb5Cnehgh0O5JA&expires_in=7200&token_type=Bearer
# gmail results https://127.0.0.1:8100/login-results#access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlRySFZvdDM4X2hGeEQ4dzlTQkx0SSJ9.eyJpc3MiOiJodHRwczovL2Fsc2FobW91LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA5YTM4YTQ0MWZkNjAwNzA4MWJiZDgiLCJhdWQiOiJjb2ZmZWUiLCJpYXQiOjE2MTEyNDQ0MjksImV4cCI6MTYxMTI1MTYyOSwiYXpwIjoicVI2YTh3VU9KY2VzWW9QMktjYkJxRjN5WjhlMmVkZDIiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbXX0.f0Ngp5RFcctNFv3jyWgkR0RDK3JUg9D7ENjQhbvYmi3_dF8KzynIq1YDYCMREzQLDwITn568QZLSVIcReY3QpF5DJ-O5HdbNKNlG7U3E_XZwH2CkS88vglnecHE3LsBWxC7iCZHgF3eSJYBURxF-ParC1vOYMlI4NZFZRnP83MjhSU3xdXuWHhAuUp-8WUFYkh-mG61TexYHHOHjBtwackYUncB-iFpmjmOhNQa9cArKMT1JIkQ9xOFvGxRmqxXRtVYccNUqTYQDcS2ox4kkYfTEnxO1jQkErQ-gJczBX2pzn-PujWa6bueJjN1r7XecOSngI25Wf4gV7Mqnfxvnew&expires_in=7200&token_type=Bearer


AUTH0_DOMAIN = 'udacity-fsnd.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'dev'

## AuthError Exception
'''
AuthError Exception
A standardized way to communicate auth failure modes
'''
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


## Auth Header

'''
@TODO implement get_token_auth_header() method
    it should attempt to get the header from the request
        it should raise an AuthError if no header is present
    it should attempt to split bearer and the token
        it should raise an AuthError if the header is malformed
    return the token part of the header
'''
def get_token_auth_header():
   raise Exception('Not Implemented')

'''
@TODO implement check_permissions(permission, payload) method
    @INPUTS
        permission: string permission (i.e. 'post:drink')
        payload: decoded jwt payload

    it should raise an AuthError if permissions are not included in the payload
        !!NOTE check your RBAC settings in Auth0
    it should raise an AuthError if the requested permission string is not in the payload permissions array
    return true otherwise
'''
def check_permissions(permission, payload):
    raise Exception('Not Implemented')

'''
@TODO implement verify_decode_jwt(token) method
    @INPUTS
        token: a json web token (string)

    it should be an Auth0 token with key id (kid)
    it should verify the token using Auth0 /.well-known/jwks.json
    it should decode the payload from the token
    it should validate the claims
    return the decoded payload

    !!NOTE urlopen has a common certificate error described here: https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org
'''
def verify_decode_jwt(token):
    raise Exception('Not Implemented')

'''
@TODO implement @requires_auth(permission) decorator method
    @INPUTS
        permission: string permission (i.e. 'post:drink')

    it should use the get_token_auth_header method to get the token
    it should use the verify_decode_jwt method to decode the jwt
    it should use the check_permissions method validate claims and check the requested permission
    return the decorator which passes the decoded payload to the decorated method
'''
def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper
    return requires_auth_decorator