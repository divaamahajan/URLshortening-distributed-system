import React, { useState } from "react";

function Ping() {
  const [serviceStatus, setServiceStatus] = useState("");
  const [showStatus, setShowStatus] = useState(false);

  const checkServiceStatus = async () => {
    try {
      const response = await fetch("/", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (response.ok) {
        setServiceStatus("Service is up");
      } else {
        setServiceStatus("Service is down");
      }
    } catch (error) {
      console.error("Error occurred while checking service status:", error);
      setServiceStatus("Service is down");
    }
    setShowStatus(true);
  };

  return (
    <div>
      <h4>Service Status:</h4>
      {showStatus && <p>{serviceStatus}</p>}
      <button className="button" onClick={checkServiceStatus}>
        Check Status
      </button>
    </div>
  );
}

export default Ping;
