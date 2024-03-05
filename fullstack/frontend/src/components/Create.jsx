import {React, useEffect, useState} from 'react'
import {useForm} from 'react-hook-form'
import {Box, Button, Typography} from '@mui/material'
import {MyDatePickerField} from './forms/MyDatePickerField'
import {MyMultilineField} from './forms/MyMultilineField'
import {MySelectField} from './forms/MySelectField'
import {MyTextField} from './forms/MyTextField'
import AxiosInstance from './Axios'
import Dayjs from 'dayjs'
import {useNavigate} from 'react-router-dom'
import { yupResolver } from "@hookform/resolvers/yup"
import * as yup from "yup"

export const Create = () => {

  const [projectmanager, setProjectmanager] = useState()
  const [loading, setLoading] = useState(true)

  const GetData = () => {
    AxiosInstance.get(`projectmanager/`).then((res) => {
      setProjectmanager(res.data)
      console.log(res.data)
      setLoading(false)
    })
  }

  useEffect(() => {
    GetData();
  },[] )

  const navigate = useNavigate()

  const defaultValues = {
    name:'',
    comments:'', 
    status:''
  }


  //validation rulesp rovided with react hook form and yup
  const schema = yup
  .object({
    name: yup.string().required("Name is required field"),
    projectmanager: yup.string().required("Name is required field"),
    status: yup.string().required("Status is required field"),
    comments: yup.string(),
    start_date: yup.date().required("Start Date is required field"),
    end_date: yup.date().required("End Date is required field").min(yup.ref('start_date'),'End date needs to be after start date'),
  })

  const {handleSubmit, control} = useForm({defaultValues:defaultValues, resolver:yupResolver(schema)})
  const submission = (data) => {
    
    const StartDate = Dayjs(data.start_date["$d"]).format("YYYY-MM-DD")
    const EndDate = Dayjs(data.end_date["$d"]).format("YYYY-MM-DD")

    AxiosInstance.post(`project/`,{
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

  const hardcoded_options = [
    {id:'', name:'None'}, 
    {id:'Open', name:'Open'}, 
    {id:'In progress', name:'In progress'}, 
    {id:'Completed', name:'Completed'}, 
  ]

  return (
    <div>
      { 
      loading ? <p>Loading data...</p> : 
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
          <MySelectField 
            label='Project manager'
            name='projectmanager'
            control={control}
            width={'30%'}
            options = {projectmanager}
          />

        </Box>
        <Box sx={{display: 'flex', justifyContent:"start", marginTop:'40px'}}>
          <Button variant="contained" type="submit" sx={{width:"30%", margin: "15px"}}>
            Submit
          </Button>
        </Box>
      </Box>
      </form>

    }
    </div>
  )
}
