import * as React from 'react';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import {Controller} from 'react-hook-form';

export function MyDatePickerField(props) {
  const {label, name, control, width} = props
  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>

<Controller
    name = {name}
    control = {control}
    render = {({
      field:{onChange, value},
    }) => (
      <DatePicker 
      sx={{width:{width}}}
      onChange={onChange}
      value={value}
      label={label}
      
       />
    )
    }      
  />
    </LocalizationProvider>
  );
}
