import React from 'react'
import { ListItem } from './ListItem'

export const List = ({items}) => {
  return (
    <ul>
        {items.map(item => (
            <ListItem key={item.id} item={item} />
        ))}

    </ul>
  )
}
