import React from "react";
// import React, { useState, useEffect } from "react";

export default function ShortURL({ shortenedURL }) {
  // useEffect(() => {
  //   // Assuming `longURL` is a state variable
  //   const url = `/shortURL/${longURL}`;

  //   fetch(url)
  //     .then((res) => res.json())
  //     .then((shortenedUrl) => {
  //       setShortenedUrl(shortenedUrl);
  //     })
  //     .catch((error) => {
  //       console.error("Error fetching data:", error);
  //       // Handle error (e.g., set a state variable to display an error message)
  //     });
  // }, [longURL]); // Add `longURL` as a dependency to useEffect

  return (
    <div>
      {shortenedURL && (
        <div>
          <p>Shortened URL:</p>
          <a href={shortenedURL} target="_blank" rel="noopener noreferrer">
            {shortenedURL}
          </a>
        </div>
      )}
    </div>
  );
}
