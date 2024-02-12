import React, { useState } from "react";
import "./App.css";
import InputURL from "./InputURL";
import ShortURL from "./ShortURL";
import Ping from "./Ping";

function App() {
  const [shortenedURL, setShortenedURL] = useState(""); // State to hold the shortened URL

  // Function to update the shortened URL state
  const handleShortenedURLReceived = (url) => {
    console.log("App", url);
    setShortenedURL(url);
  };

  return (
    <div className="container">
      <div className="status-container">
        <Ping />
      </div>
      <div className="content-container">
        <h1>URL Shortener</h1>
        <InputURL onShortenedURLReceived={handleShortenedURLReceived} />
        <ShortURL shortenedURL={shortenedURL} />
      </div>
    </div>
  );
}

export default App;
