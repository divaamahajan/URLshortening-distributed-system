import React, { useState } from "react";

export default function InputURL({ onShortenedURLReceived }) {
  const [longUrl, setLongUrl] = useState("");
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setLongUrl(e.target.value);
  };

  const handleSubmit = async () => {
    try {
      if (!isValidUrl(longUrl)) {
        onShortenedURLReceived("");
        throw new Error("Invalid URL");
      } else {
        setError(""); // Clear any previous error message
      }
      console.log("going to post", longUrl);
      // Logic to send the URL
      const response = await fetch("/longurl", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          long_url: longUrl,
        }),
      });

      console.log("I got response", response);
      if (!response.ok) {
        throw new Error("Failed to fetch data");
      }
      setError("");
      setLongUrl("")
      const data = await response.json();
      console.log("InputURL", data.shortenedUrl);
      onShortenedURLReceived(data.shortenedUrl); // Pass the shortened URL to the parent component
    } catch (err) {
      setError(err.message);
    }
  };

  const isValidUrl = (str) => {
    try {
      new URL(str);
      return true;
    } catch (err) {
      return false;
    }
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Enter URL"
        value={longUrl}
        onChange={handleChange}
      />
      <button onClick={handleSubmit}>Shorten</button>
      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
}
