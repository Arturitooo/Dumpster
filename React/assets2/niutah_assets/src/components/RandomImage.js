import React, { useState, useEffect, useRef } from 'react';
import Button from '@mui/material/Button';

const RandomImage = ({ timePerPhoto, selectedRoot }) => {
  const [images, setImages] = useState([]);
  const [currentImageIndex, setCurrentImageIndex] = useState(0);
  const [isRunning, setIsRunning] = useState(true);
  const [buttonText, setButtonText] = useState('Stop');
  const [timeRemaining, setTimeRemaining] = useState(timePerPhoto);
  const [previousImages, setPreviousImages] = useState([]);
  const timerRef = useRef(null);

  useEffect(() => {
  const importAll = (r) => r.keys().map(r);

  // Dynamically import images based on the selected root folder
  let imagesArray;
  switch (selectedRoot) {
    case 'folder1':
      imagesArray = importAll(require.context(`../assets/folder1`, false, /\.(png|jpe?g|svg)$/));
      break;
    case 'folder2':
      imagesArray = importAll(require.context(`../assets/folder2`, false, /\.(png|jpe?g|svg)$/));
      break;
    case 'folder3':
      imagesArray = importAll(require.context(`../assets/folder3`, false, /\.(png|jpe?g|svg)$/));
      break;
    default:
      imagesArray = importAll(require.context('../assets', false, /\.(png|jpe?g|svg)$/));
  }

  setImages(imagesArray);

  timerRef.current = setInterval(() => {
    if (isRunning) {
      setTimeRemaining((prevTime) => {
        if (prevTime === 0) {
          const nextIndex = (currentImageIndex + 1) % imagesArray.length;
          setCurrentImageIndex(nextIndex);
          setPreviousImages((prevImages) => {
            const updatedImages = [...prevImages, imagesArray[nextIndex]].slice(-10);
            return updatedImages;
          });
          return timePerPhoto;
        } else {
          return prevTime - 1;
        }
      });
    }
  }, 1000);

  const handleKeyPress = (event) => {
    if (event.code === 'Space' && event.target.tagName !== 'INPUT') {
      event.preventDefault();
      handleStartStopClick();
    } else if (event.code === 'ArrowRight') {
      handleNextButtonClick();
    } else if (event.code === 'ArrowLeft') {
      handlePreviousButtonClick();
    }
  };

  document.addEventListener('keydown', handleKeyPress);

  return () => {
    clearInterval(timerRef.current);
    document.removeEventListener('keydown', handleKeyPress);
  };
}, [timePerPhoto, isRunning, currentImageIndex, selectedRoot]); // Include necessary dependencies here

  const handleStartStopClick = () => {
    setIsRunning((prev) => !prev);
    setButtonText((prev) => (prev === 'Stop' ? 'Start' : 'Stop'));
  };

  const handleNextButtonClick = () => {
    setCurrentImageIndex((prevIndex) => (prevIndex + 1) % images.length);
    setTimeRemaining(timePerPhoto); // Reset time remaining to default
  };

  const handlePreviousButtonClick = () => {
    setCurrentImageIndex((prevIndex) => (prevIndex === 0 ? images.length - 1 : prevIndex - 1));
    setTimeRemaining(timePerPhoto); // Reset time remaining to default
  };

  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        {images.length > 0 && (
          <img src={images[currentImageIndex]} alt="" style={{ maxHeight: '80vh', maxWidth: '100vh', margin: 'auto'}} />
        )}
      </div>

      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', position: 'absolute', bottom: '15px', left: '50%', transform: 'translateX(-50%)' }}>
        <Button variant="contained" onClick={handlePreviousButtonClick} style={{ marginRight: '10px' }}>Previous</Button>
        <Button variant="contained" onClick={handleStartStopClick}>{buttonText}</Button>
        <Button variant="contained" onClick={handleNextButtonClick} style={{ marginLeft: '10px' }}>Next</Button>
      </div>

      <div style={{ position: 'absolute', right: "20px", top: "-2px" }}><h4>{formatTime(timeRemaining)}</h4></div>
    </div>
  );
};

const formatTime = (seconds) => {
  const minutes = Math.floor(seconds / 60);
  const remainingSeconds = seconds % 60;
  return `${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`;
};

export { RandomImage };
