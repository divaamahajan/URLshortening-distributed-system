from flask import Flask, request, jsonify
import random

app = Flask(__name__)
MAX_LEN = 7

@app.route("/longurl", methods=["POST"])
def shorten_url():
    data = request.json
    long_url = data.get("url")
    shortened_url = getshorturl()
    # shortened_url = "https://example.com/shortened-url"
    shortened_url = "https://"+get_current_host()+"/"+shortened_url
    return jsonify({"shortenedUrl": shortened_url})

def getshorturl():        
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    short_url = "".join(random.choice(chars) for _ in range(MAX_LEN))
    return short_url
    
def get_current_host():
    try:
        host = request.host
        # port = request.environ.get('SERVER_PORT')
        # return f"{host}:{port}"
        return f"{host}"
    except Exception as e:
        print("Error:", e)
        return None
    

if __name__=="__main__":
    max_s = 62**7 - 1
    print("Maximum value of s:", max_s)

    app.run(debug=True)
