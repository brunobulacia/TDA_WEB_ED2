import { cy, initializeCytoscape } from "./graph.js";
import { consumeAPI } from "../js/connection.js";

export async function inicializarGrafo() {
  initializeCytoscape();
  await fetchAPI();
}

export async function fetchAPI() {
  const datos = await consumeAPI();
  console.log(datos);
  for (const dato of datos) {
    cy.add({
      group: "nodes",
      data: { id: dato, label: dato },
    });
  }
}
