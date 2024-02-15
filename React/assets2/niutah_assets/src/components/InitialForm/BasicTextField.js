import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import { useState } from 'react';

export default function BasicTextField() {
  const [timePerPhoto, setTimePerPhoto] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    const inputValue = parseFloat(event.target.elements.input.value);
    if (!isNaN(inputValue)) {
      setTimePerPhoto(inputValue === 1 ? '1 minute' : `${inputValue} minutes`);
    } else {
      alert('Please enter a valid number.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <Box
        sx={{
          '& > :not(style)': { m: 0, width: '25ch' },
        }}
        noValidate
        autoComplete="off"
      >
        <TextField 
          id="outlined-basic" 
          name="input"
          label="Custom time (minutes)" 
          variant="outlined" 
          type="number"
          inputProps={{
            step: 'any',
            pattern: '[0-9]+([,.][0-9]+)?', 
            min: 0,
          }}
        />
      </Box>
      <Button variant="contained" type="submit" style={{margin:"5px"}}>Submit</Button>
      {timePerPhoto && <p>Time per photo: {timePerPhoto}</p>}
    </form>
  );
}