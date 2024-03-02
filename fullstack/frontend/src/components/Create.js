import {React} from 'react'
import {useForm} from 'react-hook-form'
import {Box, Button, Typography} from '@mui/material'
import {MyDatePickerField} from './forms/MyDatePickerField'
import {MyMultilineField} from './forms/MyMultilineField'
import {MySelectField} from './forms/MySelectField'
import {MyTextField} from './forms/MyTextField'
import AxiosInstance from './forms/Axios'
import Dayjs from 'dayjs'
import {useNavigate} from 'react-router-dom'

export const Create = () => {

  const navigate = useNavigate()

  const defaultValues = {
    name:'',
    comments:'', 
    status:''
  }

  const {handleSubmit, reset, setValue, control} = useForm({defaultValues:defaultValues})
  const submission = (data) => {
    
    const StartDate = Dayjs(data.start_date["$d"]).format("YYYY-MM-DD")
    const EndDate = Dayjs(data.end_date["$d"]).format("YYYY-MM-DD")

    AxiosInstance.post(`project/`,{
      name: data.name,
      status: data.status,
      comments: data.comments,
      start_date: StartDate,
      end_date: EndDate,
    })
    .then((res) => {
      navigate(`/`)
    })
  }

  const hardcoded_options = [
    {id:'', name:'None'}, 
    {id:'Open', name:'Open'}, 
    {id:'In progress', name:'In progress'}, 
    {id:'Completed', name:'Completed'}, 
  ]

  return (
    <div>
      <form onSubmit={handleSubmit(submission)}>
      <Box sx={{display: 'flex', width:'100%', backgroundColor:'#00003f', marginBottom:'10px'}}>
        <Typography sx={{marginLeft:'20px', color:'#fff'}}>
          Create records
        </Typography>
      </Box>
      <Box sx={{display: 'flex', width:'100%', boxShadow:2, padding:4, flexDirection:'column'}}>
        <Box sx={{display: 'flex', justifyContent:"space-around", alignItems:'center'}}>
          <MyTextField 
            label='Name'
            placeholder='Provide a project name'
            name='name' 
            control={control}
            width={'30%'}
          />

          <MyDatePickerField 
            label='Start date'
            name='start_date'
            control={control}
            width={'30%'}
          />
          
          <MyDatePickerField 
            label='End date'
            name='end_date'
            control={control}
            width={'30%'}
          />

        </Box>

        <Box sx={{display: 'flex', justifyContent:"space-around", marginTop:'40px'}}>
          <MyMultilineField 
            label='Comments'
            placeholder='Provide a project comments'
            name='comments'
            control={control}
            width={'30%'}
          />

          <MySelectField 
            label='Status'
            name='status'
            control={control}
            width={'30%'}
            options = {hardcoded_options}
          />
          <Box sx={{width:'30%'}}>
            <Button variant="contained" type="submit" sx={{width:"100%"}}>
              Submit
            </Button>
          </Box>

        </Box>
      </Box>
      </form>

    </div>
  )
}
