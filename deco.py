from functools import wraps
from flask import request, jsonify

from backend_app.models.access_code_models import AccessCode
# from 
import jwt
from config import Config

# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, Config.SECRET_KEY, audience="portal.radioschoolng.org", algorithms=["HS256"])

            current_user = AccessCode.query.filter_by(access_code = data['access_code']).first()
            print(data)
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401

        # returns the current logged in users contex to the routes
        return f(current_user.id, *args, **kwargs)
  
    return decorated