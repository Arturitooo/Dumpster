import React, { useState, useEffect } from 'react';

const RandomImage = ({ timePerPhoto, selectedRoot }) => {
  const [images, setImages] = useState([]);
  const [currentImageIndex, setCurrentImageIndex] = useState(0);

  useEffect(() => {
    // Function to import all images from the assets folder
    const importAll = (r) => r.keys().map(r);

    // Define images lists for each folder
    let imagesList;
    switch (selectedRoot) {
      case 'folder1':
        imagesList = importAll(require.context('../assets/folder1', false, /\.(png|jpe?g|svg)$/));
        break;
      case 'folder2':
        imagesList = importAll(require.context('../assets/folder2', false, /\.(png|jpe?g|svg)$/));
        break;
      case 'folder3':
        imagesList = importAll(require.context('../assets/folder3', false, /\.(png|jpe?g|svg)$/));
        break;
      default:
        imagesList = importAll(require.context('../assets', false, /\.(png|jpe?g|svg)$/));
    }

    // Shuffle the images array
    const shuffledImagesArray = shuffleArray(imagesList);

    // Set the images state with the shuffled images array
    setImages(shuffledImagesArray);

    // Set up interval to change image
    const interval = setInterval(() => {
      setCurrentImageIndex((prevIndex) => (prevIndex + 1) % shuffledImagesArray.length);
    }, timePerPhoto * 1000); // Convert seconds to milliseconds

    // Clean up interval on component unmount
    return () => clearInterval(interval);
  }, [timePerPhoto, selectedRoot]);

  // Function to shuffle the array
  const shuffleArray = (array) => {
    const newArray = [...array];
    for (let i = newArray.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [newArray[i], newArray[j]] = [newArray[j], newArray[i]];
    }
    return newArray;
  };

  return (
    <div style={{ marginTop: '20px', marginLeft:'auto', marginRight:'auto', maxHeight: '75%', maxWidth: '90%', overflow: 'hidden' }}>
      {/* Displaying current image based on currentImageIndex */}
      {images.length > 0 && (
        <div style={{ maxHeight: '80vh', maxWidth: '100vh', margin: 'auto' }}>
          <img
            src={images[currentImageIndex]}
            alt=""
            style={{ width: '100%', height: '100%', objectFit: 'contain' }}
          />
        </div>
      )}
    </div>
  );
};

export { RandomImage };
