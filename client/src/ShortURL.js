import React from "react";
// import React, { useState, useEffect } from "react";

export default function ShortURL({ shortenedURL }) {
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
