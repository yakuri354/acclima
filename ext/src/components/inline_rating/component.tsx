import { Box, Flex, Heading } from '@chakra-ui/layout'
import { Skeleton, Spacer } from '@chakra-ui/react';
import { emptyScoreData, AllDataPromises } from '@src/api/data';
import React, { FunctionComponent, useEffect, useState } from 'react'
import { LazyData } from './lazy_data';

type InlineRatingProps = AllDataPromises;
const displayScore = (x: number) => (x * 10).toFixed(1)

export const InlineRating: FunctionComponent<InlineRatingProps> = ({air, light, noise}: InlineRatingProps) => {
  const [air_s, light_s, noise_s] = [air, light, noise].map(p => p.then(x => displayScore(x.score)))

  return (
    <Box maxW='sm' borderWidth='1px' borderRadius='lg' overflow='hidden'>
      <Heading size="md">
        <Flex>
          <Flex direction="row">
            Air
            <Spacer w="1ch"/>
            <LazyData placeholder={displayScore(emptyScoreData.scores.air)} data={air_s}></LazyData>
          </Flex>
          <Spacer/>
          <Flex direction="row">
            Light
            <Spacer w="1ch"/>
            <LazyData placeholder={displayScore(emptyScoreData.scores.light)} data={light_s}></LazyData>
          </Flex>
          <Spacer/>
          <Flex direction="row">
            Noise
            <Spacer w="1ch"/>
            <LazyData placeholder={displayScore(emptyScoreData.scores.noise)} data={noise_s}></LazyData>
          </Flex>
        </Flex>
      </Heading>
    </Box>
  )
}
