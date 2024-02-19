import React, { useState, useEffect } from 'react';

export const Timer = ({ timePerPhoto }) => {
  const [initialTime, setInitialTime] = useState(timePerPhoto);
  const [timeRemaining, setTimeRemaining] = useState(timePerPhoto);

  useEffect(() => {
    if (timeRemaining > 0) {
      const interval = setInterval(() => {
        setTimeRemaining((prevTime) => prevTime - 1);
      }, 1000);

      return () => clearInterval(interval);
    } else {
      // Reset timer when time reaches 0
      setTimeRemaining(initialTime);
    }
  }, [timeRemaining, initialTime]);

  const formatTime = (seconds) => {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    return `${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`;
  };

  return (
    <div>
      <h4 style={{position:'absolute', right: "20px", top: "10px"}}>{formatTime(timeRemaining)}</h4>
    </div>
  );
};
