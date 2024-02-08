import "./App.css";
import React, { useState } from "react";
import InputURL from "./InputURL";
import ShortURL from "./ShortURL";

function App() {
  const [shortenedURL, setShortenedURL] = useState(""); // State to hold the shortened URL

  // Function to update the shortened URL state
  const handleShortenedURLReceived = (url) => {
    console.log("App", url);
    setShortenedURL(url);
  };

  return (
    <>
      <h1>URL Shortener</h1>
      <InputURL onShortenedURLReceived={handleShortenedURLReceived} />{" "}
      {/* Pass a callback to handle shortened URL */}
      <ShortURL shortenedURL={shortenedURL} />{" "}
      {/* Pass the long URL and shortened URL as props */}
    </>
  );
}

export default App;
