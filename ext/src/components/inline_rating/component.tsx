import { Box, Flex, Heading } from '@chakra-ui/layout'
import { Skeleton, Spacer } from '@chakra-ui/react';
import { emptyScoreData, getScoreData } from '@src/api/data';
import React, { FunctionComponent, useEffect, useState } from 'react'

type RatingState = "loading" | "ready" | "hover" | "popup" | "error"

type InlineRatingProps = {
  lat: number,
  lng: number
}

const displayScore = (x: number) => (x * 10).toFixed(1)

export const InlineRating: FunctionComponent<InlineRatingProps> = ({lat, lng}: InlineRatingProps) => {
  const [ratingState, setRatingState] = useState("loading" as RatingState);
  const [scoreData, setScoreData] = useState(emptyScoreData)

  const loaded = ratingState != "loading"

  useEffect(() => {
    if (!loaded) {
      getScoreData(lat, lng)
        .then(setScoreData)
        .then(() => setRatingState("ready"))
        .catch((e: any) => {
          setRatingState("error")
          console.error(e)
        });
    }
  });

  if (ratingState == 'error') {
    return (
        <Box>
          <Heading size="lg">
            Error occured
          </Heading>
        </Box>
    );
  }

  return (
    <Box maxW='sm' borderWidth='1px' borderRadius='lg' overflow='hidden'>
      <Heading size="md">
        <Flex>
          <Flex direction="row">
            Air
            <Spacer w="1ch"/>
            <Skeleton isLoaded={loaded}>{displayScore(scoreData.scores.air)}</Skeleton>
          </Flex>
          <Spacer/>
          <Flex direction="row">
            Light
            <Spacer w="1ch"/>
            <Skeleton isLoaded={loaded}>{displayScore(scoreData.scores.light)}</Skeleton>
          </Flex>
          <Spacer/>
          <Flex direction="row">
            Noise
            <Spacer w="1ch"/>
            <Skeleton isLoaded={loaded}>{displayScore(scoreData.scores.noise)}</Skeleton>
          </Flex>
        </Flex>
      </Heading>
    </Box>
  )
}
