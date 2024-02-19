import React from 'react'
import { Row } from './Row'

export const Table = ({ items }) => {
  return (
    <div className='table-container'>
        <table>
            <tbody>
                {items.map(item => (
                    <Row key={item.id} item={item} />
                ))}
            </tbody>
        </table>
    </div>
  )
}
