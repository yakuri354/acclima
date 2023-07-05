import * as React from 'react'
import * as ReactDOM from 'react-dom'
import { InlineRating } from "@src/components/inline_rating/component";

window.addEventListener("load", () => {
  let table = document.getElementById("search_results_table");

  let cards = table?.querySelectorAll('[data-testid="property-card"]')

  cards?.forEach(el => {
    let tooltip = document.createElement("div");
    let new_elem = undefined;

    let card_text = el?.children[0]?.children[1]?.children[0];
    if (card_text?.children?.length) {
      new_elem = card_text.insertBefore(tooltip, card_text.lastChild);
    }

    if (!new_elem) {
      console.error("Failed to insert a tooltip")
    }

    let rating = React.createElement(InlineRating, {lat: 55, lng: 37});
    ReactDOM.render(rating, tooltip);
  });
});
