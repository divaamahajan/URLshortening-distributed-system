from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/members")
def members():
    return jsonify({"members":["m1", "m2", "m3"]})

@app.route("/longurl", methods=["POST"])
def shorten_url():
    data = request.json
    long_url = data.get("url")
    # Logic to shorten the URL goes here
    # Assuming you have some logic to generate a shortened URL
    shortened_url = "https://example.com/shortened-url"
    return jsonify({"shortenedUrl": shortened_url})

if __name__=="__main__":
    app.run(debug=True)