import React, { useState } from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import FormControl from '@mui/material/FormControl';
import FormControlLabel from '@mui/material/FormControlLabel';
import RadioGroup from '@mui/material/RadioGroup';
import Radio from '@mui/material/Radio';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import InputLabel from '@mui/material/InputLabel';

export function InitialForm({ setTimePerPhoto, setSelectedRoot, setShowForm }) {
  const [timePerPhotoInput, setTimePerPhotoInput] = useState('');
  const [selectedTime, setSelectedTime] = useState('');
  const [selectedRootValue, setSelectedRootValue] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    let timeInSeconds;
    if (selectedTime) {
      timeInSeconds = selectedTime * 60;
    } else {
      const inputValue = parseFloat(event.target.elements.input.value.replace(',', '.'));
      if (!isNaN(inputValue)) {
        timeInSeconds = inputValue * 60;
      } else {
        alert('Please enter a valid number or select a predefined value.');
        return;
      }
    }
    setTimePerPhoto(timeInSeconds);
    setTimePerPhotoInput(timeInSeconds); // Update the input field value to reflect the time entered
    setSelectedRoot(selectedRootValue); // Update the selected root directory
  };

  const handleRootChange = (event) => {
    setSelectedRootValue(event.target.value);
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
      <div style={{ textAlign: 'center' }}>
        <h3>How long should each image display?</h3>
        <FormControl component="fieldset" style={{ marginBottom: '20px' }}>
          <RadioGroup
            aria-label="time"
            name="time"
            value={selectedTime}
            onChange={(e) => setSelectedTime(e.target.value)}
            style={{ display: 'flex', flexDirection:'row', columnGap:'15px', justifyContent: 'center' }}
          >
            <FormControlLabel value="0.5" control={<Radio />} label="30 sec" />
            <FormControlLabel value="1" control={<Radio />} label="1 min" />
            <FormControlLabel value="5" control={<Radio />} label="5 mins" />
            <FormControlLabel value="10" control={<Radio />} label="10 mins" />
          </RadioGroup>
        </FormControl>
        <form onSubmit={handleSubmit}>
          <Box
            sx={{
              '& > :not(style)': { m: 0, width: '25ch' },
              marginBottom: '10px'
            }}
            noValidate
            autoComplete="off"
          >
            <TextField 
              id="outlined-basic" 
              name="input"
              label="Custom time (minutes)" 
              variant="outlined" 
              type="text" // Change type to text to allow comma input
              inputProps={{
                step: 'any',
                pattern: '[0-9]+([,.][0-9]+)?', 
                min: 0,
              }}
              value={timePerPhotoInput} // Display the current value entered by the user
              onChange={(e) => setTimePerPhotoInput(e.target.value)} // Update the input field value
            />
          </Box>

          <FormControl style={{ width:'25ch', marginBottom: '10px' }} >
            <InputLabel id="root-select-label">Root Directory</InputLabel>
            <Select
              labelId="root-select-label"
              id="root-select"
              value={selectedRootValue}
              label="Root Directory"
              onChange={handleRootChange}
            >
              <MenuItem value="Default">Default</MenuItem>
              <MenuItem value="folder1">Folder 1</MenuItem> 
              <MenuItem value="folder2">Folder 2</MenuItem>
              <MenuItem value="folder3">Folder 3</MenuItem>
            </Select>
          </FormControl><br/>

          <Button variant="contained" type="submit" style={{margin:"5px"}}>Submit</Button>
        </form>
      </div>
    </div>
  );
}
