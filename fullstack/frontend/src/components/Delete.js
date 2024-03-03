import {React, useEffect, useState} from 'react'
import {Box, Button, Typography} from '@mui/material'
import AxiosInstance from './Axios'
import {useNavigate, useParams} from 'react-router-dom'


export const Delete = () => {
  const MyParam = useParams()
  const MyId = MyParam.id
  const navigate = useNavigate()

  const [myData, setMyData] = useState()
  const [loading, setLoading] = useState(true)

  const GetData = () => {
    AxiosInstance.get(`project/${MyId}`).then((res) => {
      setMyData(res.data)
      console.log(res.data)
      setLoading(false)
    })
  }

  useEffect(() => {
    GetData();
  },[] )

  const submission = (data) => {

    AxiosInstance.delete(`project/${MyId}/`,{
    })
    .then((res) => {
      navigate(`/`)
    })
  }

  return (
    <div>
    { 
    loading ? <p>Loading data...</p> :
    <div>
      <Box sx={{display: 'flex', width:'100%', backgroundColor:'#00003f', marginBottom:'10px'}}>
        <Typography sx={{marginLeft:'20px', color:'#fff'}}>
          Delete project: {myData.name}
        </Typography>
      </Box>

      <Box sx={{display: 'flex', width:'100%', boxShadow:2, padding:4, flexDirection:'column'}}>
        <Box sx={{display: 'flex', justifyContent:"start", alignItems:'center'}}> 
          Are you sure that you want to delete project: {myData.name}
        </Box>

        <Box sx={{width:'30%', justifyContent:"end"}}>
          <Button variant="contained" onClick={submission} sx={{width:"100%", backgroundColor:"red"}}>
            Delete the project
          </Button>
        </Box>

      </Box>
    </div>
    }
    </div>
  )
}
