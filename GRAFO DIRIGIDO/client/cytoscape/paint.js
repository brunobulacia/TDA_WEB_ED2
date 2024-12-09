import { cy, initializeCytoscape } from "./graph.js";
import { getGrafoAPI } from "../js/connection.js";
let aristas = [];
let vertices = [];
export async function inicializarGrafo() {
  initializeCytoscape();
  await addVertices();
  await addAristas();
  ajustarGrafo();
}

export async function addVertices() {
  const grafo = await getGrafoAPI();
  console.log(Object.entries(grafo));
  for (const [vertice, vecinos] of Object.entries(grafo)) {
    vertices.push({
      group: "nodes",
      data: { id: vertice, label: vertice },
    });
    for (const [vecino, peso] of vecinos) {
      aristas.push({
        group: "edges",
        data: { id: `${vertice}-${vecino}`, source: vertice, target: vecino },
        style: {
          label: `${peso}`,
        },
      });
    }
  }
  cy.add(vertices);
}

export async function addAristas() {
  cy.add(aristas);
}

function ajustarGrafo() {
  const layout = cy.layout({
    name: "circle",
    spacingFactor: 0.4,
    animate: true,
    animationDuration: 500,
    animationEasing: "ease-in-out",
  });

  layout.run();
}
