import React, { useState, useEffect } from 'react';
import './App.css';
import RandomPhoto from './RandomPhoto';

function App() {
  const [images, setImages] = useState([]);

  useEffect(() => {
    const importImages = async () => {
      const imageContext = require.context('./assets', false, /\.(jpg|jpeg|png)$/);
      const imagePaths = imageContext.keys().map(imageContext);
      const imageObjects = imagePaths.map((path, index) => ({ name: `Image ${index + 1}`, path }));
      setImages(imageObjects); // Update images state with all images found in the assets folder
    };
    importImages();
  }, []); // Empty dependency array ensures useEffect runs only once, on component mount

  return (
    <div className="App">
      <RandomPhoto photos={images} />
    </div>
  );
}

export default App;
