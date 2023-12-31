export type ScoreData = {
  overall: number,
  scores: {
    air: number,
    light: number,
    noise: number
  }
}

export type SingleData = {
  score: number,
  data: any
}

export type emptySingleData = {
  score: 0.0,
  data: {}
}

export type AllDataPromises = {
  air: Promise<SingleData>,
  light: Promise<SingleData>,
  noise: Promise<SingleData>
};

export const emptyScoreData: ScoreData = {
  overall: 1.0,
  scores: {
    air: 1.0,
    light: 1.0,
    noise: 1.0
  }
}

const apiUrl = "http://localhost:8000";

// export async function getScoreData(lat: number, lng: number): Promise<ScoreData> {
//   let fakeScoreData = emptyScoreData;
//   fakeScoreData.scores.air = lat;
//   fakeScoreData.scores.light = lng;
//   return new Promise(resolve => setTimeout(() => resolve(fakeScoreData), 2000));
// }

export function getAllData(lat: number, lng: number): AllDataPromises {
  return {
    air: getSingleData("air", lat, lng),
    light: getSingleData("light", lat, lng),
    noise: getSingleData("noise", lat, lng)
  }
}

export async function getSingleData(kind: string, lat: number, lng: number): Promise<SingleData> {
  return fetch(apiUrl + `/${kind}/${lat}/${lng}`)
    .then(r => r.json())
    .then(r => {console.log(r); return r;});
}

export async function getScoreData(kind: string, lat: number, lng: number): Promise<ScoreData> {
  return fetch(apiUrl + `/data/${lat}/${lng}`)
    .then(r => r.json())
    .then(r => {console.log(r); return r;});
}