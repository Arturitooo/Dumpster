import React from 'react'
import BasicTextField from "./BasicTextField"

export const InitialForm = () => {
  return (
    <div style={{display: "flex", justifyContent: "center", alignItems: "center" }}>
      <div style={{textAlign: "center"}}>
          <h3>Specify how much time you want to display each image</h3>
          <BasicTextField/>
      </div>
    </div>
  )
}
