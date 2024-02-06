import { Stack, Button } from '@mui/material'

export const MuiButton = () => {
  return (
    <Stack spacing = {4}>
        <Stack spacing = {2} direction = "row">
            <Button variant = "text">Text</Button>
            <Button variant = "contained">Contained</Button>
            <Button variant = "outlined">Outlined</Button>
        </Stack>

        <Stack spacing = {1} direction = "row">
            <Button variant = "contained" color='primary' >Primary</Button>
            <Button variant = "contained" color='secondary' >Secondary</Button>
            <Button variant = "contained" color='error' >Error</Button>
            <Button variant = "contained" color='warning' >warning</Button>
            <Button variant = "contained" color='info' >info</Button>
            <Button variant = "contained" color='success' >success</Button>
        </Stack>
    </Stack>
)
}
