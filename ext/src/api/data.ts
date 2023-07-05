type ScoreData = {
  overall: number,
  scores: {
    air: number,
    light: number,
    noise: number
  }
}

export const emptyScoreData: ScoreData = {
  overall: 1.0,
  scores: {
    air: 1.0,
    light: 1.0,
    noise: 1.0
  }
}

const apiUrl = "http://localhost:8000";
export async function getScoreData(lat: number, lng: number): Promise<ScoreData> {
  return new Promise(resolve => setTimeout(() => resolve(emptyScoreData), 500));
}

// export async function getScoreData(lat: number, lng: number): Promise<ScoreData> {
//   return fetch(apiUrl + `/data/${lat}/${lng}`).then(r => r.json()).then(r => {console.log(r); return r;});
// }
