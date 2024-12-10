import { cy, initializeCytoscape } from "/client/cytoscape/graph.js";
// import { getNodes, getRoot } from "/client/js/connection.js";
import { getTreeAPI } from "../js/connection.js";
let nodes = [];
let edges = [];

export async function inicializarGrafo() {
  await initializeCytoscape();
  await addVertices();
  await addAristas();
  // ajustarGrafo();
}

export async function addVertices() {
  nodes = await getTreeAPI();
  console.log(Object.entries(nodes));
  let fuck = [];
  for (const [key, value] of Object.entries(nodes)) {
    // console.log(key, value);
    for (let i = 0; i < value.length; i++) {
      console.log(value[i]);
      fuck.push({
        data: {
          id: String(value[i][0]),
        },
        style: {
          width: value[i][0].length * 30 + 10,
        },
      });
    }
  }
  cy.add(fuck);
}
export async function addAristas() {
  nodes = await getTreeAPI();
  console.log(Object.entries(nodes));
  let aristas = [];
  for (const [key, value] of Object.entries(nodes)) {
    for (let i = 0; i < value.length; i++) {
      aristas.push({
        data: {
          id: String(value[i][1]) + "-" + String(value[i][0]),
          source: String(value[i][1]), // El padre
          target: String(value[i][0]), // El nodo actual
        },
      });
    }
  }
  console.log(aristas.slice(1, aristas.length));
  cy.add(aristas.slice(1, aristas.length));
}
/*

async function ajustarGrafo() {
  const nodos = await getNodes();
  let horizontalSpacing = Math.pow(2, nodos[nodos.length - 1][2] + 4);
  let verticalSpacing = 50; //
  let rootX = 500; // Posición inicial de la raíz en el eje X (mantener o ajustar)
  let rootY = 50; // Posición inicial de la raíz en el eje Y (mantener o ajustar)
  // Recorrer cada nodo para posicionarlos
  nodos.forEach((node) => {
    let parent = cy.getElementById(String(node[1])); // Obtener el nodo padre
    let child = cy.getElementById(String(node[0])); // Obtener el nodo hijo
    let posX, posY;
    let posParent = parent.position();
    posY = posParent.y + verticalSpacing; // El hijo siempre estará debajo del padre, con menos altura
    // Ajustamos el espaciado horizontal según el nivel del nodo
    let depth = node[2]; // La profundidad del nodo
    let levelSpacing = horizontalSpacing / Math.pow(2, depth); // Reducimos el espacio con la profundidad

    if (node[0] < node[1]) {
      // El hijo es menor que el padre, va a la izquierda
      posX = posParent.x - levelSpacing;
    } else {
      // El hijo es mayor que el padre, va a la derecha
      posX = posParent.x + levelSpacing;
    }
    // Actualizamos la posición del nodo hijo
    child.position({ x: posX, y: posY });
  });
} */

export function searchNodePaint(e) {
  let foundNode = null;
  foundNode = cy.getElementById(e);
  if (foundNode) {
    foundNode.style("background-color", "#ffff00");
  }
  setTimeout(() => {
    foundNode.style("background-color", "#1A7F8F");
  }, 2000);
}
