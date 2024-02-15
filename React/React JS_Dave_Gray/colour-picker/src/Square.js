import React from 'react'

const Square = ({ colorValue, hexValue, isDarkText }) => {
  return (
    <section
        className='square'
        style = {{
          backgroundColor: colorValue,
          color: isDarkText ? "#363435" : "#b5b5b5"
        }}
    >
        <p>{colorValue ? colorValue : "Empty value"}</p>
        <p>{hexValue ? hexValue : null}</p>
    </section>
  )
}

Square.defaultProps = {
    colorValue: "Empty Color value"
}

export default Square