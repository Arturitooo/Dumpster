import React, { useState, useEffect, useCallback } from 'react';

const predefinedTimes = [
  { label: '0.5 min', value: 0.5 },
  { label: '1 min', value: 1 },
  { label: '2 min', value: 2 },
  { label: '5 min', value: 5 },
  { label: '10 min', value: 10 },
];

const RandomPhoto = ({ photos }) => {
  const [shownPhotos, setShownPhotos] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(null);
  const [secondsPerPhoto, setSecondsPerPhoto] = useState('');
  const [defaultSecondsPerPhoto, setDefaultSecondsPerPhoto] = useState('');
  const [formSubmitted, setFormSubmitted] = useState(false);
  const [timeLeft, setTimeLeft] = useState(null);
  const [previousIndices, setPreviousIndices] = useState([]);
  const [isRunning, setIsRunning] = useState(true); // Default to true
  const [customTime, setCustomTime] = useState('');

  useEffect(() => {
    setDefaultSecondsPerPhoto(secondsPerPhoto);
  }, [secondsPerPhoto]);

  useEffect(() => {
    let intervalId;
    if (secondsPerPhoto !== '' && formSubmitted && isRunning) {
      intervalId = setInterval(() => {
        let nextIndex;
        do {
          nextIndex = Math.floor(Math.random() * photos.length);
        } while (shownPhotos.includes(nextIndex));
  
        const updatedShownPhotos = [...shownPhotos, nextIndex].slice(-3);
        setShownPhotos(updatedShownPhotos);
        setCurrentIndex(nextIndex);
        setTimeLeft(parseFloat(secondsPerPhoto) * 60); // Convert minutes to seconds
      }, parseFloat(secondsPerPhoto) * 60 * 1000); // Convert minutes to milliseconds
    }

    return () => clearInterval(intervalId);
  }, [photos, shownPhotos, secondsPerPhoto, formSubmitted, isRunning]); // Update dependency array

  useEffect(() => {
    if (photos.length > 1 && currentIndex === null) {
      const randomIndex = Math.floor(Math.random() * photos.length);
      setCurrentIndex(randomIndex);
      setPreviousIndices([randomIndex]);
    }
  }, [currentIndex, photos]);

  const handleNext = useCallback(() => {
    let nextIndex;
    do {
      nextIndex = Math.floor(Math.random() * photos.length);
    } while (previousIndices.includes(nextIndex));
    setCurrentIndex(nextIndex);
    setPreviousIndices(prevIndices => [...prevIndices, nextIndex]);
    setTimeLeft(parseFloat(secondsPerPhoto) * 60); // Reset the timer to default
  }, [photos, previousIndices, secondsPerPhoto]);

  useEffect(() => {
    if (timeLeft !== null && isRunning) {
      const timerId = setInterval(() => {
        setTimeLeft(prevTimeLeft => {
          if (prevTimeLeft === 0) {
            handleNext(); // Show next photo when timer reaches 0:00
            return parseFloat(secondsPerPhoto) * 60;
          } else {
            return prevTimeLeft - 1;
          }
        });
      }, 1000);

      return () => clearInterval(timerId);
    }
  }, [timeLeft, isRunning, handleNext, secondsPerPhoto]);


  const handlePrevious = useCallback(() => {
    if (previousIndices.length > 1) {
      const prevIndex = previousIndices[previousIndices.length - 2];
      setPreviousIndices(prevIndices => prevIndices.slice(0, -1));
      setCurrentIndex(prevIndex);
      setSecondsPerPhoto(defaultSecondsPerPhoto); // Reset the timer to default
    }
  }, [previousIndices, defaultSecondsPerPhoto]);

  const handleToggleTimer = () => {
    setIsRunning(prevIsRunning => !prevIsRunning);
  };

  useEffect(() => {
    const handleKeyDown = (e) => {
      if (!isRunning) return; // Ignore key presses if timer is stopped
      if (e.key === 'ArrowRight') {
        handleNext();
      } else if (e.key === 'ArrowLeft') {
        handlePrevious();
      }
    };
  
    document.addEventListener('keydown', handleKeyDown);
  
    return () => {
      document.removeEventListener('keydown', handleKeyDown);
    };
  }, [handleNext, handlePrevious, isRunning]); // Update dependency array

  const handleCustomTimeChange = (e) => {
    const value = e.target.value.trim();
    if (value === '' || /^\d*\.?\d+$/.test(value)) {
      setCustomTime(value);
    }
  };

  const handlePredefinedTimeChange = (e) => {
    setCustomTime(e.target.value);
    setSecondsPerPhoto(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (parseFloat(customTime) > 0) {
      setSecondsPerPhoto(customTime);
      setFormSubmitted(true);
      setTimeLeft(parseFloat(customTime) * 60); // Convert minutes to seconds
    }
  };

  return (
    <div className='photo' style={{ position: 'relative' }}>
      <h2>Niutah Assets</h2>
      {!formSubmitted && (
        <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor="custom">Custom: </label>
            <input 
              type="text" 
              id="custom" 
              name="custom" 
              value={customTime} 
              onChange={handleCustomTimeChange} 
              placeholder="Enter custom time" 
            />
            <br />
            <span>Predefined:</span>
            {predefinedTimes.map((time, index) => (
              <label key={index}>
                <input 
                  type="radio" 
                  name="predefinedTime" 
                  value={time.value} 
                  checked={secondsPerPhoto === String(time.value)} 
                  onChange={handlePredefinedTimeChange} 
                /> 
                {time.label}
              </label>
            ))}
            <br />
            <button type="submit">Submit</button>
          </div>
        </form>
      )}
      {formSubmitted && secondsPerPhoto !== '' && (
        <div>
          {photos.length > 0 && (
            <>
              <div className='timer' style={{ position: 'absolute', top: 0, right: 0 }}>
                <h3>Time left: {Math.floor(timeLeft / 60)}:{timeLeft % 60 < 10 ? `0${timeLeft % 60}` : timeLeft % 60} min</h3>
              </div>
              {timeLeft !== null && (
                <img src={photos[currentIndex].path} alt={photos[currentIndex].name} />
              )}
              <div>
                <br/>
                <button onClick={handlePrevious}>PREVIOUS</button> &nbsp;
                <button onClick={handleToggleTimer}>{isRunning ? 'STOP' : 'START'}</button> &nbsp; 
                <button onClick={handleNext}>NEXT</button>
              </div>
            </>
          )}
        </div>
      )}
    </div>
  );
};

export default RandomPhoto;
