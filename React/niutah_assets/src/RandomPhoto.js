import React from 'react';

const RandomPhoto = ({ photos }) => {
  const randomIndex = Math.floor(Math.random() * photos.length);
  const randomPhoto = photos[randomIndex];
  

  return (
    <div className='photo'>
      <h2>Niutah Assets</h2>
      {randomPhoto && <img src={randomPhoto.path} alt={randomPhoto.name} />}
    </div>
  );
};

export default RandomPhoto;
