import json
import security_layer as security_layer

# import requests


def lambda_handler(event, context):

    respjson = { 
        "layer": security_layer.getLogonInfo(), 
        "message": "public page"
    } 

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
            "Access-Control-Allow-Origin": "https://diq3qr0d5ppph.cloudfront.net",
            "Content-Type": "application/json"
            },        
        "body": json.dumps(respjson)
    }
