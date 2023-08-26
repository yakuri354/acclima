import { Skeleton } from "@chakra-ui/react";
import React, { FunctionComponent, useState, useEffect } from 'react'

export type LazyDataProps = {
    placeholder: string,
    data: Promise<string>
}

export const LazyData: FunctionComponent<LazyDataProps> = ({placeholder, data}: LazyDataProps) => {
    const [text, setText] = useState<string>(placeholder);
    const [loaded, setLoaded] = useState<boolean>(false);
    
    useEffect(() => {
        if (!loaded) {
            data.then(v => {
                setLoaded(true)
                setText(v)
            }).catch(e => {
                console.error(e)
                setLoaded(true)
                setText("Error :(")
            })
        }
    })
    
    return (
        <Skeleton isLoaded={loaded}>{text}</Skeleton>
    )
}