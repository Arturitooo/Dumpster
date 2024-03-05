import {React, useEffect, useState} from 'react'
import {useForm} from 'react-hook-form'
import {Box, Button, Typography} from '@mui/material'
import {MyDatePickerField} from './forms/MyDatePickerField'
import {MyMultilineField} from './forms/MyMultilineField'
import {MySelectField} from './forms/MySelectField'
import {MyTextField} from './forms/MyTextField'
import AxiosInstance from './Axios'
import Dayjs from 'dayjs'
import {useNavigate, useParams} from 'react-router-dom'


export const Edit = () => {

  const [projectmanager, setProjectmanager] = useState()
  const [loading, setLoading] = useState(true)

  const hardcoded_options = [
    {id:'', name:'None'}, 
    {id:'Open', name:'Open'}, 
    {id:'In progress', name:'In progress'}, 
    {id:'Completed', name:'Completed'}, 
  ]

  const MyParam = useParams()
  const MyId = MyParam.id
  const navigate = useNavigate()

  const defaultValues = {
    name:'',
    comments:'', 
    status:''
  }


  const GetData = () => {
    AxiosInstance.get(`project/${MyId}`).then((res) => {
      console.log(res.data)
      setValue('name',res.data.name)
      setValue('status',res.data.status)
      setValue('projectmanager',res.data.projectmanager)
      setValue('comments',res.data.comments)
      setValue('start_date',Dayjs(res.data.start_date))
      setValue('end_date',Dayjs(res.data.end_date))
    })

    AxiosInstance.get(`projectmanager/`).then((res) => {
      setProjectmanager(res.data)
      console.log(res.data)
      setLoading(false)
    })
  }

  useEffect(() => {
    GetData();
  },[] )

  const {handleSubmit, setValue, control} = useForm({defaultValues:defaultValues})
  const submission = (data) => {
    
    const StartDate = Dayjs(data.start_date["$d"]).format("YYYY-MM-DD")
    const EndDate = Dayjs(data.end_date["$d"]).format("YYYY-MM-DD")

    AxiosInstance.put(`project/${MyId}/`,{
      name: data.name,
      projectmanager: data.projectmanager,
      status: data.status,
      comments: data.comments,
      start_date: StartDate,
      end_date: EndDate,
    })
    .then((res) => {
      navigate(`/`)
    })
  }


  return (
    <div>
      { 
      loading ? <p>Loading data...</p> : 
      <form onSubmit={handleSubmit(submission)}>
      <Box sx={{display: 'flex', width:'100%', backgroundColor:'#00003f', marginBottom:'10px'}}>
        <Typography sx={{marginLeft:'20px', color:'#fff'}}>
          Edit records
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

          <MySelectField 
            label='Project manager'
            name='projectmanager'
            control={control}
            width={'30%'}
            options = {projectmanager}
          />

        </Box>

        <Box sx={{display: 'flex', justifyContent:"start", marginTop:'40px'}}>
          <Button variant="contained" type="submit" sx={{width:"30%"}}>
            Submit
          </Button>
        </Box>

      </Box>
      </form>
      }

    </div>
  )
}
