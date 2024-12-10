import { cy, initializeCytoscape } from "./graph.js";
import { getGrafoAPI, dijkstraAPI } from "../js/connection.js";
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
    name: "cose",
    spacingFactor: 0.4,
    animate: true,
    animationDuration: 500,
    animationEasing: "ease-in-out",
  });

  layout.run();
}

export function pintarCamino(ruta, distancia) {
  console.log(ruta);
  for (let i = 0; i < ruta.length - 1; i++) {
    setTimeout(() => {
      const origen = ruta[i];
      const destino = ruta[i + 1];
      const arista = cy.edges(`#${origen}-${destino}`);
      arista.style({
        "line-color": "red",
        "target-arrow-color": "red",
        "target-arrow-shape": "triangle",
        width: 8,
      });
    }, i * 500); // 200 ms delay for each edge
  }

  const tiempo = ruta.length * 500; // Total time for the animation

  // Reset the style of all edges after the animation is complete
  setTimeout(() => {
    if (distancia > 0) {
      alert(`Distancia total: ${distancia}`);
    }
    cy.edges().style({
      "line-color": "#F59E0B",
      "target-arrow-color": "#F59E0B",
      "target-arrow-shape": "triangle",
      width: 4,
    });
  }, tiempo); // Add a small delay to ensure the last edge is painted before resetting
}

export function pintarVerticesRecorrido(vertices) {
  for (let i = 0; i < vertices.length; i++) {
    setTimeout(() => {
      const vertice = vertices[i];
      const nodo = cy.nodes(`#${vertice}`);
      nodo.style({
        "background-color": "#e84118",
        "border-color": "#e84118",
        "border-width": 4,
        width: 60,
        height: 60,
      });
    }, i * 500); // 200 ms delay for each edge
  }

  const tiempo = vertices.length * 500; // Total time for the animation
  setTimeout(() => {
    cy.nodes().style({
      "background-color": "#1A7F8F",
      "border-color": "#3B12F6",
      "border-width": 3,
      width: 50,
      height: 50,
    });
  }, tiempo + 500); // Add a small delay to ensure the last edge is painted before resetting
}
