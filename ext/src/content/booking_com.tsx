import * as React from 'react'
import * as ReactDOM from 'react-dom'
import { InlineRating } from "@src/components/inline_rating/component";
import { getScoreData, getSingleData } from '@src/api/data';

const log = console.log;

const INTERSECTION_RATIO = 0.5

const onViewportEnter = (el: Element) => new Promise<void>(resolve => {
  const options = {
    root: null,
    rootMargin: "0px",
    threshold: [INTERSECTION_RATIO]
  };
  const o = new IntersectionObserver(([ent], obs) => {
    if (ent.intersectionRatio <= 0) return;

    resolve();
    obs.disconnect();
  }, options);
  o.observe(el);
});

const injectSearchResults = () => {
  let table = document.getElementById("search_results_table");

  let cards = table?.querySelectorAll('[data-testid="property-card"]')

  cards?.forEach(el => {
    let tooltip = document.createElement("div");

    let new_elem = el?.children[0]?.children[1]?.children[0]?.lastElementChild?.insertAdjacentElement('beforebegin', tooltip);

    if (!new_elem) {
      console.error("Failed to insert a tooltip")
      return;
    }

    let link = el.querySelector('[data-testid="title-link"]')?.getAttribute("href");

    if (!link) {
      console.error("Failed to follow a link to a search result")
      return;
    }

    let data = (async () => {
      await onViewportEnter(new_elem!);

      let resp = await fetch(link!);
      let txt = await resp.text();

      let p = new DOMParser().parseFromString(txt, 'text/html');

      let map = p.querySelector("a#hotel_sidebar_static_map");
      let latlng = map?.getAttribute("data-atlas-latlng")?.split(",").map(x => parseFloat(x));
      if (!latlng) throw new Error("Location coords not found");

      return latlng
    })();
    
    let comps = {
      air: data.then(l => getSingleData("air", l[0], l[1])),
      light: data.then(l => getSingleData("light", l[0], l[1])),
      noise: data.then(l => getSingleData("noise", l[0], l[1])),
    }

    let rating = React.createElement(InlineRating, comps);
    ReactDOM.render(rating, tooltip);
  });
}

window.addEventListener("load", () => {
  if (window.location.pathname.startsWith("/searchresults")) {
    injectSearchResults();
  }
});
